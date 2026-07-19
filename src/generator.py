from src.database import query_chromadb
from src.search import get_live_news_context
from google import genai 
from dotenv import load_dotenv 
import os
import json

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


# Generate quiz using ChromaDB + Web Search + Gemini
def compile_quiz_data(sport,difficulty):
    db_context=query_chromadb(f"{sport} history")
    web_context=get_live_news_context(sport)
    prompt = f"""
You are an expert sports quiz generator.

Historical Facts:
{db_context}

Latest Sports News:
{web_context}

Generate exactly 10 multiple-choice questions.

Rules:

- Use ONLY the provided information.
- Do not use outside knowledge.
- Do not hallucinate.
- Difficulty: {difficulty}
- Mix historical facts and latest news.
- Each question should teach something new.

Return ONLY valid JSON.

Use this exact format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option B"
  }}
]

Do not return markdown.
Do not return explanations.
Do not wrap the JSON inside ```json.
Return ONLY the JSON array.
"""
    response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)
    quiz = json.loads(response.text)

    return quiz

if __name__ =="__main__":
    compile_quiz_data("Football","Hard")