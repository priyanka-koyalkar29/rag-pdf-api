from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]


class IngestResponse(BaseModel):
    message: str
    chunks_stored: int
