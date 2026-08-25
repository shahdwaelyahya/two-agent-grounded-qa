from langchain_openai import ChatOpenAI

from app.config import get_settings


REVIEWER_PROMPT = """
You are the Reviewer Agent for a grounded Q&A assistant.

Your job is to review the Researcher's draft answer against
the retrieved source passages.

Check:
1. Is the answer supported by the provided context?
2. Did the researcher add unsupported information?
3. Is the answer relevant to the question?
4. Is it clear and concise?

Return:
VERDICT: PASS or FAIL

If PASS:
Return the corrected final answer.

If FAIL:
Explain briefly what is unsupported and provide a corrected answer
using only the source context.
"""


def review_answer(
    question: str,
    draft_answer: str,
    documents: list,
):
    settings = get_settings()

    llm = ChatOpenAI(
        model=settings.chat_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
{REVIEWER_PROMPT}

Question:
{question}

Researcher Draft:
{draft_answer}

Source Context:
{context}
"""

    response = llm.invoke(prompt)

    return response.content
