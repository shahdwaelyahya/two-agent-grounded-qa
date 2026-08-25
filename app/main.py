from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import answer_question


app = FastAPI(
    title="Rich Dad Poor Dad RAG API",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str
    sources: list[int]


@app.get("/")
def root():
    return {
        "message": "Rich Dad Poor Dad RAG API is running"
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    answer, documents = answer_question(request.question)

    sources = []

    for document in documents:
        page = document.metadata.get("page")

        if page is not None:
            page_number = page + 1

            if page_number not in sources:
                sources.append(page_number)

    return {
        "answer": answer,
        "sources": sources,
    }
