"""
OpenAI web search when in-app buying guides do not cover the question.

Tries Responses API + ``web_search_preview``, then falls back to
``gpt-4o-mini-search-preview`` Chat Completions. Requires OPENAI_API_KEY.
Web search may incur extra charges per OpenAI pricing.
"""

from __future__ import annotations

import os
import re
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MAX_OUTPUT_TOKENS = 700

# Rough per-1M-token pricing (USD). Keep minimal; update as provider pricing changes.
_MODEL_PRICING_PER_1M: dict[str, tuple[float, float]] = {
    "gpt-4o-mini": (0.15, 0.60),  # input, output
    "gpt-4o-mini-search-preview": (0.15, 0.60),
}

HEADER = (
    "**This food buying guides don't include this topic.**\n\n"
    "Below is an answer from **OpenAI web search** (external sources—not from the know your food guide curated database). "
    "Check the links and use your own judgment.\n\n"
    "---\n\n"
)

def _unique(urls: list[str]) -> list[str]:
    out: list[str] = []
    for u in urls:
        if u and u not in out:
            out.append(u)
    return out


def _urls_from_markdown(text: str) -> list[str]:
    return _unique(re.findall(r"https?://[^\s\)\]\>\"']+", text or ""))


def _parse_responses_output(resp: Any) -> tuple[str, list[str]]:
    text_parts: list[str] = []
    urls: list[str] = []
    output = getattr(resp, "output", None) or []
    for item in output:
        if getattr(item, "type", None) != "message":
            continue
        for block in getattr(item, "content", None) or []:
            t = getattr(block, "text", None)
            if t:
                text_parts.append(t)
            for ann in getattr(block, "annotations", None) or []:
                if getattr(ann, "type", None) == "url_citation":
                    u = getattr(ann, "url", None)
                    if u:
                        urls.append(u)
    text = "\n".join(text_parts).strip()
    return text, _unique(urls)


def _estimate_cost_usd(model: str, input_tokens: int, output_tokens: int) -> float | None:
    pricing = _MODEL_PRICING_PER_1M.get(model)
    if pricing is None:
        return None
    in_per_m, out_per_m = pricing
    return (input_tokens / 1_000_000.0) * in_per_m + (output_tokens / 1_000_000.0) * out_per_m


def _extract_usage_dict(resp: Any) -> dict[str, int]:
    usage = getattr(resp, "usage", None) or {}
    if not isinstance(usage, dict):
        # Newer SDK objects expose attributes.
        prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
        completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
        total_tokens = int(getattr(usage, "total_tokens", 0) or 0)
        return {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens or (prompt_tokens + completion_tokens),
        }
    prompt_tokens = int(usage.get("prompt_tokens", 0) or 0)
    completion_tokens = int(usage.get("completion_tokens", 0) or 0)
    total_tokens = int(usage.get("total_tokens", 0) or 0)
    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens or (prompt_tokens + completion_tokens),
    }


def _responses_web_search(
    client: OpenAI, user_question: str
) -> tuple[str | None, list[str], dict[str, int], str]:
    model = os.getenv("OPENAI_WEB_SEARCH_MODEL", "gpt-4o-mini")
    instruction = (
        "You help someone shopping for food or drink in a store. "
        "Search the web and give a short, practical answer. "
        "Prefer reputable sources (government health sites, food-safety agencies, "
        "established consumer organisations). "
        "Use markdown links to sources you found in search."
    )
    try:
        resp = client.responses.create(
            model=model,
            tools=[{"type": "web_search_preview"}],
            input=f"{instruction}\n\nShopper question:\n{user_question}",
            max_output_tokens=MAX_OUTPUT_TOKENS,
        )
    except Exception:
        return None, [], {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}, model

    text, urls = _parse_responses_output(resp)
    if not text:
        return None, [], _extract_usage_dict(resp), model
    if not urls:
        urls = _urls_from_markdown(text)
    return text, urls, _extract_usage_dict(resp), model


def _chat_search_preview(
    client: OpenAI, user_question: str
) -> tuple[str, list[str], dict[str, int], str]:
    model = os.getenv("OPENAI_CHAT_SEARCH_MODEL", "gpt-4o-mini-search-preview")
    instruction = (
        "You help someone shopping for food or drink in a store. "
        "Use web search, then give a short practical answer with markdown links to sources you used."
    )
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_question},
            ],
            max_tokens=MAX_OUTPUT_TOKENS,
        )
    except Exception:
        return "", [], {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}, model

    text = (r.choices[0].message.content or "").strip()
    return text, _urls_from_markdown(text), _extract_usage_dict(r), model


def openai_web_fallback_answer_detailed(
    user_question: str,
    *,
    include_guides_disclaimer: bool = True,
) -> tuple[str, list[str], dict[str, Any]]:
    """
    Return (markdown, source URLs, usage metadata).
    """
    usage_meta: dict[str, Any] = {
        "provider": "openai",
        "model": None,
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0.0,
        "note": "",
    }
    if not os.getenv("OPENAI_API_KEY"):
        usage_meta["note"] = "OPENAI_API_KEY missing; web fallback disabled."
        return (
            "**Your guides don't cover this topic.** "
            "Set `OPENAI_API_KEY` to enable OpenAI web search.",
            [],
            usage_meta,
        )

    client = OpenAI()
    text, urls, usage, model = _responses_web_search(client, user_question)
    usage_meta.update(usage)
    usage_meta["model"] = model

    if text is None or not text.strip():
        text, urls, usage2, model2 = _chat_search_preview(client, user_question)
        usage_meta["prompt_tokens"] = int(usage_meta["prompt_tokens"]) + int(
            usage2.get("prompt_tokens", 0)
        )
        usage_meta["completion_tokens"] = int(usage_meta["completion_tokens"]) + int(
            usage2.get("completion_tokens", 0)
        )
        usage_meta["total_tokens"] = int(usage_meta["total_tokens"]) + int(
            usage2.get("total_tokens", 0)
        )
        usage_meta["model"] = model2

    est = _estimate_cost_usd(
        str(usage_meta.get("model") or ""),
        int(usage_meta.get("prompt_tokens", 0)),
        int(usage_meta.get("completion_tokens", 0)),
    )
    usage_meta["cost_usd"] = float(est or 0.0)
    if est is None:
        usage_meta["note"] = "Cost estimate unavailable for current fallback model."

    if not text:
        return (
            "**Your guides don't cover this topic.** "
            "Web search did not return an answer—try rephrasing your question.",
            [],
            usage_meta,
        )

    if include_guides_disclaimer:
        return HEADER + text, urls, usage_meta
    return text, urls, usage_meta


def openai_web_fallback_answer(
    user_question: str,
    *,
    include_guides_disclaimer: bool = True,
) -> tuple[str, list[str]]:
    """
    Return (markdown for the user, source URLs for the UI).

    If web search is unavailable or fails, returns a short message and no URLs.

    Set ``include_guides_disclaimer=False`` when the text is only used as hidden
    context, so the "guides don't include" header is omitted.
    """
    text, urls, _usage = openai_web_fallback_answer_detailed(
        user_question, include_guides_disclaimer=include_guides_disclaimer
    )
    return text, urls
