# flashcard_app.py

# Written by Ovi
# Date: 2025-04-04
# Summary: A comprehensive Streamlit-based flashcard app for Bangla vocabulary with hints, stats, and review tracking.

import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Bangla Flashcards", layout="centered")
st.title("📘 Bangla Vocabulary Flashcards")

# Upload Excel
uploaded_file = st.file_uploader("📤 Upload your Excel file", type=["xlsx", "xls"])
required_columns = {'target_word', 'translation'}

# Initialize session state
if 'review_index' not in st.session_state:
    st.session_state.review_index = 0
if 'order' not in st.session_state:
    st.session_state.order = []
if 'correct' not in st.session_state:
    st.session_state.correct = 0
if 'mistake' not in st.session_state:
    st.session_state.mistake = 0
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

# Reset session
def reset_session():
    st.session_state.review_index = 0
    st.session_state.correct = 0
    st.session_state.mistake = 0
    st.session_state.order = []
    st.session_state.df = pd.DataFrame()

# Main logic
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    if required_columns.issubset(df.columns):
        df = df.dropna(subset=['target_word', 'translation']).reset_index(drop=True)

        if st.session_state.df.empty:
            st.session_state.df = df
            st.session_state.order = random.sample(range(len(df)), len(df))

        total_cards = len(st.session_state.df)

        # Sidebar stats
        st.sidebar.markdown("### 📊 Your Stats")
        st.sidebar.write(f"✅ Known: {st.session_state.correct}")
        st.sidebar.write(f"❌ Mistakes: {st.session_state.mistake}")
        reviewed = st.session_state.correct + st.session_state.mistake
        st.sidebar.write(f"🧠 Reviewed: {reviewed}/{total_cards}")
        if reviewed > 0:
            accuracy = 100 * st.session_state.correct / reviewed
            st.sidebar.write(f"🎯 Accuracy: {accuracy:.2f}%")

        # Current card
        idx = st.session_state.order[st.session_state.review_index]
        row = st.session_state.df.iloc[idx]

        st.subheader(f"🔤 Word: `{row['target_word']}`")

        # Hint toggle
        show_hint = st.toggle("💡 Show Hint", value=False)
        if show_hint:
            if 'part_of_speech' in row and pd.notna(row['part_of_speech']):
                st.markdown(f"🧩 *Part of Speech:* `{row['part_of_speech']}`")
            if 'sample_sentence' in row and pd.notna(row['sample_sentence']):
                st.markdown(f"✒️ *Sample:* _{row['sample_sentence']}_")

        # Translation toggle
        show_translation = st.toggle("👁 Show Translation", value=False)
        if show_translation:
            st.markdown(f"💬 **Translation:** {row['translation']}")
            if 'bangla_meaning' in row and pd.notna(row['bangla_meaning']):
                st.markdown(f"📝 **Bangla Meaning:** _{row['bangla_meaning']}_")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ I knew this"):
                    st.session_state.correct += 1
                    st.session_state.review_index += 1
            with col2:
                if st.button("❌ I didn't know"):
                    st.session_state.mistake += 1
                    st.session_state.review_index += 1
        else:
            st.info("Click '👁 Show Translation' to reveal meaning and continue.")

        # End of review
        if st.session_state.review_index >= len(st.session_state.df):
            st.balloons()
            st.success("🎉 Review completed!")
            st.markdown(f"""
            - ✅ Known: `{st.session_state.correct}`
            - ❌ Mistakes: `{st.session_state.mistake}`
            - 🎯 Accuracy: `{100 * st.session_state.correct / (st.session_state.correct + st.session_state.mistake):.2f}%`
            """)
            if st.button("🔁 Restart Review"):
                reset_session()
    else:
        st.error("❌ Required columns not found. Please include 'target_word' and 'translation'.")
else:
    st.info("📂 Please upload a vocabulary Excel file to begin.")