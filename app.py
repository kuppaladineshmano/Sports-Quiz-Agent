# Streamlit User Interface
import streamlit as st
from src.generator import compile_quiz_data

st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Powered Sports Quiz Generator")
st.markdown(
    """
Generate quizzes using:

✅ Historical Sports Facts (ChromaDB)

✅ Latest Sports News (Web Search)

🤖 Powered by Gemini
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    sport = st.selectbox(
        "🏅 Select Sport",
        ["Football", "Cricket", "Tennis", "Badminton"]
    )

with col2:
    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

st.divider()

if st.button("🚀 Generate Quiz", use_container_width=True):

    with st.spinner("Generating AI Quiz... Please wait..."):

        try:
            quiz = compile_quiz_data(sport, difficulty)

            st.success("✅ Quiz Generated Successfully!")

            st.markdown("---")
            st.markdown(quiz)

        except Exception as e:
            st.error("Something went wrong!")
            st.exception(e)

st.divider()

st.caption("Developed by Dinesh Mano using ChromaDB, DuckDuckGo Search and Google Gemini")