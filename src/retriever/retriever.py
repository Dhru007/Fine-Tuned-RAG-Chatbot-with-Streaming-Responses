from langchain_chroma import Chroma
from src.config import CHROMA_PATH, TOP_K


def get_retriever(embedding):

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding
    )

    return db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": TOP_K,
            "fetch_k": 20
        }
    )