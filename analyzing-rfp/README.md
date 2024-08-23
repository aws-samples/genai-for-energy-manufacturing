
# Analyzing RFP Documents

Summarize an Request For Proposal(RFP) using Bedrock, LangChain, and Streamlit.

# Lab introduction

Final product:

![synthetic image generation](/static/rfp/final.jpg)

In this lab, we will summarize an Request For Proposal(RFP) using [Amazon Bedrock](https://aws.amazon.com/bedrock/), LangChain framework, and Streamlit App.

# Use Case

RFP proposals contains lengthy requirements and craft responses that can be time-consuming and tedious. We can use AI to summarise this document for streamlining the time it takes to consume these proposals. 

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Architecture

![](/static/rfp/RFPUpdated.jpg)

This application consists of two files: one for the Streamlit front-end and a backend file that stores information about the bedrock api calls and the function to perform the langchain.

# Sample files
Download and upload the following file 

- [2024 Distributed Wind Turbine Competitiveness Improvement Project](https://sam.gov/opp/021443b500c64639a56192ab05c17489/view)

# Run the Streamlit App

1. Access the bash terminal and make sure you're in the rfp directory. if not, 

```python 
cd ~/environment/genai-for-energy-manufacturing/analyzing-rfp
```

2. Run the Streamlit command from the terminal.

```bash
streamlit run rfp_app.py --server.port 8080
```

3. On Average, it would take aroud 4-5 mins for the application to process the docuement and provide a summary.

<br>

Ignore the Network URL and External URL links displayed by the Streamlit command. Instead, we will use AWS Cloud9's preview feature.

4. In AWS Cloud9, select Preview -> Preview Running Application.

![root cause analysis](/static/root-cause-analysis/cloud9-preview.png)

**You should see a web page now with the desired title and upload**:

Feel free to explore the application and test with different size documents