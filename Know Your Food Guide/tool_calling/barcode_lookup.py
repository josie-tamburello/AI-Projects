"""
Look up packaged food products by barcode via the Open Food Facts API (UK instance).

Exposes an OpenAI-style function tool schema plus helpers for agents or Streamlit.

API base: https://uk.openfoodfacts.org/ — see Open Food Facts developer docs for terms of use.
"""

from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------------
# Open Food Facts (UK) — product by barcode
# ---------------------------------------------------------------------------

OFF_UK_API_BASE = "https://uk.openfoodfacts.org/api/v2/product"
# Descriptive User-Agent is required/recommended by Open Food Facts for API access.
OFF_USER_AGENT = "KnowYourFoodGuide/0.1 (https://github.com/openfoodfacts; educational app)"

# ---------------------------------------------------------------------------
# OpenAI / Chat Completions tool schema
# ---------------------------------------------------------------------------

BARCODE_LOOKUP_TOOL_OPENAI: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "lookup_product_by_barcode",
        "description": (
            "Look up a packaged food or drink product by its barcode (EAN-13, UPC, etc.) "
            "using the Open Food Facts database (UK). Returns name, brand, pack size, "
            "ingredients summary, Nutri-Score / NOVA when available, and allergens."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "barcode": {
                    "type": "string",
                    "description": (
                        "Numeric barcode from the package (often 8, 12, or 13 digits). "
                        "Strip spaces; leading zeros are significant."
                    ),
                },
            },
            "required": ["barcode"],
        },
    },
}


def _normalize_barcode(raw: str) -> str:
    s = "".join(ch for ch in raw.strip() if ch.isdigit())
    if not s or len(s) > 14:
        raise ValueError("Enter a valid numeric barcode (typically 8–13 digits).")
    return s


def fetch_open_food_facts_product(barcode: str, timeout_s: float = 15.0) -> dict[str, Any]:
    """
    GET product JSON from the UK Open Food Facts API.
    Returns the parsed top-level object (includes status, product, code).
    """
    code = _normalize_barcode(barcode)
    url = f"{OFF_UK_API_BASE}/{quote(code, safe='')}"
    req = Request(
        url,
        headers={
            "User-Agent": OFF_USER_AGENT,
            "Accept": "application/json",
        },
        method="GET",
    )
    try:
        with urlopen(req, timeout=timeout_s) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except HTTPError as e:
        raise RuntimeError(f"Open Food Facts HTTP error ({e.code}).") from e
    except URLError as e:
        raise RuntimeError(f"Could not reach Open Food Facts: {e.reason!r}.") from e

    try:
        return json.loads(body)
    except json.JSONDecodeError as e:
        raise RuntimeError("Invalid JSON from Open Food Facts.") from e


def _first_str(*values: object) -> str | None:
    for v in values:
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def _nutriscore_letter(product: dict[str, Any]) -> str | None:
    for key in (
        "nutrition_grade_fr",
        "nutrition_grades",
        "nutriscore_grade",
    ):
        val = product.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip().upper()[:1]
    return None


def _nova_group(product: dict[str, Any]) -> str | None:
    ng = product.get("nova_group")
    if ng is None:
        return None
    if isinstance(ng, int) and 1 <= ng <= 4:
        return str(ng)
    if isinstance(ng, str) and ng.strip().isdigit():
        return ng.strip()
    return None


def _energy_kcal_100g(product: dict[str, Any]) -> str | None:
    nut = product.get("nutriments")
    if not isinstance(nut, dict):
        return None
    for k in ("energy-kcal_100g", "energy_kcal_100g"):
        v = nut.get(k)
        if v is not None and str(v).strip():
            try:
                return f"{float(v):.0f}"
            except (TypeError, ValueError):
                return str(v).strip()
    return None


def summarize_open_food_facts_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Structured summary for programmatic use."""
    status = int(payload.get("status") or 0)
    code = str(payload.get("code") or "").strip()
    if status != 1:
        verbose = str(payload.get("status_verbose") or "product not found")
        return {
            "found": False,
            "barcode": code or None,
            "message": verbose,
        }

    p = payload.get("product")
    if not isinstance(p, dict):
        return {"found": False, "barcode": code or None, "message": "Malformed product data."}

    name = _first_str(
        p.get("product_name"),
        p.get("product_name_en"),
        p.get("generic_name"),
        p.get("generic_name_en"),
    )
    brands = _first_str(p.get("brands"))
    qty = _first_str(p.get("quantity"))
    ing = _first_str(p.get("ingredients_text"), p.get("ingredients_text_en"))
    allergens = _first_str(p.get("allergens"))
    traces = _first_str(p.get("traces"))
    labels = _first_str(p.get("labels"))

    url = f"https://uk.openfoodfacts.org/product/{code}" if code else None

    return {
        "found": True,
        "barcode": code or None,
        "name": name,
        "brands": brands,
        "quantity": qty,
        "nutriscore": _nutriscore_letter(p),
        "nova_group": _nova_group(p),
        "energy_kcal_per_100g": _energy_kcal_100g(p),
        "ingredients_text": ing,
        "ingredients_excerpt": (ing[:500] + "…") if ing and len(ing) > 500 else ing,
        "allergens": allergens,
        "traces": traces,
        "labels": labels,
        "open_food_facts_url": url,
    }


def format_barcode_lookup_markdown(summary: dict[str, Any]) -> str:
    """Turn summarize_open_food_facts_payload output into markdown for chat/UI."""
    if not summary.get("found"):
        msg = summary.get("message") or "Product not found."
        bc = summary.get("barcode")
        head = f"Barcode `{bc}`" if bc else "That barcode"
        return f"### Barcode lookup\n\n{head}: **{msg}** (Open Food Facts UK).\n"

    lines = [
        "### Barcode lookup (Open Food Facts UK)",
        "",
    ]
    name = summary.get("name") or "Unknown product"
    lines.append(f"**{name}**")
    if summary.get("brands"):
        lines.append(f"- **Brand:** {summary['brands']}")
    if summary.get("quantity"):
        lines.append(f"- **Pack / quantity:** {summary['quantity']}")
    if summary.get("barcode"):
        lines.append(f"- **Barcode:** `{summary['barcode']}`")

    meta: list[str] = []
    if summary.get("nutriscore"):
        meta.append(f"Nutri-Score **{summary['nutriscore']}**")
    if summary.get("nova_group"):
        meta.append(f"NOVA **{summary['nova_group']}**")
    if summary.get("energy_kcal_per_100g"):
        meta.append(f"~**{summary['energy_kcal_per_100g']}** kcal / 100 g")
    if meta:
        lines.append("- " + "; ".join(meta))

    if summary.get("labels"):
        lines.append(f"- **Labels:** {summary['labels']}")

    ing = summary.get("ingredients_excerpt") or summary.get("ingredients_text")
    if ing:
        lines += ["", "**Ingredients (excerpt)**", "", ing]

    if summary.get("allergens"):
        lines += ["", f"**Allergens:** {summary['allergens']}"]
    if summary.get("traces"):
        lines.append(f"**May contain traces:** {summary['traces']}")

    if summary.get("open_food_facts_url"):
        lines += ["", f"[View on Open Food Facts]({summary['open_food_facts_url']})"]

    lines += [
        "",
        "_Data is crowd-sourced; always check the real package._",
    ]
    return "\n".join(lines)


def lookup_product_by_barcode(barcode: str, *, timeout_s: float = 15.0) -> str:
    """
    Fetch product by barcode and return a markdown summary for tool / UI output.
    """
    payload = fetch_open_food_facts_product(barcode, timeout_s=timeout_s)
    summary = summarize_open_food_facts_payload(payload)
    return format_barcode_lookup_markdown(summary)


def invoke_barcode_lookup_tool_call(arguments: str | dict) -> str:
    """Parse OpenAI tool arguments and run the lookup."""
    if isinstance(arguments, str):
        payload = json.loads(arguments or "{}")
    else:
        payload = dict(arguments)
    bc = payload.get("barcode")
    if not isinstance(bc, str) or not bc.strip():
        raise ValueError("Missing or invalid 'barcode'.")
    return lookup_product_by_barcode(bc)
