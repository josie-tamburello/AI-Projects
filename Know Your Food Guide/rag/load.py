from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

data_dir = Path(__file__).parent / "data"

loader = DirectoryLoader(
    path=str(data_dir),
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
    show_progress=True,
)

docs = loader.load()