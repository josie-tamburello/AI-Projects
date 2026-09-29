from .load import docs
from .split import split_docs
from .vectorstore import vector_store

all_splits = split_docs(docs)
document_ids = vector_store.add_documents(documents=all_splits)
print(document_ids[:3])