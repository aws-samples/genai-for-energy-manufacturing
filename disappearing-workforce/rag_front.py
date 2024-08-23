import streamlit as st #all streamlit commands will be available through the "st" alias
import rag_back as rb #reference to local lib script

st.set_page_config(page_title="Disappearing-Workforce-KB")
st.title("Disappearing-Workforce")

selected_model = st.selectbox("Choose a model", [rb.model_id[0] for rb.model_id in rb.claude_model_ids])

query = st.text_area("Ask a question")

run_button = st.button("Run")

if run_button:
    # Find the selected model ARN
    model_arn = next((model_id[1] for model_id in rb.claude_model_ids if model_id[0] == selected_model), None)
    if model_arn:
        response = rb.ask_bedrock_llm_with_knowledge_base(query, model_arn, rb.kb_id)
        generated_text = response['output']['text']
        
     # Display the response
        st.text_area("Response", generated_text, height=200)
    else:
        st.error("Invalid model selected.")