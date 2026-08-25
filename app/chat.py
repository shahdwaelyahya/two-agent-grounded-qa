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
            answer = answer_question(question)

            print(f"\nAssistant: {answer}\n")

        except Exception as error:
            print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
