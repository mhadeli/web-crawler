import os
import json
import streamlit as st
import shutil

parent_dir = os.path.abspath(os.path.join(os.getcwd()))

files = os.listdir(parent_dir)
json_files = [f for f in files if f.endswith(".json") and f != "settings.json"]
faiss_dirs = [d for d in files if os.path.isdir(os.path.join(parent_dir, d)) and d.endswith(".faiss")]

json_contents = []

for json_file in json_files:
    file_path = os.path.join(parent_dir, json_file)
    with open(file_path, 'r') as f:
        data = json.load(f)
        json_contents.append(data)

st.title("JSON Data Viewer")
for idx, content in enumerate(json_contents):
    st.subheader(f"Contents of {json_files[idx]}")
    st.json(content)

    if st.sidebar.button(f"Delete {json_files[idx]}"):
        try:
            os.remove(os.path.join(parent_dir, json_files[idx]))
            st.success(f"Deleted {json_files[idx]}")
        except (PermissionError, FileNotFoundError):
            st.error(f"Error deleting {json_files[idx]}")
        st.rerun()

for faiss_dir in faiss_dirs:
    if st.sidebar.button(f"Delete {faiss_dir}"):
        try:
            dir_to_delete = os.path.join(parent_dir, faiss_dir)
            if os.path.exists(dir_to_delete):
                shutil.rmtree(dir_to_delete, ignore_errors=True)
                st.success(f"Deleted {faiss_dir}")
        except (PermissionError, FileNotFoundError, OSError):
            st.error(f"Error deleting {faiss_dir}")
        st.rerun()

if st.sidebar.button("Refresh"):
    st.rerun()