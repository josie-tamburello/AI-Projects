from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

_router_llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=200, temperature=0)

_router_prompt = ChatPromptTemplate.from_template(
    """You are a gate for "Know Your Food Guide": help shoppers choose food in a store using short buying guides.

Decide if the user is asking something that should use those guides.

Use RAG when they want help choosing, comparing, or judging FOOD or DRINK to buy (ingredients, labels, quality, what to pick in the shop). Vague but on-topic counts (e.g. "something for a salad", "is this tin any good").

ALWAYS use RAG when they ask for a checklist, Word document, .docx, or downloadable guide **as long as the topic is what to look for when buying food or drink** (e.g. "Word checklist for honey", "docx for choosing eggs"). The format request does not make it SKIP.

Use SKIP for: greetings, thanks, jokes, chit-chat, homework, code, politics, medical advice, or anything not about shopping for food/drink in a store.

Reply with EXACTLY two lines and nothing else:
Line 1: RAG or SKIP (uppercase, one word)
Line 2: If SKIP, one short friendly sentence steering them to ask a food-shopping question. If RAG, write NONE

User message:
{message}
"""
)

def should_use_rag(user_message: str) -> tuple[bool, str]:
    default_skip = (
        "I only help with food shopping—what to look for when you buy ingredients. "
        "Ask me about a food or drink you're choosing in the shop."
    )
    msg = _router_prompt.invoke({"message": user_message})
    raw = _router_llm.invoke(msg).content.strip()
    lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    if not lines:
        return True, ""

    first = lines[0].upper().split()[0] if lines[0].upper().split() else ""
    if first == "RAG":
        return True, ""
    if first == "SKIP":
        second = lines[1] if len(lines) > 1 else default_skip
        if not second or second.upper() == "NONE":
            second = default_skip
        return False, second

    return True, ""