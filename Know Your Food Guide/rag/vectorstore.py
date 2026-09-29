from langchain_core.vectorstores import InMemoryVectorStore
from .embed import embeddings

vector_store = InMemoryVectorStore(embeddings)