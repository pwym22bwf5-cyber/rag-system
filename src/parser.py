import pdfplumber
from models import Chunk, Modality

def extract_chunks(pdf_path: str) -> list[Chunk]:
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                chunk = Chunk(
                    content=text.strip(),
                    modality=Modality.TEXT,
                    page=page_num + 1,
                    source=pdf_path,
                    chunk_id=f"chunk_{page_num + 1:03d}"
                )
                chunks.append(chunk)
    return chunks

if __name__ == "__main__":
    chunks = extract_chunks("data/test.pdf")
    for chunk in chunks:
        print(f"--- {chunk.chunk_id} | Page {chunk.page} ---")
        print(chunk.content[:200])
        print()