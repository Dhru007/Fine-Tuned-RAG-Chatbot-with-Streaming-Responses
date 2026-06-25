def build_prompt(context, question):

    return f"""
You are a legal document assistant.

Rules:

1. Use only provided context.
2. Do not hallucinate.
3. If answer not found say:
   "Information not available in document."

Context:
{context}

Question:
{question}

Answer:
"""