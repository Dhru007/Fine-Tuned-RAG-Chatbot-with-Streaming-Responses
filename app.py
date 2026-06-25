import streamlit as st

from src.pipeline.rag_pipeline import stream_answer

st.set_page_config(
    page_title="RAG Chatbot",
    layout="wide"
)

st.title("Document RAG Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input(
    "Ask anything about the document"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        full_response = ""

        source_docs = []

        try:

            for token, docs in stream_answer(question):

                full_response += token

                placeholder.markdown(full_response)

                source_docs = docs

        except Exception as e:
            st.error(f"Unable to generate a response: {e}")

        st.markdown("---")

        st.subheader("Sources")

        for doc in source_docs:

            with st.expander(
                f"Page {doc.metadata.get('page')}"
            ):
                st.write(doc.page_content)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )
    
st.sidebar.info(
"""
Model: Mistral

Embedding:
BAAI/bge-base-en-v1.5

Retriever:
MMR

Vector DB:
Chroma
"""
)