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

import base64

# Set page configuration
st.set_page_config(layout="wide")  # Set wide layout to utilize the full screen

# Function to load image and encode it to base64
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load and encode the train image
encoded_image = load_image("image.png")

# Custom CSS to animate the image
st.markdown(
    f"""
    <style>
    @keyframes slideIn {{
        0% {{
            transform: translateX(-100%);
        }}
        100% {{
            transform: translateX(100%);
        }}
    }}
    .header-img {{
        animation: slideIn 20s linear infinite;
        width: 100%;
        height: auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add the animated image to the header
st.markdown(
    f"""
    <div style="position: relative; width: 100%; overflow: hidden;">
        <img src="data:image/png;base64,{encoded_image}" class="header-img" alt="Header Image">
    </div>
    """,
    unsafe_allow_html=True
)

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
