import streamlit as st
from youtube_fetch import search_youtube

st.title("AI Learning Resource Recommender")

topic = st.text_input("Enter a topic you want to learn")

if topic:

    st.write("Searching resources for:", topic)

    videos = search_youtube(topic)

    st.subheader("Top Learning Videos")

    for title, link in videos:
        st.write(f"[{title}]({link})")