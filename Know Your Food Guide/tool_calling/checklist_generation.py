"""
Generate a Word (.docx) shopping checklist from the in-app guides when possible,
otherwise from web search constrained to supermarket food/drink selection tips.

Also exposes an OpenAI-style function tool schema for agent/tool-calling setups.

When the UI offers a .docx download, use ``tidy_chat_answer_for_word_export``
on the chat reply so the model is not contradicting that button (e.g. "create it manually").
"""

from __future__ import annotations

import io
import json
import re
from typing import Any

_IMPORT_ERROR: Exception | None = None
try:
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field
    from rag.llmfallback import openai_web_fallback_answer
    from rag.retrieve import retrieve, serialize_context
except Exception as err:  # pragma: no cover - only used in misconfigured envs
    ChatPromptTemplate = None  # type: ignore[assignment]
    ChatOpenAI = None  # type: ignore[assignment]
    BaseModel = object  # type: ignore[assignment]
    Field = None  # type: ignore[assignment]
    openai_web_fallback_answer = None  # type: ignore[assignment]
    retrieve = None  # type: ignore[assignment]
    serialize_context = None  # type: ignore[assignment]
    _IMPORT_ERROR = err

# ---------------------------------------------------------------------------
# OpenAI / Chat Completions tool schema
# ---------------------------------------------------------------------------

CHECKLIST_TOOL_OPENAI: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "create_shopping_checklist_word_document",
        "description": (
            "Create a downloadable Word document (.docx) with a practical checklist for choosing "
            "food or drink in a supermarket. Uses the app's buying guides when they apply; "
            "otherwise uses web search limited to in-store selection tips (labels, quality, packaging)—"
            "not recipes or unrelated topics."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": (
                        "What the shopper wants a checklist for (e.g. 'olive oil', 'eggs at the store', "
                        "or the user's full question)."
                    ),
                },
            },
            "required": ["topic"],
        },
    },
}


def wants_word_checklist(user_message: str) -> bool:
    """True if the user is asking for a Word document / downloadable checklist."""
    t = user_message.lower()
    patterns = (
        r"\bword\b",
        r"\bdocx\b",
        r"\.docx",
        r"\bdownload(able)?\b.*\b(checklist|document|doc)\b",
        r"\b(checklist|document|doc)\b.*\bdownload\b",
        r"\bmicrosoft word\b",
        r"\bms word\b",
    )
    return any(re.search(p, t) for p in patterns)


def tidy_chat_answer_for_word_export(answer: str) -> str:
    """
    Strip lines that wrongly tell the user to build a Word/checklist by hand when
    the app will show a download button for the same request.
    """
    if not answer or not answer.strip():
        return answer
    out_lines: list[str] = []
    for line in answer.splitlines():
        low = line.lower()
        if "manually" in low and any(
            w in low for w in ("checklist", "document", ".docx", "word", "download")
        ):
            continue
        if "create it yourself" in low or "create one yourself" in low:
            continue
        out_lines.append(line)
    cleaned = "\n".join(out_lines).strip()
    return cleaned if cleaned else answer


_FOOD_TERMS = (
    "food",
    "drink",
    "beverage",
    "fruit",
    "vegetable",
    "mushroom",
    "meat",
    "fish",
    "seafood",
    "dairy",
    "cheese",
    "milk",
    "yogurt",
    "egg",
    "honey",
    "olive oil",
    "oil",
    "vinegar",
    "pasta",
    "rice",
    "bread",
    "tomato",
    "olive",
    "bean",
    "lentil",
    "nut",
    "seed",
    "snack",
)

_SHOPPING_INTENT_TERMS = (
    "shop",
    "shopping",
    "supermarket",
    "grocery",
    "store",
    "buy",
    "choose",
    "select",
    "pick",
    "quality",
    "label",
    "look for",
    "what should i look for",
    "checklist",
    "download",
    "downloadable",
    "word",
    "docx",
)

_NON_FOOD_TERMS = (
    "tractor",
    "car part",
    "engine",
    "tyre",
    "tire",
    "battery",
    "phone",
    "laptop",
    "software",
    "real estate",
)


if _IMPORT_ERROR is None:
    class ChecklistExportDecision(BaseModel):
        allow_export: bool = Field(
            description=(
                "True only when the request is for choosing/comparing/checking quality of food or drink items while shopping."
            )
        )
        reason: str = Field(description="Short reason for the decision.")
else:
    class ChecklistExportDecision:  # pragma: no cover - only used in misconfigured envs
        pass


if _IMPORT_ERROR is None:
    _EXPORT_SCOPE_PROMPT = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Decide if a checklist export request is in scope for a food-shopping assistant.\n"
                "ALLOW only when the request is about choosing, comparing, or checking quality/labels of FOOD or DRINK items in a grocery/supermarket/store context.\n"
                "REJECT non-food topics (vehicles, tools, electronics, software, real estate, etc.), recipe-only requests, medical requests, and unrelated tasks.\n"
                "If food/drink is implied but clear enough (e.g. 'mozzarella checklist'), ALLOW.\n"
                "Return only structured output fields.",
            ),
            ("human", "User request:\n{text}\n"),
        ]
    )
else:
    _EXPORT_SCOPE_PROMPT = None

_export_scope_chain: Any = None


def _get_export_scope_chain():
    global _export_scope_chain
    if _export_scope_chain is None:
        _export_scope_chain = _get_llm().with_structured_output(ChecklistExportDecision)
    return _export_scope_chain


def is_food_shopping_topic(text: str) -> bool:
    """Semantic gate: allow only food/drink shopping checklist requests."""
    t = " ".join((text or "").strip().split())
    if not t:
        return False
    # Keep a lightweight deterministic deny-list as a first pass.
    if any(term in t.lower() for term in _NON_FOOD_TERMS):
        return False
    # If dependencies are unavailable, fail-open to avoid false rejections.
    if _IMPORT_ERROR is not None or _EXPORT_SCOPE_PROMPT is None:
        return True
    try:
        msg = _EXPORT_SCOPE_PROMPT.invoke({"text": t})
        parsed = _get_export_scope_chain().invoke(msg)
        return bool(getattr(parsed, "allow_export", False))
    except Exception:
        # Avoid blocking legitimate shoppers if classification hiccups.
        return True


# ---------------------------------------------------------------------------
# LLM: structure checklist from guide text or from web notes
# ---------------------------------------------------------------------------

if _IMPORT_ERROR is None:
    class GroundedChecklist(BaseModel):
        grounded_in_guides: bool = Field(
            description=(
                "True only if the excerpts clearly support the topic; then bullets must follow only those excerpts."
            )
        )
        title: str = Field(description="Short document title for the checklist.")
        bullets: list[str] = Field(
            default_factory=list,
            description="Actionable checklist lines; empty if not grounded.",
        )


    class RefinedWebChecklist(BaseModel):
        title: str
        bullets: list[str] = Field(
            default_factory=list,
            description="5–14 short supermarket selection tips; food/drink shopping only.",
        )
else:
    class GroundedChecklist:  # pragma: no cover - only used in misconfigured envs
        pass


    class RefinedWebChecklist:  # pragma: no cover - only used in misconfigured envs
        pass


# Lazy LLM / chains so importing this module always succeeds (Streamlit can import main).
_llm_singleton: Any = None
_struct_guides_chain: Any = None
_struct_web_chain: Any = None


def _get_llm() -> Any:
    if _IMPORT_ERROR is not None:
        raise RuntimeError(
            "Checklist generation dependencies failed to import. "
            f"Original error: {_IMPORT_ERROR}"
        ) from _IMPORT_ERROR
    global _llm_singleton
    if _llm_singleton is None:
        _llm_singleton = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=800)
    return _llm_singleton


def _get_struct_guides():
    global _struct_guides_chain
    if _struct_guides_chain is None:
        _struct_guides_chain = _get_llm().with_structured_output(GroundedChecklist)
    return _struct_guides_chain


def _get_struct_web():
    global _struct_web_chain
    if _struct_web_chain is None:
        _struct_web_chain = _get_llm().with_structured_output(RefinedWebChecklist)
    return _struct_web_chain


if _IMPORT_ERROR is None:
    _KB_PROMPT = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You turn buying-guide excerpts into a practical supermarket shopping checklist.\n"
                "Rules:\n"
                "- Each bullet is one clear, actionable tip for someone in a store.\n"
                "- Use ONLY information from the excerpts. Do not invent facts.\n"
                "- If excerpts are missing, off-topic, or too thin for the question, set "
                "grounded_in_guides to false and bullets to [].\n"
                "- Title should name the product or topic (not 'Checklist').",
            ),
            (
                "human",
                "Shopper request:\n{question}\n\nGuide excerpts:\n{context}\n",
            ),
        ]
    )

    _WEB_REFINE_PROMPT = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You extract a supermarket shopping checklist from web-sourced notes.\n"
                "Include only tips about choosing food or drink products in a shop "
                "(labels, packaging, freshness, quality cues, unit price, variants).\n"
                "Exclude recipes, meal plans, medical claims, and anything not about picking products in a store.\n"
                "Short bullets only; no URLs inside bullet text.",
            ),
            ("human", "Topic:\n{topic}\n\nNotes:\n{notes}\n"),
        ]
    )
else:
    _KB_PROMPT = None
    _WEB_REFINE_PROMPT = None


def _slug_filename(title: str, fallback: str) -> str:
    base = title.strip() or fallback
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower() or "shopping-checklist"
    return f"{slug[:80]}.docx"


def _topic_label(topic: str) -> str:
    cleaned = re.sub(r"\s+", " ", topic).strip()
    if not cleaned:
        return "Food or Drink"
    if len(cleaned) > 60:
        cleaned = cleaned[:60].rsplit(" ", 1)[0] or cleaned[:60]
    return cleaned[:1].upper() + cleaned[1:]


def _extract_food_subject(topic: str) -> str:
    """
    Pull the most likely food/drink subject from a user-style request.
    Example: "Create me a downloadable checklist for broad beans"
    -> "Broad beans".
    """
    t = " ".join(topic.lower().split())
    # Prefer explicit known food terms (longest first for multi-word matches).
    known_terms = sorted(set(_FOOD_TERMS), key=len, reverse=True)
    for term in known_terms:
        if term in t:
            return term[:1].upper() + term[1:]

    # Heuristic fallback: keep text after "for", strip common request words.
    m = re.search(r"\bfor\s+(.+)$", t)
    core = m.group(1) if m else t
    core = re.sub(
        r"\b(create|make|build|generate|give|me|a|an|the|download|downloadable|word|docx|checklist|tips)\b",
        " ",
        core,
    )
    core = re.sub(r"[^a-zA-Z0-9\s-]+", " ", core)
    core = re.sub(r"\s+", " ", core).strip(" -")
    return _topic_label(core or topic)


def _safe_checklist_title(candidate: str | None, topic: str) -> str:
    """
    Ensure document titles are shopper-facing and topic-based.
    Reject generic/class-like titles (e.g. 'RefinedWebChecklist').
    """
    raw = (candidate or "").strip()
    normalized = re.sub(r"[^a-zA-Z0-9]+", "", raw).lower()
    bad_titles = {
        "",
        "refinedwebchecklist",
        "groundedchecklist",
        "checklist",
        "shoppingchecklist",
        "wordchecklist",
        "docxchecklist",
    }
    if normalized in bad_titles:
        return f"{_extract_food_subject(topic)} Checklist"
    return raw


def _build_docx(
    title: str,
    bullets: list[str],
    intro: str,
    sources: list[str],
    source_heading: str = "Sources",
) -> bytes:
    try:
        from docx import Document
    except ModuleNotFoundError as err:
        raise ModuleNotFoundError(
            "Install python-docx to export Word files: pip install python-docx"
        ) from err

    doc = Document()
    doc.add_heading(title, 0)
    if intro.strip():
        doc.add_paragraph(intro.strip())
    for line in bullets:
        text = line.strip()
        if text:
            doc.add_paragraph(text, style="List Bullet")
    doc.add_heading(source_heading, level=2)
    for s in sources:
        if s.strip():
            doc.add_paragraph(s.strip(), style="List Bullet")
    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def _checklist_from_guides(question: str, context: str) -> GroundedChecklist:
    msg = _KB_PROMPT.invoke({"question": question, "context": context})
    return _get_struct_guides().invoke(msg)


def _checklist_from_web_notes(topic: str, notes: str) -> RefinedWebChecklist:
    msg = _WEB_REFINE_PROMPT.invoke({"topic": topic, "notes": notes})
    return _get_struct_web().invoke(msg)


def _unique_sources_from_docs(metadata_sources: list[str]) -> list[str]:
    out: list[str] = []
    for s in metadata_sources:
        if s and s not in out:
            out.append(s)
    return out


def create_shopping_checklist_word_document(topic: str) -> tuple[bytes, str, list[str]]:
    """
    Build a .docx checklist for *topic* (or the user's full question).

    Returns ``(file_bytes, suggested_filename, source_lines_for_ui)``.
    """
    topic = " ".join(topic.strip().split())
    if not topic:
        raise ValueError("topic must be non-empty")
    if not is_food_shopping_topic(topic):
        raise ValueError(
            "Word checklist export is limited to food/drink shopping tips. "
            "Try a request like: 'downloadable Word checklist for choosing mushrooms'."
        )

    state: dict = {"question": topic}
    retrieved = retrieve(state, _get_llm())
    docs = retrieved.get("context") or []
    context_text = serialize_context(docs) if docs else ""
    guide_sources = _unique_sources_from_docs(
        [str(d.metadata.get("source", "")) for d in docs]
    )

    spec = _checklist_from_guides(topic, context_text or "(no excerpts retrieved)")

    intro: str
    source_lines: list[str]
    source_heading: str

    if spec.grounded_in_guides and spec.bullets:
        title = _safe_checklist_title(spec.title, topic)
        intro = (
            "This checklist is based on the Know Your Food Guide buying guides in the app."
        )
        source_lines = guide_sources or ["In-app buying guides"]
        source_heading = "Sources (in-app guides)"
        doc_bytes = _build_docx(title, spec.bullets, intro, source_lines, source_heading)
        return doc_bytes, _slug_filename(title, topic), source_lines

    # Web path: strictly supermarket selection framing
    web_query = (
        f"{topic}\n\n"
        "Answer with practical points only about how to choose this food or drink when shopping "
        "in a supermarket (labels, packaging, freshness or quality cues, what to compare on the shelf). "
        "Do not include recipes, diets, or medical advice."
    )
    web_notes, urls = openai_web_fallback_answer(web_query, include_guides_disclaimer=False)
    refined = _checklist_from_web_notes(topic, web_notes)

    if not refined.bullets:
        raise RuntimeError(
            "Could not build a checklist from guides or web notes. Try a more specific food or drink topic."
        )

    intro = (
        "This checklist was generated from web sources because the in-app guides did not "
        "cover this topic well enough. Verify tips against current labels and local advice."
    )
    source_lines = urls if urls else ["Web search (OpenAI)"]
    source_heading = "Sources (web)"
    final_title = _safe_checklist_title(refined.title or spec.title, topic)
    doc_bytes = _build_docx(
        final_title,
        refined.bullets,
        intro,
        source_lines,
        source_heading,
    )
    return (
        doc_bytes,
        _slug_filename(final_title, topic),
        source_lines,
    )


def invoke_checklist_tool_call(arguments: str | dict) -> tuple[bytes, str, list[str]]:
    """
    Run the tool from a Chat Completions ``tool_calls[i].function.arguments`` value
    (JSON string or already-parsed dict).
    """
    if isinstance(arguments, str):
        payload = json.loads(arguments or "{}")
    else:
        payload = dict(arguments)
    topic = str(payload.get("topic", "")).strip()
    return create_shopping_checklist_word_document(topic)
