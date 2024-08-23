
# Disappearing Workforce

# Lab introduction

Final product:

![disappearing workforce final](/static/disappearing-workforce/streamlit.png)

In this lab, we will build a Retrieval Augmented Generation (RAG) Framework with [Amazon Bedrock](https://aws.amazon.com/bedrock/) Knowledge Bases and Streamlit. We will use Amazon Bedrock's Knowledge Bases to serve as an index where we can grab a corpus of information old containing emails and public sourced Energy companies' operations data. Depite this being a relatively simple example, it showcases how to integrate Generative AI Foundation models with information indexes from a location and be able to return a response based off the question and the information that was searched upon. This solution with seamlessly make it easier to find old information after an individual may leave the company or for new employees who may not have much context about the company. 

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Use Cases
Incorporating RAG into your enterprise can significantly enhance the retrieval and assembling time of information needed. By retrieving and generating, you can:

- Improved knowledge and information access: By combining large language models with the ability to retrieve and contextualize relevant information from external sources, RAG models can provide more accurate, up-to-date, and comprehensive responses to user queries, spanning a wide range of topics.
- Enhanced decision-making and problem-solving: With access to vast amounts of information and the ability to synthesize and reason over it, RAG models can assist users in making informed decisions, solving complex problems, and exploring various possibilities by drawing insights from diverse sources

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Architecture
![](/static/disappearing-workforce/architecture-dp.png)

The goal of this module is to give you hands-on experience leveraging foundation models (FMs) and retrieval-augmented generation (RAG) using Vector engine for OpenSearch Serverless and Amazon Bedrock. Here we use Amazon Bedrock's Knowledge base feature to simplify the RAG workflow.

You take the following steps to set up and use your knowledge base using Amazon Bedrock,

- [Step 1 Setup your knowledge base by uploading the data sources to S3](/disappearing-workforce/configure-knowledge-base.md).
- Step 2 Sync the data between s3 and the OpenSearch serverless vector engine.
- [Step 3 Query the knowledge base and receive augmented responses through Streamlit application.](/disappearing-workforce/app.md)

In the following modules, you will perform the above steps and simplify setting up a OpenSearch serverless RAG solution using Amazon Bedrock's Knowledge base feature.

# Sample files
Download and save the following files to the **~/environment/genai-for-energy-manufacturing/data/disappearing_workforce/sample_pdfs** folder.
- [Exon Mobile Drilling Guide PDF](https://www.scribd.com/document/465487836/Exon-Mobile-Drilling-Guide-pdf)
- [Geophysical characterization of the Ota-Vila Franca de Xira-Lisbon-Sesimbra fault zone, Portugal](https://www.researchgate.net/publication/241259383_Geophysical_characterization_of_the_Ota-Vila_Franca_de_Xira-Lisbon-Sesimbra_fault_zone_Portugal)

