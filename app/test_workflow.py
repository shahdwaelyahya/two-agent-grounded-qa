from app.workflow import run_qa_workflow


def main():
    question = input("Ask a question: ")

    result = run_qa_workflow(question)

    print("\n=== RESEARCHER DRAFT ===")
    print(result["draft_answer"])

    print("\n=== REVIEWER ===")
    print(result["review"])

    print("\n=== SOURCES ===")
    for page in result["sources"]:
        print(f"Page {page}")


if __name__ == "__main__":
    main()
