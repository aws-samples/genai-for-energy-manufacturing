import boto3
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from pypdf import PdfReader

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

def summary_create(prompt_data) -> str:
    body = json.dumps({"prompt": prompt_data,
                       "max_tokens_to_sample": 8191,
                       "temperature": 0,
                       "top_k": 250,
                       "top_p": 0.999,
                       "stop_sequences": []
                       })
    modelId = 'anthropic.claude-instant-v1'
    accept = 'application/json'
    contentType = 'application/json'
    response = bedrock.invoke_model(body=body,
                                    modelId=modelId,
                                    accept=accept,
                                    contentType=contentType)
    response_body = json.loads(response.get('body').read())
    answer = response_body.get('completion')
    return answer

def Chunking_Summary(uploaded_file) -> str:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100,
    )

    texts = text_splitter.create_documents([text])
    summary = ""
    for index, chunk in enumerate(texts):
        chunk_content = chunk.page_content
        prompt = f"""\n\nHuman: Provide a detailed summary for the chunk of text provided to you:
        Text: {chunk_content}
        \n\nAssistant:"""
        summary += summary_create(prompt)
        print("I'm working on the summary")
        #print(f"\n\nNumber of tokens for Chunk {index + 1} with the prompt: {num_tokens_from_string(prompt)} tokens")
        #print("-------------------------------------------------------------------------------------------------------")
   
    final_summary_prompt = f"""\n\nHuman: You will be given a set of summaries from a document. Create a  
    summary from the provided individual summaries in detail.
    Summaries: {summary}
            \n\nAssistant:"""
    #print(f"Number of tokens for this Chunk with the final prompt: {"""num_tokens_from_string"""(final_summary_prompt)}")
    return summary_create(final_summary_prompt)
