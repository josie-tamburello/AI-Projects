import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

model_name = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-large")
embeddings = OpenAIEmbeddings(model=model_name)