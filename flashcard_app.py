# flashcard_app.py

# Written by Ovi
# Date: 2025-04-04
# Summary: Streamlit-based flashcard app with login, logout, multiple sets, pronunciation, hints, gamified stats, and persistent user tracking with resume support.

import streamlit as st
import pandas as pd
import random
import os
import datetime
import hashlib
import streamlit.components.v1 as components

# --------------------- CONFIG ---------------------
st.set_page_config(page_title="Bangla Flashcards", layout="centered")

# --------------------- USER SYSTEM ---------------------
users = {
    "ovi": hashlib.sha256("1234".encode()).hexdigest(),
    "guest": hashlib.sha256("guest".encode()).hexdigest()
}

def ensure_user_data_dir():
    os.makedirs("user_data", exist_ok=True)

def get_user_file(username):
    return f"user_data/{username}_history.csv"

def load_user_data(username):
    ensure_user_data_dir()
    file = get_user_file(username)
    if os.path.exists(file):
        return pd.read_csv(file).set_index("word").to_dict("index")
    return {}

def save_user_data(username, history):
    ensure_user_data_dir()
    file = get_user_file(username)

    if not history:
        return  # Don't save if there's no history

    df = pd.DataFrame.from_dict(history, orient="index")
    df.index.name = "word"
    df = df.reset_index()

    for col in ["correct", "mistake", "last_review"]:
        if col not in df.columns:
            df[col] = None

    df = df[["word", "correct", "mistake", "last_review"]]
    df.to_csv(file, index=False)

def logout():
    save_user_data(st.session_state["user"], st.session_state.history)
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --------------------- LOGIN ---------------------
def login():
    st.sidebar.header("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in users and hashlib.sha256(password.encode()).hexdigest() == users[username]:
            st.session_state["user"] = username
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.sidebar.error("Invalid credentials")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
    st.stop()

# --------------------- LOGGED IN STATE ---------------------
username = st.session_state["user"]
st.sidebar.success(f"👋 Logged in as `{username}`")
if st.sidebar.button("🚪 Logout"):
    logout()

# --------------------- FILE SELECTION ---------------------
st.title("📘 Bangla Vocabulary Flashcards")

os.makedirs("flashcards", exist_ok=True)
flashcard_files = [f for f in os.listdir("flashcards") if f.endswith(".xlsx")]
if not flashcard_files:
    st.warning("No flashcards found in 'flashcards/' directory.")
    st.stop()

selected_file = st.selectbox("📂 Choose a flashcard set", flashcard_files)
df = pd.read_excel(f"flashcards/{selected_file}")
required_columns = {'target_word', 'translation'}
if not required_columns.issubset(df.columns):
    st.error("❌ Missing required columns: 'target_word', 'translation'")
    st.stop()

df = df.dropna(subset=['target_word', 'translation']).reset_index(drop=True)

# --------------------- SESSION INIT ---------------------
defaults = {
    "review_index": 0, "correct": 0, "mistake": 0,
    "score": 0, "streak": 0, "order": [], "df": df
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# Load saved history
if "history" not in st.session_state:
    st.session_state.history = load_user_data(username)
    history = st.session_state.history
    st.session_state.correct = sum(v["correct"] for v in history.values())
    st.session_state.mistake = sum(v["mistake"] for v in history.values())
    st.session_state.score = st.session_state.correct * 10 - st.session_state.mistake * 5
    st.session_state.streak = 0

    reviewed_words = set(history.keys())
    remaining = [i for i, row in df.iterrows() if row['target_word'] not in reviewed_words]
    all_indices = remaining if remaining else list(range(len(df)))
    st.session_state.order = random.sample(all_indices, len(all_indices))
    st.session_state.review_index = 0

# --------------------- RESET REVIEW ---------------------
def reset_session():
    st.session_state.review_index = 0
    st.session_state.correct = 0
    st.session_state.mistake = 0
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.order = random.sample(range(len(df)), len(df))
    st.session_state.df = df
    st.session_state.history = {}

if st.sidebar.button("🔁 Start New Review"):
    reset_session()
    st.rerun()

if not st.session_state.order:
    reset_session()

# --------------------- SIDEBAR STATS ---------------------
reviewed = st.session_state.correct + st.session_state.mistake
accuracy = 100 * st.session_state.correct / reviewed if reviewed > 0 else 0

st.sidebar.markdown("### 📊 Stats")
st.sidebar.write(f"✅ Correct: {st.session_state.correct}")
st.sidebar.write(f"❌ Mistakes: {st.session_state.mistake}")
st.sidebar.write(f"🎯 Accuracy: {accuracy:.2f}%")
st.sidebar.write(f"🔥 Streak: {st.session_state.streak}")
st.sidebar.write(f"💎 Score: {st.session_state.score}")

# --------------------- END OF SESSION ---------------------
if st.session_state.review_index >= len(st.session_state.order):
    st.balloons()
    st.success("🎉 Review Completed!")
    if st.button("🔄 Restart"):
        reset_session()
        st.rerun()
    st.stop()

# --------------------- CURRENT CARD ---------------------
idx = st.session_state.order[st.session_state.review_index]
row = st.session_state.df.iloc[idx]
word = row['target_word']

st.subheader(f"🔤 Word: `{word}`")

# --------------------- PRONUNCIATION ---------------------
components.html(f"""
    <button onclick="speakWord()">🔊 Hear Pronunciation</button>
    <script>
    function speakWord() {{
      const msg = new SpeechSynthesisUtterance("{word}");
      window.speechSynthesis.speak(msg);
    }}
    </script>
""", height=50)

# --------------------- HINT TOGGLE ---------------------
show_hint = st.checkbox("💡 Show Hint", key=f"hint_{st.session_state.review_index}")
if show_hint:
    if pd.notna(row.get("part_of_speech")):
        st.markdown(f"🧩 Part of Speech: `{row['part_of_speech']}`")
    if pd.notna(row.get("level")):
        st.markdown(f"📶 Level: `{row['level']}`")
    if pd.notna(row.get("synonyms")):
        st.markdown(f"🔁 Synonyms: `{row['synonyms']}`")
    if pd.notna(row.get("antonyms")):
        st.markdown(f"↔️ Antonyms: `{row['antonyms']}`")
    if pd.notna(row.get("sample_sentence")):
        st.markdown(f"✒️ Sample: _{row['sample_sentence']}_")

# --------------------- TRANSLATION TOGGLE ---------------------
show_translation = st.checkbox("👁 Show Translation", key=f"trans_{st.session_state.review_index}")
if show_translation:
    st.markdown(f"💬 **Translation:** {row['translation']}")
    if pd.notna(row.get("bangla_meaning")):
        st.markdown(f"📝 **Bangla Meaning:** _{row['bangla_meaning']}_")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ I knew this"):
            st.session_state.correct += 1
            st.session_state.streak += 1
            st.session_state.score += 10
            st.session_state.history[word] = st.session_state.history.get(word, {
                "correct": 0, "mistake": 0, "last_review": None
            })
            st.session_state.history[word]["correct"] += 1
            st.session_state.history[word]["last_review"] = str(datetime.date.today())
            st.session_state.review_index += 1
            st.rerun()
    with col2:
        if st.button("❌ I didn't know"):
            st.session_state.mistake += 1
            st.session_state.streak = 0
            st.session_state.score = max(0, st.session_state.score - 5)
            st.session_state.history[word] = st.session_state.history.get(word, {
                "correct": 0, "mistake": 0, "last_review": None
            })
            st.session_state.history[word]["mistake"] += 1
            st.session_state.history[word]["last_review"] = str(datetime.date.today())
            st.session_state.review_index += 1
            st.rerun()
else:
    st.info("Click 👁 Show Translation to reveal answer and continue.")