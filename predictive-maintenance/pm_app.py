import streamlit as st 
from pm_lib import *

##
st.set_page_config(page_title="Generative AI for Synthetic Image Generation", page_icon="cloud_with_lightning")
st.title(':orange[Generative AI] for Synthetic Image Generation')


## image paths
static_pipeline_path = '../../data/predictive-maintenance/static-pipeline.jpeg'

st.write('Static image')
st.image(static_pipeline_path)

col1, col2, col3 = st.columns(3)

prompt = st.text_input('Defect Prompt', 'light rust on surface area on pipeline, weathered, damaged, old')
submit = st.button('Generate Variations')
if submit:
    generate_image(static_pipeline_path, prompt)
    with col1:
        st.write('Generated image 1')
        st.image('output-1.png')
    with col2:
        st.write('Generated image 2')
        st.image('output-2.png')
    with col3:
        st.write('Generated image 3')
        st.image('output-3.png')
        