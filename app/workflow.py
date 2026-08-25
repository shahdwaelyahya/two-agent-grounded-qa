from app.researcher import research_question
from app.reviewer import review_answer


def run_qa_workflow(question: str):
    research_result = research_question(question)

    review_result = review_answer(
        question=research_result["question"],
        draft_answer=research_result["draft_answer"],
        documents=research_result["documents"],
    )

    sources = []

    for document in research_result["documents"]:
        page = document.metadata.get("page")

        if page is not None:
            page_number = page + 1

            if page_number not in sources:
                sources.append(page_number)

    return {
        "question": question,
        "draft_answer": research_result["draft_answer"],
        "review": review_result,
        "sources": sources,
    }
