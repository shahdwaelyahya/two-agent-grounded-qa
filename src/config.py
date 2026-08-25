import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    qdrant_url: str
    qdrant_api_key: str
    qdrant_collection_name: str
    chat_model: str
    embedding_model: str
    retrieval_k: int
    retrieval_score_threshold: float


def _require_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}"
        )

    return value


def get_settings() -> Settings:
    return Settings(
        openai_api_key=_require_env("OPENAI_API_KEY"),
        qdrant_url=_require_env("QDRANT_URL"),
        qdrant_api_key=_require_env("QDRANT_API_KEY"),
        qdrant_collection_name=os.getenv(
            "QDRANT_COLLECTION_NAME",
            "langchain_qdrant_docs",
        ),
        chat_model=os.getenv(
            "CHAT_MODEL",
            "gpt-4o-mini",
        ),
        embedding_model=os.getenv(
            "EMBEDDING_MODEL",
            "text-embedding-3-small",
        ),
        retrieval_k=int(
            os.getenv("RETRIEVAL_K", "5")
        ),
        retrieval_score_threshold=float(
            os.getenv("RETRIEVAL_SCORE_THRESHOLD", "0.35")
        ),
    )
