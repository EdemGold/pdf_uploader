import streamlit as st
import pandas as pd
from pathlib import Path

st.title("PDF Viewer App")

pdfs = {}

# Allow multiple uploads with a while loop
uploaded = True
while uploaded:
    uploaded_file = st.file_uploader("Choose a PDF", type=['pdf'])
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
        pdfs[uploaded_file.name] = uploaded_file.read()

    else:
        uploaded = False

# Display all uploaded PDFs
for name, data in pdfs.items():
    st.write(name)
    if st.checkbox(f'Show {name}'):
        st.write(data)