#!/usr/bin/python

'''
/**
 * Author:    Mohammed Saifullah
 * Created:   11.05.2022
 * 
 * (c) Copyright by Fishbone Solutions
 **/
'''
import streamlit as st
from pathlib import Path
from pypdf import PdfWriter


file_dispatch_worker = []
st.header(' FISH DOCX 🪝🐟')
ptest = "archive/"
uploaded_files = st.file_uploader(
    "Choose a File", accept_multiple_files=True, type=['pdf'])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    Path(ptest).mkdir(parents=True, exist_ok=True)
    f = open(ptest + str(uploaded_file.name), "wb")
    f.write(bytes_data)
    f.close()
    file_dispatch_worker.append(ptest+uploaded_file.name)
merger = PdfWriter()
for pdf in file_dispatch_worker:
    merger.append(pdf)

merger.write("archive/merged-pdf.pdf")
merger.close()
with open("archive/merged-pdf.pdf", "rb") as file:
    btn = st.download_button(
        label="Generate PDF",
        data=file,
        file_name="dowloaded.pdf",
        mime="application/octet-stream"
    )
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
