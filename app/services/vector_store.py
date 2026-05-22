import uuid
import chromadb
from app.services.embedder import embed_chunks, embed_query

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="pdf_chunks")


def store_chunks(chunks: list[str]) -> int:
    embeddings = embed_chunks(chunks)
    ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )
    return len(chunks)


def retrieve_relevant_chunks(query: str, top_k: int = 3) -> list[str]:
    query_embedding = embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]
