import streamlit as st

st.title("AI Learning Resource Recommender")

topic = st.text_input("Enter a topic you want to learn")

if topic:
    st.write("Searching resources for:", topic)

    st.write("Top Learning Resources:")
    st.write("1. Example Video 1")
    st.write("2. Example Video 2")
    st.write("3. Example Article")