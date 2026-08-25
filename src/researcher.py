from langchain_openai import ChatOpenAI

from app.config import get_settings
from app.retriever import get_retriever


RESEARCHER_PROMPT = """
You are the Researcher Agent for a grounded Q&A assistant about
the book "Rich Dad Poor Dad".

Your job is to:
1. Search the provided retrieved context.
2. Identify the passages that answer the user's question.
3. Draft an answer using ONLY the retrieved context.
4. Never invent facts that are not supported by the context.

Return:
- A concise draft answer.
- The source passages used.
"""


def research_question(question: str):
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
{RESEARCHER_PROMPT}

User Question:
{question}

Retrieved Context:
{context}
"""

    response = llm.invoke(prompt)

    return {
        "question": question,
        "draft_answer": response.content,
        "documents": documents,
    }
