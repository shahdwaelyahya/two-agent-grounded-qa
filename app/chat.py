from app.rag import create_rag_chain


def main():
    retriever, llm = create_rag_chain()

    question = input("Ask a question about the book: ")

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a helpful assistant answering questions about
Rich Dad Poor Dad.

Answer the user's question using only the provided context.

If the answer is not found in the context, say:
"I couldn't find the answer in the book."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)


if __name__ == "__main__":
    main()
