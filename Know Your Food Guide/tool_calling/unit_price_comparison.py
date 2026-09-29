"""
Compare food/drink offers by normalizing price per gram or per millilitre.

Exposes an OpenAI-style function tool schema plus pure Python helpers for agents or Streamlit.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

# ---------------------------------------------------------------------------
# OpenAI / Chat Completions tool schema
# ---------------------------------------------------------------------------

UNIT_PRICE_TOOL_OPENAI: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "compare_food_unit_prices",
        "description": (
            "Compare which food or drink offer is better value by converting each price to "
            "cost per gram (g/kg) or per millilitre (ml/l). Use the same kind of measure for "
            "all offers (all mass or all volume—do not mix g with ml in one call)."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "offers": {
                    "type": "array",
                    "description": "Two or more priced packs to compare.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "label": {
                                "type": "string",
                                "description": "Short name, e.g. 'Brand A' or '50g pack'.",
                            },
                            "price": {
                                "type": "number",
                                "description": "Total shelf price for that pack (e.g. 3.0 for £3).",
                            },
                            "currency": {
                                "type": "string",
                                "description": "ISO-style code for display only, e.g. GBP, EUR, USD.",
                            },
                            "quantity": {
                                "type": "number",
                                "description": "Net weight or volume of the pack (e.g. 50 for 50g).",
                            },
                            "unit": {
                                "type": "string",
                                "enum": ["g", "kg", "ml", "l"],
                                "description": "Unit for quantity.",
                            },
                        },
                        "required": ["price", "quantity", "unit"],
                    },
                    "minItems": 2,
                },
                "currency": {
                    "type": "string",
                    "description": "Default currency for display if an offer omits it.",
                },
            },
            "required": ["offers"],
        },
    },
}


def _d(x: float | int | str | Decimal) -> Decimal:
    return Decimal(str(x))


def _normalize_quantity(quantity: float | int | Decimal, unit: str) -> tuple[Decimal, str]:
    """Return (amount_in_base, base_unit) where base is 'g' for mass or 'ml' for volume."""
    u = unit.strip().lower()
    q = _d(quantity)
    if q <= 0:
        raise ValueError("quantity must be positive")

    if u == "g":
        return q, "g"
    if u == "kg":
        return q * _d("1000"), "g"
    if u == "ml":
        return q, "ml"
    if u == "l":
        return q * _d("1000"), "ml"
    raise ValueError(f"Unsupported unit: {unit!r}. Use g, kg, ml, or l.")


def compare_food_unit_prices(
    offers: list[dict[str, Any]],
    *,
    currency: str | None = None,
) -> str:
    """
    Markdown summary: best value per g or per ml, table of all offers sorted by unit price.
    """
    if len(offers) < 2:
        raise ValueError("Provide at least two offers to compare.")

    parsed: list[dict[str, Any]] = []
    base_kind: str | None = None

    for i, raw in enumerate(offers):
        if not isinstance(raw, dict):
            raise ValueError(f"Offer {i} must be an object/dict.")
        if raw.get("price") is None or raw.get("quantity") is None or raw.get("unit") is None:
            raise ValueError(f"Offer {i} needs price, quantity, and unit.")

        p = _d(raw["price"])
        if p < 0:
            raise ValueError("price cannot be negative.")

        amount_base, base_unit = _normalize_quantity(raw["quantity"], str(raw["unit"]))
        if base_kind is None:
            base_kind = base_unit
        elif base_unit != base_kind:
            raise ValueError(
                "All offers must use the same measure type (all g/kg or all ml/l), not mixed."
            )

        label = str(raw.get("label") or f"Option {i + 1}")
        curr = str(raw.get("currency") or currency or "").strip() or "—"
        price_per = (p / amount_base).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)

        parsed.append(
            {
                "label": label,
                "pack_price": p,
                "price_per_base": price_per,
                "currency": curr,
                "base_unit": base_unit,
                "quantity": _d(raw["quantity"]),
                "unit_display": str(raw["unit"]).strip().lower(),
            }
        )

    parsed.sort(key=lambda r: r["price_per_base"])
    best = parsed[0]
    unit_label = "100 g" if best["base_unit"] == "g" else "100 ml"
    scale = _d("100")
    per_100 = (best["price_per_base"] * scale).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    lines = [
        "### Unit price comparison",
        "",
        f"**Best value:** **{best['label']}** — about **{best['currency']} {per_100:.2f}** per {unit_label} "
        f"(pack total **{best['currency']} {best['pack_price']:.2f}**).",
        "",
        "| Option | Pack price | Size | Price per " + unit_label + " |",
        "| --- | ---:| ---:| ---:|",
    ]
    for r in parsed:
        ppb = (r["price_per_base"] * scale).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        lines.append(
            f"| {r['label']} | {r['currency']} {r['pack_price']:.2f} | "
            f"{r['quantity']} {r['unit_display']} | {r['currency']} {ppb:.2f} |"
        )

    lines += [
        "",
        "_Lower price per "
        + unit_label.lower()
        + " means better shelf value (same product type assumed)._",
    ]
    return "\n".join(lines)


def invoke_unit_price_tool_call(arguments: str | dict) -> str:
    if isinstance(arguments, str):
        payload = json.loads(arguments or "{}")
    else:
        payload = dict(arguments)
    offers = payload.get("offers")
    if not isinstance(offers, list):
        raise ValueError("Missing or invalid 'offers' array.")
    curr = payload.get("currency")
    return compare_food_unit_prices(
        offers,
        currency=curr if isinstance(curr, str) else None,
    )