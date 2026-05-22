from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_answer(question: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer the question based only on the context provided. If the answer is not in the context, say 'I don't know based on the provided document.'"
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ],
        max_tokens=300,
        temperature=0.3
    )

    return response.choices[0].message.content
