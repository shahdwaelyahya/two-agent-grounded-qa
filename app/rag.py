from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.retriever import get_retriever


SYSTEM_PROMPT = """
You are a question-answering assistant for the book
"Rich Dad Poor Dad".

Use only the provided context to answer the question.

Do not invent information.
If the answer is not available in the context,
say that you could not find it in the book.
"""


def answer_question(question: str):
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

    return response.content, documents
