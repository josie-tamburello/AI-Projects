from typing import List, TypedDict

from langchain_core.documents import Document

from .vectorstore import vector_store
from .querytranslation import generate_queries


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: State, llm) -> dict:
    """Retrieve relevant chunks using multi-query expansion + deduplication."""
    question = state["question"].strip()

    queries = generate_queries(question, llm)
    if question not in queries:
        queries = [question, *queries]

    all_docs: List[Document] = []
    for q in queries:
        all_docs.extend(vector_store.similarity_search(q, k=4))

    seen = set()
    unique_docs: List[Document] = []
    for doc in all_docs:
        key = (doc.metadata.get("source"), doc.page_content[:200])
        if key not in seen:
            seen.add(key)
            unique_docs.append(doc)

    return {"context": unique_docs[:8]}


def serialize_context(docs: List[Document]) -> str:
    """Format retrieved docs into prompt-ready context text."""
    return "\n\n".join(
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in docs
    )