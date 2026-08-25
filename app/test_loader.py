from app.loader import load_book


documents = load_book()

print(f"Loaded {len(documents)} pages.")

for document in documents[:2]:
    print(document.metadata)
    print(document.page_content[:500])
    print("-" * 50)
