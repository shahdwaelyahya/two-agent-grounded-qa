from app.loader import load_book
from app.splitter import split_documents
from app.vectorstore import create_vectorstore


def main():
    print("Loading book...")

    documents = load_book()

    print(f"Loaded {len(documents)} pages.")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings and uploading to Qdrant...")

    create_vectorstore(chunks)

    print("Done! Book is now stored in Qdrant.")


if __name__ == "__main__":
    main()
