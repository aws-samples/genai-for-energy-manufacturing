import os
from pathlib import Path
import streamlit as st
import shr_lib as shrlib  # reference to local lib script

fms = ['Bedrock Titan', 'Bedrock Claude 3 Sonnet', 'Bedrock Claude 2', 'Bedrock Claude Instant', 'Bedrock Llama 3', 'Bedrock Mistral Large']
default_model = fms.index('Bedrock Claude 3 Sonnet')

default_values = {
    "img_summary": None,
    "new_contents": None,
    "label_text": None,
    "document": None,
    "document_summary": None,
    "page_model": None,
    "chat_history": None
}


def initialize_session_state():
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value


def configure_page():
    st.set_page_config(
        page_title="Shift Handover Report Chatbot",
        page_icon="eyeglasses"
    )


def add_header():
    st.title("Shift Handover Report Analyzer")
    st.markdown("# :orange[Analyze] your daily operational report")
    st.markdown("Integrating GenAI into your shift handover report process can significantly enhance the clarity, comprehensiveness, and efficiency of information transfer between shifts. By summarizing equipment health, work activity, photos, voice memos, and ERP changes, this application ensures that critical information is effectively communicated during shift changes at industrial facilities.")
    st.markdown("----")
    st.markdown("### :orange[How to use]:")
    st.markdown(
        "1. Select a Bedrock FM from the dropdown menu on the sidebar")
    st.markdown("2. Upload your daily operational report (PDF, JPEG, PNG, MP3, WAV, M4A).")
    st.markdown("3. Wait for the summary to be auto-generated")
    st.markdown("4. Chat with your document.")


def configure_sidebar():
    with st.sidebar:
        st.markdown(
            "Generative AI can be used to analyze daily operational reports and provide contextually accurate answers.")
        return st.selectbox('Select a Bedrock FM', options=fms, index=default_model)


def select_document():
    c1, c2 = st.columns([0.7, 0.3])

    c1.subheader("# :orange[Summarize] your operational reports")
    uploaded_file = c1.file_uploader("Upload a document", type=[
                                     'pdf', 'jpg', 'png', 'jpeg', 'mp3', 'wav', 'm4a'], on_change=None, key="uploader")

    if uploaded_file is not None:
        # determine the path to temporarily save the PDF file that was uploaded
        save_folder = os.path.join("../../data/shift-handover-report")
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        # create a posix path of save_folder and the file name
        save_path = Path(save_folder, uploaded_file.name)
        if st.session_state['document'] == uploaded_file.name:            
            return st.session_state['document']
        else:
            try:
                with open(save_path, mode='wb') as w:
                    w.write(uploaded_file.getvalue())
            except IOError as e:
                print("Failed to open file", e)
            # once the save path exists...
            if save_path.exists():
                st.toast(f'File {uploaded_file.name} is successfully uploaded!', icon='😍')

            return uploaded_file.name if uploaded_file else None


def process_file(document, model):
    if document is None or st.session_state['document_summary']:
        return

    st.session_state["document"] = document
    file_type = document.split('.')[-1]

    with st.spinner(f'File {document} uploaded successfully and starting summarization...'):

        new_contents, document_summary = get_summary(
            file_type, os.path.abspath("../../data/shift-handover-report/" + document), model)
        if document_summary != None:
            st.session_state['document_summary'] = document_summary[-1]['content'][0]['text']
            st.session_state['chat_history'] = document_summary
        new_contents = new_contents.replace("$", "\$")

        st.session_state['new_contents'] = new_contents
        st.toast('Summary Generation Completed', icon='😍')


def get_summary(file_type, file_name, model):

    new_contents = ''
    if file_type == 'pdf':
        new_contents += shrlib.read_pdf(file_name, model)
        messages = [{"role": "user", "content": [
            {"text": 'Create a summary of the document in English in not more than 1000 words. The document content has been split into extracted texts and extracted descriptions from images.'}, {"text": new_contents}]}]
    elif file_type in ['png', 'jpg', 'jpeg']:
        with open(file_name, 'rb') as f:
            contents = f.read()
            new_contents = shrlib.detect_labels(contents)
            st.session_state['label_text'] = new_contents

            messages = [{"role": "user", "content": [
                {"text": 'As a truthful summarizer, explain in not more than 1000 words in English, the labels generated from images in an operational shift handover report: '}, {"text": new_contents}]}]

    elif file_type in ['mp3', 'wav', 'm4a']:
        st.success('Converting file to wav format')
        file_name = shrlib.convert_audio_format(file_name)
        st.success('Conversion completed.')
        
        st.success('Transcription Started. This might take a while')
        result = shrlib.extract_text_from_audio(file_name)
        

        messages = [{"role": "user", "content": [
            {"text": 'As a truthful summarizer, explain in not more than 1000 words in English, the content of the audio file: '}, {"text": result["text"]}]}]

    return new_contents, shrlib.call_bedrock(model, messages)


def display_summary(model):
    st.markdown('**Report Summary:** \n')
    st.write(str(st.session_state['document_summary']).replace("$", "\$"))


def display_prompt_data():
    st.markdown("---")
    st.subheader("**Analyze operational report**\n")
    return st.text_input('**What insights would you like?**', key='text')


def process_report(model):
    if selected_document is None:
        return


    if st.session_state['document_summary'] and len(st.session_state['document_summary']) > 0:
        display_summary(selected_model)
        return display_prompt_data()


def get_answers(input_text, model):

    if input_text is not None and input_text != '' and st.session_state['chat_history']:
        result = shrlib.get_answers(
            st.session_state['chat_history'], input_text, model)
        st.write(result[-1]['content'][0]['text'])


initialize_session_state()
configure_page()
add_header()
st.markdown("---")

selected_model = configure_sidebar().lower()

if st.session_state['page_model'] is None or st.session_state['page_model'] != selected_model:
    previous_document = st.session_state['document']
    st.session_state = {}
    initialize_session_state()
    st.session_state['document'] = previous_document
    st.session_state['page_model'] = selected_model
    
selected_document = select_document()

process_file(selected_document, selected_model)

input_text = process_report(selected_model)

get_answers(input_text, selected_model)

