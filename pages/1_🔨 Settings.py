import streamlit as st
import json

settings = {
    "model": st.selectbox("OpenAI Model", ["gpt-3.5-turbo", "gpt-4o"]),
    "top_k": st.slider("Number of similar documents to retrieve", min_value=1, max_value=5, value=1),
    "chunk_size": st.slider("Chunk size", min_value=500, max_value=4000, value=1500),
    "chunk_overlap": st.slider("Chunk overlap", min_value=0, max_value=200, value=50),
    "min_content_length": st.slider("Min content length of html tag", min_value=50, max_value=500, value=100),
    "max_depth": st.slider("Max crawling depth (more depth takes much longer time)", min_value=1, max_value=10, value=1)
}

if st.button("Save settings"):
    with open("settings.json", "w") as settings_file:
        json.dump(settings, settings_file)