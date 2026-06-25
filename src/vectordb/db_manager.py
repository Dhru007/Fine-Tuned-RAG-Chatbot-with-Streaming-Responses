from langchain_chroma import Chroma


def create_vector_store(chunks, embeddings, persist_directory="vectordb"):
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(persist_directory),
    )

    return db