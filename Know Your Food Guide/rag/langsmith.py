import os
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("LANGSMITH_TRACING", "true")
os.environ.setdefault("LANGSMITH_PROJECT", "know-your-food-guide")

if not os.getenv("LANGSMITH_API_KEY"):
    raise ValueError("LANGSMITH_API_KEY is missing. Add it to your .env file.")