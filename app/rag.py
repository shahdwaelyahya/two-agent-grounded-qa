from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.retriever import get_retriever


SYSTEM_PROMPT = """
You are a question-answering assistant for the book
"Rich Dad Poor Dad".

Use only the provided context to answer the question.

Rules:
1. Do not invent information.
2. If the answer cannot be found in the context, say:
   "I couldn't find the answer in the provided book context."
3. Give a clear and concise answer.
4. Explain the answer based on the retrieved context.
"""


def answer_question(question: str) -> str:
    settings = get_settings()

    retriever = get_retriever()

    llm = ChatOpenAI(
        model=settings.chat_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
