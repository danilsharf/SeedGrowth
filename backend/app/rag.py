from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_rag_answer(question: str, entries: list[str]):

    context = "\n".join(entries)

    prompt = f"""
    You are an assistant helping summarize a user's journal.

    Use the context below to answer the question.

    If relevant information exists in the context,
    summarize it.

    Only say "Information is missing"
    if the context truly contains no relevant information.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text