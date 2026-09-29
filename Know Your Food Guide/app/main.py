import csv
import io
import json
import sys
from pathlib import Path

import streamlit as st
from langchain_community.callbacks.manager import get_openai_callback

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag.index import all_splits
from rag import llmfallback
from rag.rag_chain import graph
from rag.router import should_use_rag
from tool_calling.checklist_generation import (
    create_shopping_checklist_word_document,
    is_food_shopping_topic,
    tidy_chat_answer_for_word_export,
    wants_word_checklist,
)
from tool_calling.barcode_lookup import lookup_product_by_barcode
from tool_calling.unit_price_comparison import compare_food_unit_prices

# ---------------------------------------------------------------------------
# Page config & styling (set_page_config before most other st.* calls)
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Know Your Food Guide", page_icon="🥗")


def load_css() -> None:
    css_path = PROJECT_ROOT / "ui.css"
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


load_css()

# ---------------------------------------------------------------------------
# Input limits
# ---------------------------------------------------------------------------
MAX_QUESTION_CHARS = 1000
MIN_QUESTION_CHARS = 8
MIN_QUESTION_WORDS = 2

# Scrollable chat history so long threads don’t stretch the whole page.
CHAT_HISTORY_SCROLL_HEIGHT_PX = 300

CHECKLIST_READY_SUMMARY = (
    "**Checklist ready.** Full shopping tips are in the Word file —use **Download** "
    "below to save the .docx"
)


def _usage_row(
    *,
    provider: str,
    model: str | None,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    cost_usd: float,
    note: str = "",
) -> dict:
    return {
        "provider": provider,
        "model": model,
        "prompt_tokens": int(prompt_tokens),
        "completion_tokens": int(completion_tokens),
        "total_tokens": int(total_tokens),
        "cost_usd": float(cost_usd),
        "note": note,
    }


def _merge_usage(a: dict, b: dict) -> dict:
    model_a = a.get("model")
    model_b = b.get("model")
    if model_a and model_b and model_a != model_b:
        model = f"{model_a} + {model_b}"
    else:
        model = model_a or model_b
    note = " ".join(
        x for x in [str(a.get("note", "")).strip(), str(b.get("note", "")).strip()] if x
    )
    return _usage_row(
        provider=str(a.get("provider") or b.get("provider") or "unknown"),
        model=model,
        prompt_tokens=int(a.get("prompt_tokens", 0)) + int(b.get("prompt_tokens", 0)),
        completion_tokens=int(a.get("completion_tokens", 0))
        + int(b.get("completion_tokens", 0)),
        total_tokens=int(a.get("total_tokens", 0)) + int(b.get("total_tokens", 0)),
        cost_usd=float(a.get("cost_usd", 0.0)) + float(b.get("cost_usd", 0.0)),
        note=note,
    )


def _format_usage_caption(usage: dict) -> str:
    model = usage.get("model") or "n/a"
    base = (
        f"Tokens: prompt {int(usage.get('prompt_tokens', 0))}, "
        f"completion {int(usage.get('completion_tokens', 0))}, "
        f"total {int(usage.get('total_tokens', 0))} | "
        f"Estimated cost: ${float(usage.get('cost_usd', 0.0)):.6f} | "
        f"Model: {model}"
    )
    note = str(usage.get("note", "")).strip()
    return f"{base} | {note}" if note else base


def _fallback_answer_with_usage(question: str) -> tuple[str, list[str], dict]:
    detailed = getattr(llmfallback, "openai_web_fallback_answer_detailed", None)
    if callable(detailed):
        return detailed(question)
    text, urls = llmfallback.openai_web_fallback_answer(question)
    return (
        text,
        urls,
        _usage_row(
            provider="openai",
            model="unknown",
            prompt_tokens=0,
            completion_tokens=0,
            total_tokens=0,
            cost_usd=0.0,
            note="Detailed usage unavailable in current module load; restart app to refresh.",
        ),
    )


def _chat_export_rows(messages: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for idx, msg in enumerate(messages, start=1):
        role = str(msg.get("role", ""))
        content = str(msg.get("content", ""))
        sources = msg.get("sources") or []
        usage = msg.get("usage") or {}
        rows.append(
            {
                "turn": idx,
                "role": role,
                "content": content,
                "sources": " | ".join(str(s) for s in sources),
                "model": str(usage.get("model", "")),
                "prompt_tokens": int(usage.get("prompt_tokens", 0) or 0),
                "completion_tokens": int(usage.get("completion_tokens", 0) or 0),
                "total_tokens": int(usage.get("total_tokens", 0) or 0),
                "cost_usd": float(usage.get("cost_usd", 0.0) or 0.0),
            }
        )
    return rows


def _chat_json_bytes(messages: list[dict]) -> bytes:
    payload = {"messages": _chat_export_rows(messages)}
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")


def _chat_csv_bytes(messages: list[dict]) -> bytes:
    rows = _chat_export_rows(messages)
    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=[
            "turn",
            "role",
            "content",
            "sources",
            "model",
            "prompt_tokens",
            "completion_tokens",
            "total_tokens",
            "cost_usd",
        ],
    )
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode("utf-8")


def _pdf_escape_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _chat_pdf_bytes(messages: list[dict]) -> bytes:
    """
    Minimal one-page PDF generator for quick chat export.
    """
    rows = _chat_export_rows(messages)
    lines: list[str] = ["Know Your Food Guide - Chat Export", ""]
    for row in rows:
        role = (row.get("role") or "").upper()
        content = str(row.get("content") or "").replace("\n", " ").strip()
        if len(content) > 140:
            content = content[:140] + "..."
        lines.append(f"[{row['turn']}] {role}: {content}")

    if len(lines) > 42:
        lines = lines[:42] + ["...", "Output truncated for PDF. Use JSON/CSV for full history."]

    font_size = 10
    leading = 14
    y_start = 800
    text_ops = [
        "BT",
        f"/F1 {font_size} Tf",
        f"72 {y_start} Td",
        f"{leading} TL",
    ]
    first = True
    for line in lines:
        esc = _pdf_escape_text(line)
        if first:
            text_ops.append(f"({esc}) Tj")
            first = False
        else:
            text_ops.append("T*")
            text_ops.append(f"({esc}) Tj")
    text_ops.append("ET")
    stream = "\n".join(text_ops).encode("latin-1", errors="replace")

    objects: list[bytes] = [
        b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n",
        b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n",
        (
            b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >> endobj\n"
        ),
        b"4 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n",
        (
            f"5 0 obj << /Length {len(stream)} >> stream\n".encode("ascii")
            + stream
            + b"\nendstream endobj\n"
        ),
    ]

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for obj in objects:
        offsets.append(len(pdf))
        pdf.extend(obj)
    xref_start = len(pdf)
    pdf.extend(f"xref\n0 {len(offsets)}\n".encode("ascii"))
    pdf.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        pdf.extend(f"{off:010d} 00000 n \n".encode("ascii"))
    pdf.extend(
        f"trailer << /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref_start}\n%%EOF\n".encode(
            "ascii"
        )
    )
    return bytes(pdf)

def clean_question(text: str) -> str | None:
    """Normalize input; return None if too empty, too short, or not wordy enough for RAG."""
    q = " ".join(text.strip().split())
    if not q:
        return None
    if len(q) > MAX_QUESTION_CHARS:
        return None
    if len(q) < MIN_QUESTION_CHARS:
        return None
    if len(q.split()) < MIN_QUESTION_WORDS:
        return None
    return q


def rag_answer_refuses_context(answer: str) -> bool:
    """
    True if the guide-grounded reply does not actually use the corpus (model bug:
    used_guides=True but answer is a refusal). Triggers web fallback.
    """
    t = answer.lower().strip()
    needles = (
        "don't know",
        "do not know",
        "i don't have",
        "not in the context",
        "not in the provided",
        "not enough information",
        "no information in",
        "guides don't",
        "guides do not",
        "don't cover",
        "doesn't cover",
        "does not cover",
        "not covered",
        "isn't in the context",
        "is not in the context",
    )
    return any(n in t for n in needles)


PENDING_FOOD_QUESTION_KEY = "pending_food_question"


def run_assistant_turn(question: str, rag_graph) -> None:
    """
    Append user + assistant messages only (no st.chat_message). Used before the history
    loop so the chat composer can stay at the bottom of the thread.
    """
    st.session_state.messages.append({"role": "user", "content": question})

    sources: list[str] = []
    sources_expander_title = "Sources used for this answer"
    answer = ""
    checklist_bytes: bytes | None = None
    checklist_name: str | None = None
    checklist_doc_src: list[str] = []
    usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="No model call (rule-based reply).",
    )

    if wants_word_checklist(question) and not is_food_shopping_topic(question):
        answer = (
            "I can only export downloadable checklists for food/drink shopping help. "
            "Ask me what to look for when choosing a food or drink item in the store."
        )
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "avatar": "🧑‍🍳",
                "sources": [],
            }
        )
        st.stop()

    use_rag, steer_reply = should_use_rag(question)
    if wants_word_checklist(question):
        use_rag = True
        steer_reply = ""

    if not use_rag:
        answer = steer_reply
    else:
        progress = st.progress(5, text="Starting...")
        result: dict = {}
        with get_openai_callback() as cb:
            for update in rag_graph.stream(
                {"question": question},
                stream_mode="updates",
            ):
                if "retrieve_node" in update:
                    progress.progress(50, text="Retrieved sources")
                    result.update(update["retrieve_node"])
                if "generate" in update:
                    progress.progress(90, text="Generating answer")
                    result.update(update["generate"])

            answer = result.get("answer", "Sorry, I could not generate an answer.")
            used_guides = result.get("used_guides", True)
            if used_guides and rag_answer_refuses_context(answer):
                used_guides = False

            usage = _usage_row(
                provider="openai",
                model="gpt-4o-mini",
                prompt_tokens=int(cb.prompt_tokens),
                completion_tokens=int(cb.completion_tokens),
                total_tokens=int(cb.total_tokens),
                cost_usd=float(cb.total_cost or 0.0),
                note="",
            )

            if used_guides:
                progress.progress(100, text="Done")
                docs = result.get("context", [])
                seen: set[str] = set()
                for doc in docs:
                    src = doc.metadata.get("source", "unknown")
                    if src not in seen:
                        seen.add(src)
                        sources.append(src)
            else:
                progress.progress(85, text="Searching the web...")
                ext_answer, web_urls, web_usage = _fallback_answer_with_usage(question)
                progress.progress(100, text="Done")
                answer = ext_answer
                sources = web_urls
                sources_expander_title = "Web sources"
                usage = _merge_usage(usage, web_usage)

            if wants_word_checklist(question):
                answer = tidy_chat_answer_for_word_export(answer)
                try:
                    checklist_bytes, checklist_name, checklist_doc_src = (
                        create_shopping_checklist_word_document(question)
                    )
                    answer = CHECKLIST_READY_SUMMARY
                except Exception as exc:
                    st.warning(f"Could not generate the Word checklist: {exc}")

    assistant_msg: dict = {
        "role": "assistant",
        "content": answer,
        "avatar": "🧑‍🍳",
        "sources": sources,
        "usage": usage,
    }
    if sources:
        assistant_msg["sources_expander_title"] = sources_expander_title
    if checklist_bytes is not None:
        assistant_msg["checklist_docx_bytes"] = checklist_bytes
        assistant_msg["checklist_file_name"] = checklist_name or "shopping-checklist.docx"
        assistant_msg["checklist_doc_sources"] = checklist_doc_src
    st.session_state.messages.append(assistant_msg)


# ---------------------------------------------------------------------------
# RAG bootstrap
# ---------------------------------------------------------------------------
@st.cache_resource
def bootstrap_rag():
    # Import-time indexing already happens in rag.index.
    return graph, len(all_splits)


rag_graph, _num_chunks = bootstrap_rag()

# ---------------------------------------------------------------------------
# UI: header & shortcuts
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="kyfg-main-title"><h1>🛒 Know Your Food Guide</h1></div>',
    unsafe_allow_html=True,
)
st.subheader("Food Shopping Q&A")
st.caption(
    "Ask questions about the food you want to buy and download food buying checklists."
)

col1, col2, col3 = st.columns(3)
if col1.button("🧀 How do I choose Parmigiano?"):
    st.session_state[PENDING_FOOD_QUESTION_KEY] = "How do I choose authentic Parmigiano?"
if col2.button("🍯 How can I tell if this honey is high quality?"):
    st.session_state[PENDING_FOOD_QUESTION_KEY] = "How can I tell if honey is high quality?"
if col3.button("🫒 What makes good olive oil?"):
    st.session_state[PENDING_FOOD_QUESTION_KEY] = "What should I check when buying olive oil?"
# ---------------------------------------------------------------------------
# Chat history
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Ask me anything about your foods you want to buy.",
            "avatar": "🧑‍🍳",
        },
    ]

if "unit_price_result" not in st.session_state:
    st.session_state.unit_price_result = ""
if "unit_price_usage" not in st.session_state:
    st.session_state.unit_price_usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="Local deterministic calculator; no model call.",
    )

if "barcode_lookup_result" not in st.session_state:
    st.session_state.barcode_lookup_result = ""
if "barcode_lookup_usage" not in st.session_state:
    st.session_state.barcode_lookup_usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="External API lookup only; no model call.",
    )

if "_barcode_input_key_suffix" not in st.session_state:
    st.session_state._barcode_input_key_suffix = 0

# Process shortcut / chat submissions before rendering so new turns are not drawn
# below the composer (inline mid-thread).
if PENDING_FOOD_QUESTION_KEY in st.session_state:
    raw_pending = st.session_state.pop(PENDING_FOOD_QUESTION_KEY)
    cleaned_pending = clean_question(raw_pending)
    if cleaned_pending is None:
        st.warning(
            f"Please enter a food-shopping question "
            f"({MIN_QUESTION_WORDS}+ words, {MIN_QUESTION_CHARS}+ characters, "
            f"at most {MAX_QUESTION_CHARS})."
        )
    else:
        run_assistant_turn(cleaned_pending, rag_graph)

with st.container(
    height=CHAT_HISTORY_SCROLL_HEIGHT_PX,
    border=True,
):
    for i, msg in enumerate(st.session_state.messages):
        with st.chat_message(msg["role"], avatar=msg.get("avatar")):
            st.markdown(msg["content"])
            has_checklist_download = (
                msg["role"] == "assistant" and msg.get("checklist_docx_bytes") is not None
            )
            if msg["role"] == "assistant" and msg.get("sources") and not has_checklist_download:
                expander_title = msg.get(
                    "sources_expander_title", "Sources used for this answer"
                )
                with st.expander(expander_title, expanded=False):
                    for j, src in enumerate(msg["sources"], start=1):
                        st.caption(f"[{j}] {src}")
            if has_checklist_download:
                st.download_button(
                    label="Download checklist as Word (.docx)",
                    data=msg["checklist_docx_bytes"],
                    file_name=msg.get("checklist_file_name", "shopping-checklist.docx"),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key=f"checklist-docx-msg-{i}",
                )
            if msg["role"] == "assistant" and msg.get("usage"):
                st.caption(_format_usage_caption(msg["usage"]))

# Chatbot-only conversation export
chat_export_json = _chat_json_bytes(st.session_state.messages)
chat_export_csv = _chat_csv_bytes(st.session_state.messages)
chat_export_pdf = _chat_pdf_bytes(st.session_state.messages)
st.caption("Export this chatbot conversation")
ex1, ex2, ex3 = st.columns(3)
with ex1:
    st.download_button(
        label="Download JSON",
        data=chat_export_json,
        file_name="chat-export.json",
        mime="application/json",
        key="chat_export_json_btn",
        use_container_width=True,
    )
with ex2:
    st.download_button(
        label="Download CSV",
        data=chat_export_csv,
        file_name="chat-export.csv",
        mime="text/csv",
        key="chat_export_csv_btn",
        use_container_width=True,
    )
with ex3:
    st.download_button(
        label="Download PDF",
        data=chat_export_pdf,
        file_name="chat-export.pdf",
        mime="application/pdf",
        key="chat_export_pdf_btn",
        use_container_width=True,
    )

# Inline composer at the end of Food Shopping Q&A (not Streamlit’s viewport-pinned bar),
# so barcode lookup and unit-price compare render below this section.
with st.container():
    if typed := st.chat_input("Ask a food question..."):
        st.session_state[PENDING_FOOD_QUESTION_KEY] = typed
        st.rerun()

# ---------------------------------------------------------------------------
# Barcode lookup (Open Food Facts UK)
# ---------------------------------------------------------------------------
st.subheader("Look Up By Barcode", anchor="barcode-lookup")
st.caption(
    "Enter the barcode from the food packaging to see product and nutrition information (digits only)."
)
_barcode_widget_key = f"barcode_field_{st.session_state._barcode_input_key_suffix}"
barcode_input = st.text_input(
    "Barcode number",
    placeholder="e.g. 5012345678900",
    key=_barcode_widget_key,
)
bc_look, bc_new = st.columns(2)
with bc_look:
    barcode_lookup_clicked = st.button(
        "Look up product", key="barcode_lookup_btn", use_container_width=True
    )
with bc_new:
    barcode_new_clicked = st.button(
        "New barcode", key="barcode_new_btn", use_container_width=True
    )

if barcode_new_clicked:
    st.session_state.barcode_lookup_result = ""
    st.session_state.barcode_lookup_usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="External API lookup only; no model call.",
    )
    st.session_state._barcode_input_key_suffix += 1
    st.rerun()

if barcode_lookup_clicked:
    digits = "".join(c for c in (barcode_input or "") if c.isdigit())
    if not digits:
        st.session_state.barcode_lookup_result = (
            "### Barcode lookup\n\nEnter a numeric barcode from the package."
        )
    else:
        try:
            st.session_state.barcode_lookup_result = lookup_product_by_barcode(digits)
        except Exception as exc:
            st.session_state.barcode_lookup_result = f"**Lookup failed:** {exc}"
    st.session_state.barcode_lookup_usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="External API lookup only; no model call.",
    )

if st.session_state.barcode_lookup_result:
    st.markdown(st.session_state.barcode_lookup_result)
    st.caption(_format_usage_caption(st.session_state.barcode_lookup_usage))

# ---------------------------------------------------------------------------
# Unit price comparison
# ---------------------------------------------------------------------------
st.subheader("Compare Unit Prices", anchor="compare-unit-prices")
st.caption("Enter price and amount for two food items to see which is better value. Enter two items using the same measure type (all g/kg or all ml/l).")
c1, c2 = st.columns(2, gap="small")
with c1:
    st.markdown("**Item A**")
    a_price = st.number_input("Price A", min_value=0.0, value=3.0, step=0.01, key="upa")
    a_qty = st.number_input("Amount A", min_value=0.01, value=50.0, step=0.1, key="uqa")
    a_unit = st.selectbox("Unit A", ["g", "kg", "ml", "l"], index=0, key="uua")
with c2:
    st.markdown("**Item B**")
    b_price = st.number_input("Price B", min_value=0.0, value=6.0, step=0.01, key="upb")
    b_qty = st.number_input("Amount B", min_value=0.01, value=80.0, step=0.1, key="uqb")
    b_unit = st.selectbox("Unit B", ["g", "kg", "ml", "l"], index=0, key="uub")
currency = st.text_input("Currency (display)", value="GBP", key="ucur")

if st.button("Compare", key="unit_price_compare_btn"):
    try:
        offers = [
            {
                "label": "Item A",
                "price": float(a_price),
                "currency": (currency or "").strip() or "GBP",
                "quantity": float(a_qty),
                "unit": a_unit,
            },
            {
                "label": "Item B",
                "price": float(b_price),
                "currency": (currency or "").strip() or "GBP",
                "quantity": float(b_qty),
                "unit": b_unit,
            },
        ]
        st.session_state.unit_price_result = compare_food_unit_prices(
            offers, currency=(currency or "").strip() or None
        )
    except Exception as exc:
        st.session_state.unit_price_result = f"**Could not compare:** {exc}"
    st.session_state.unit_price_usage = _usage_row(
        provider="none",
        model="no-model",
        prompt_tokens=0,
        completion_tokens=0,
        total_tokens=0,
        cost_usd=0.0,
        note="Local deterministic calculator; no model call.",
    )

if st.session_state.unit_price_result:
    st.markdown(st.session_state.unit_price_result)
    st.caption(_format_usage_caption(st.session_state.unit_price_usage))