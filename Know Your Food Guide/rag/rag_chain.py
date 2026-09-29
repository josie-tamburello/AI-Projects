from typing import List, TypedDict

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from pydantic import BaseModel, Field

from .retrieve import retrieve, serialize_context
from .prompts.rag_prompt import prompt


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    used_guides: bool


class GuidedAnswer(BaseModel):
    used_guides: bool = Field(
        description=(
            "True ONLY if you give a substantive answer using facts from the Context. "
            "MUST be False if you say you don't know, the guides don't cover the topic, "
            "the context doesn't contain the answer, or you only refuse or redirect. "
            "Never set True together with a refusal or 'I don't know' style answer."
        )
    )
    answer: str = Field(description="Reply to the shopper in plain language.")


llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=500)
structured_llm = llm.with_structured_output(GuidedAnswer)


def retrieve_node(state: State) -> dict:
    return retrieve(state, llm)


def generate(state: State) -> dict:
    context_text = serialize_context(state["context"])
    messages = prompt.invoke(
        {
            "question": state["question"],
            "context": context_text,
        }
    )
    parsed = structured_llm.invoke(messages)
    return {"answer": parsed.answer, "used_guides": parsed.used_guides}


graph_builder = StateGraph(State).add_sequence([retrieve_node, generate])
graph_builder.add_edge(START, "retrieve_node")
graph = graph_builder.compile()
