from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class InitialiseVectorstoreConfig:
    documents_directory: Path
    index_name: str


@dataclass(frozen=True)
class RAGConfig:
    index_name: str