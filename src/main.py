from models import Chunk, Modality

chunk = Chunk(
    content="Revenue increased by 12% in Q3 2024.",
    modality=Modality.TABLE,
    page=4,
    source="annual_report_2024.pdf",
    chunk_id="chunk_001"
)

print(chunk)