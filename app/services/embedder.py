from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings.tolist()


def embed_query(query: str) -> list[float]:
    embedding = model.encode(query)
    return embedding.tolist()
