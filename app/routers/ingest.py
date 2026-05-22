from fastapi import APIRouter, UploadFile, File
from app.services.pdf_parser import extract_text_from_pdf, chunk_text
from app.services.vector_store import store_chunks
from app.models.schemas import IngestResponse

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
async def ingest_pdf(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = extract_text_from_pdf(file_bytes)
    chunks = chunk_text(text)
    chunks_stored = store_chunks(chunks)

    return IngestResponse(
        message="PDF ingested successfully",
        chunks_stored=chunks_stored
    )
