from src.embeddings.embedder import get_embedding_model
from src.retriever.retriever import get_retriever
from src.llm.models import get_llm
from src.prompts.prompt_templaate import build_prompt

embedding = get_embedding_model()

retriever = get_retriever(embedding)

llm = get_llm()


def retrieve_context(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context, docs


def stream_answer(question):

    context, docs = retrieve_context(question)

    prompt = build_prompt(
        context,
        question
    )

    for chunk in llm.stream(prompt):

        if hasattr(chunk, "content"):
            yield chunk.content, docs