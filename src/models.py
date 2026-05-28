from dataclasses import dataclass
from enum import Enum

class Modality(Enum):
    TEXT = "text"
    TABLE = "table"
    CHART = "chart"

@dataclass
class Chunk:
    content: str
    modality: Modality
    page: int
    source: str
    chunk_id: str