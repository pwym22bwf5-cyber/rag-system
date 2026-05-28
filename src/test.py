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

# Test it
if __name__ == "__main__":
    chunk = Chunk(
        content="Revenue increased by 12% in Q3 2024.",
        modality=Modality.TEXT,
        page=4,
        source="annual_report_2024.pdf",
        chunk_id="chunk_001"
    )
    print(chunk)
    print(f"Source: {chunk.source}")
    print(f"Type: {chunk.modality.value}")