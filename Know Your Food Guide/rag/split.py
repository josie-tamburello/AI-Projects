from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_docs(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        add_start_index=True,
    )
    all_splits = text_splitter.split_documents(docs)
    print(f"Split source docs into {len(all_splits)} chunks.")
    return all_splits


