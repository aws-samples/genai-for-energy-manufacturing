# Disappearing Workforce App

Disappearing Workforce Retrieval Augmented Generation (RAG) Framework with Amazon Bedrock

This application consists of two files: one for the Streamlit front-end, and one for the supporting library to make calls to Bedrock.


# Retrieve the Bedrock Knowledge Base ID
1. First, go back to the AWS console and type in Amazon Bedrock in the Knowledge Base. Click on "Amazon Bedrock".

2. You should arrive at the Amazon Bedrock Get started page. Click the 3 bars on the top left hand corner

3. Then click Knowledge bases under "Orchestration".

4. Click on the Knowledge base "bedrock-disappearing-workforce-kb".

5. Retrieve the Knowledge base ID by Copying and keeping it somewhere on the side. You will need this Knowledge base ID later to refer to the Data source the Foundation model is indexing from. 

Replace the kb_id in rag_back.py with the ID in Bedrock under knowledge bases.

# Run the Streamlit App

1. Select the bash terminal in your development environment and change the directory.

```bash
cd ~/environment/genai-for-energy-manufacturing/disappearing-workforce
```

2. Run the Streamlit command from the terminal.

```bash
streamlit run rag_front.py --server.port 8080
```

3. Follow the instructions provided by the Streamlit command to access the application in your web browser.

<br>

**You should see a web page like the one below**:

![disappearing-workforce](/static/disappearing-workforce/streamlit.png)

Feel free to ask the following questions
- Tell me about ExxonMobil Drilling Operations
- What are the general operational guidelines for ExxonMobil Platform Rigs?
- Tell me more about Carburetors.
- What is the update on our operations at Rig 12 in the Permian Basin?
- Summarize the Pluspetrol Colombia Daily Operational Report.
- What are important things to consider when talking about Petroleum Well Construction?
- What are the predominant factors and/or features of a successful shale play?
