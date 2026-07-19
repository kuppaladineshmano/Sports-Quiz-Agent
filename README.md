# 🏆 AI Powered Sports Quiz Generator

## Project Overview

This project is an AI-powered Sports Quiz Generator built using Retrieval Augmented Generation (RAG).

The application retrieves historical sports facts from ChromaDB and combines them with the latest sports news from the web before generating quizzes using Google's Gemini AI.

---

## Features

- AI-powered quiz generation
- Historical sports facts using ChromaDB
- Latest sports news using DDGS
- Streamlit dashboard
- Difficulty selection
- Multiple sports support

---

## Tech Stack

- Python
- Streamlit
- ChromaDB
- Google Gemini API
- DuckDuckGo Search (DDGS)

---

## Project Structure

```
sports-quiz-agent/

│

├── app.py

├── data/

│ └── sports_facts.json

├── src/

│ ├── database.py

│ ├── search.py

│ └── generator.py

├── requirements.txt

└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## Workflow

1. User selects sport and difficulty.
2. Historical facts are retrieved from ChromaDB.
3. Latest sports news is retrieved using DDGS.
4. Gemini combines both contexts.
5. AI generates the quiz.
6. Quiz is displayed in Streamlit.

---

## Developed By

K. Dinesh Mano