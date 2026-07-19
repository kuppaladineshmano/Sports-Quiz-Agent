import streamlit as st
from src.generator import compile_quiz_data

if "quiz" not in st.session_state:
    st.session_state.quiz = None

st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Powered Sports Quiz Generator")

st.markdown("""
Generate quizzes using:

✅ Historical Sports Facts (ChromaDB)

✅ Latest Sports News (Web Search)

🤖 Powered by Gemini
""")

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

    with st.spinner("Generating AI Quiz..."):

        try:
            st.session_state.quiz = compile_quiz_data(sport, difficulty)
            st.success("✅ Quiz Generated Successfully!")

        except Exception as e:
            st.error("Something went wrong!")
            st.exception(e)

if st.session_state.quiz:

    st.header("📘 Generated Quiz")

    for i, question in enumerate(st.session_state.quiz, start=1):

        st.subheader(f"Question {i}")

        st.write(question["question"])

        st.radio(
            "Choose your answer:",
            question["options"],
            key=f"q{i}"
        )

        st.divider()

    if st.button("✅ Show Answers"):

        st.header("📖 Answer Key")

        for i, question in enumerate(st.session_state.quiz, start=1):

            st.success(f"Question {i}: {question['answer']}")

st.divider()

st.caption("Developed by Dinesh Mano using ChromaDB, DDGS and Google Gemini")