import streamlit as st
import os
from pathlib import Path
from rfp_main import Chunking_Summary

st.title(f"""Analyzing RFP Documents Using Amazon Bedrock""")

with st.container():

    st.header('Upload')
    File = st.file_uploader('Upload a file', type=["pdf"], key="new")
    if File is not None:
        # determine the path to temporarily save the PDF file that was uploaded
        save_folder = os.path.join("../../data/analyzing-rfp")
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        # create a posix path of save_folder and the file name
        save_path = Path(save_folder, File.name)
        try:
            with open(save_path, mode='wb') as w:
                w.write(File.getvalue())
        except IOError as e:
            print("Failed to open file", e)
        # once the save path exists...
        if save_path.exists():
            st.success(f'File {File.name} is successfully saved!')
            st.write(Chunking_Summary(save_path))
            os.remove(save_path)
