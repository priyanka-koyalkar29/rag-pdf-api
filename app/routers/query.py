from fastapi import APIRouter
from app.services.vector_store import retrieve_relevant_chunks
from app.services.llm import get_answer
from app.models.schemas import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_pdf(request: QueryRequest):
    chunks = retrieve_relevant_chunks(request.question, request.top_k)
    answer = get_answer(request.question, chunks)

    return QueryResponse(
        question=request.question,
        answer=answer,
        sources=chunks
    )
