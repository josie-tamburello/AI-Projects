from langchain_core.prompts import ChatPromptTemplate


template = """
You rewrite a shopper's question into search queries for a small food-buying guide.

The knowledge base has one short article per product topic (tomatoes, pasta, olives, etc.).
Generate exactly 4 alternative search queries — paraphrases of the SAME topic only.

Rules:
- Same food item or category as the user (only synonyms and rephrasing: e.g. tinned / canned / whole peeled tomatoes).
- Do NOT broaden to related ingredients, meals, cuisines, or "pantry" themes.
- Do NOT add new aspects (nutrition, recipes, brands, price) unless the user already asked.
- Each query: one line, under 16 words, plain text, no numbering or bullets.

User question:
{question}
""".strip()

prompt_perspectives = ChatPromptTemplate.from_template(template)

def parse_queries(text: str) -> list[str]:
    """Turn model output into a clean list of query strings."""
    return [line.strip("- ").strip() for line in text.splitlines() if line.strip()]


def generate_queries(question: str, llm) -> list[str]:
    """Call LLM to create alternative retrieval queries."""
    messages = prompt_perspectives.invoke({"question": question})
    response = llm.invoke(messages)
    queries = parse_queries(response.content)
    return queries or [question]