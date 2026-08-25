from pathlib import Path

import requests
from langchain_community.document_loaders import PyPDFLoader

from app.config import get_settings


BOOK_PATH = Path("data/rich_dad_poor_dad.pdf")


def download_book() -> Path:
    settings = get_settings()

    BOOK_PATH.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(settings.book_url, timeout=60)
    response.raise_for_status()

    BOOK_PATH.write_bytes(response.content)

    return BOOK_PATH


def load_book():
    book_path = download_book()

    loader = PyPDFLoader(str(book_path))
    documents = loader.load()

    return documents
