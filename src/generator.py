from src.database import query_chromadb
from src.search import get_live_news_context
from google import genai 
from dotenv import load_dotenv 
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


# Generate quiz using ChromaDB + Web Search + Gemini
def compile_quiz_data(sport,difficulty):
    db_context=query_chromadb(f"{sport} history")
    web_context=get_live_news_context(sport)
    prompt = f"""
You are an expert sports quiz generator.

I will provide two sources of information.

Historical Facts:
{db_context}

Latest Sports News:
{web_context}

Generate 10 multiple-choice questions.

Rules:

- Use ONLY the information provided.
- Do not use outside knowledge.
- Do not hallucinate.
- Difficulty level: {difficulty}
- Mix historical facts and latest news.
- Each question should teach the student something new.
- Each question must have exactly 4 options.
- Display every option on a NEW LINE.
- Leave one blank line after every question.
- After the quiz, provide the answer key.

Use this exact format:

Question 1:
Who hosted the first FIFA World Cup?

A) Brazil
B) Uruguay
C) England
D) Italy

Question 2:
...

Answer Key:
1. B
2. A
...
"""
    response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)
    return response.text

if __name__ =="__main__":
    compile_quiz_data("Football","Hard")