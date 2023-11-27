import streamlit as st
from pathlib import Path  
from PyPDF2 import PdfFileWriter, PdfFileReader
import uuid

st.title("PDF Viewer App")

pdfs = {}

# Allow multiple uploads 
uploaded = True  

while uploaded:

    key = str(uuid.uuid4())  
    uploaded_file = st.file_uploader("Choose PDF", type=['pdf'], key=key)

    if uploaded_file is not None:

        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}  
        pdfs[uploaded_file.name] = uploaded_file.read()

        # Save to temp file
        with open(Path("temp.pdf"), "wb") as f: 
            f.write(uploaded_file.getbuffer())

        # Read PDF
        pdf_reader = PdfFileReader(Path("temp.pdf"))

        # Display pages
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            st.write(page)

    else:
        uploaded = False  

# List uploaded PDFs
for name in pdfs:
    st.write(name)
