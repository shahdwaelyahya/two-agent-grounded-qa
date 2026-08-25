from app.retriever import get_retriever


def main():
    retriever = get_retriever()

    question = "What is the difference between the rich dad and poor dad?"

    documents = retriever.invoke(question)

    print(f"Retrieved {len(documents)} documents.\n")

    for i, document in enumerate(documents, start=1):
        print(f"--- Document {i} ---")
        print(document.page_content[:1000])
        print()


if __name__ == "__main__":
    main()
