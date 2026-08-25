from app.rag import answer_question


def main():
    print("Rich Dad Poor Dad RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        try:
            answer, documents = answer_question(question)

            print(f"\nAssistant: {answer}\n")

            print("Sources:")

            seen_pages = set()

            for document in documents:
                page = document.metadata.get("page")

                if page not in seen_pages:
                    seen_pages.add(page)
                    print(f"- Page {page + 1}")

            print()

        except Exception as error:
            print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()
