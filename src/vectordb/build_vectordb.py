from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.ingestion.loader import load_pdf
from src.ingestion.chunker import create_chunks
from src.embeddings.embedder import get_embedding_model
from src.vectordb.db_manager import create_vector_store


def build_vector_db(data_path=None, persist_directory=None):
    data_path = Path(data_path or PROJECT_ROOT / "data" / "AI_Training_Document.pdf")
    persist_directory = Path(persist_directory or PROJECT_ROOT / "vectordb")

    docs = load_pdf(str(data_path))
    chunks = create_chunks(docs)
    embedding = get_embedding_model()
    create_vector_store(chunks, embedding, persist_directory=str(persist_directory))
    return persist_directory


if __name__ == "__main__":
    build_vector_db()
    print("Vector DB Created")