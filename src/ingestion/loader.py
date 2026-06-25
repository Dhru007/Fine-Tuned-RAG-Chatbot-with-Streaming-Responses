from langchain_community.document_loaders import PyPDFLoader

def load_pdf(path):

    loader = PyPDFLoader(path)

    docs = loader.load()

    for i, doc in enumerate(docs):
        doc.metadata["page"] = i + 1

    return docs