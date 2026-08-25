from langchain_community.document_loaders import PyPDFLoader

from app.config import get_settings


def load_book():
    settings = get_settings()

    loader = PyPDFLoader(settings.book_url)

    documents = loader.load()

    return documents
