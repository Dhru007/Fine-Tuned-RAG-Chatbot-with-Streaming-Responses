from langchain_ollama import ChatOllama
from src.config import MODEL_NAME, TEMPERATURE


def get_llm():
    try:
        return ChatOllama(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
        )
    except Exception:
        return ChatOllama(
            model="llama2:latest",
            temperature=TEMPERATURE,
        )