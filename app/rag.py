from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.retriever import get_retriever


def create_rag_chain():
    settings = get_settings()

    retriever = get_retriever()

    llm = ChatOpenAI(
        model=settings.chat_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )

    return retriever, llm
