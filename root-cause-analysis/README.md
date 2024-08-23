# Root Cause Analysis of Equipments

Root Cause Analysis of Equipments Using Manufacturer specs

# Lab introduction

Final product:

![synthetic image generation](/static/root-cause-analysis/demo.gif)

In this lab, we will build a simple text generator with [Amazon Bedrock](https://aws.amazon.com/bedrock/) , [Textract](https://aws.amazon.com/textract), and Streamlit. We will upload an electric motor datasheet specs document, extract specs, pass it to Bedrock, pass sensor data and return the foundation model’s response. While this is a fairly trivial example, it allows us to understand how to build a basic generative AI prototype with very little code.

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Use cases
Incorporating GenAI into your RCA process, you can make the analysis more adaptive, context-aware, and capable of reasoning his includes data sheets, technical manuals, and any other documentation that outlines the specifications and operational parameters is good for the following use cases:

- Understand normal operating conditions then identify deviations from specifications
- Accurate and efficient identification of root causes in electric motor issues

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Architecture
![synthetic image generation](/static/root-cause-analysis/intro.jpg)

![synthetic image generation](/static/root-cause-analysis/arch.png)

This application consists of two files: one for the Streamlit front end, and one for the supporting library to make calls to Bedrock.

# Sample files
Download and save the following files to the **~/environment/genai-for-energy-manufacturing/data/root-cause-analysis** folder.
- [RS PRO 3 Phase AC motor](https://docs.rs-online.com/7939/A700000006779781.pdf)
- [AMA-IE2 90L2 2.2kW 2 Pole](https://amtecs.co.uk/datasheet/6Gq4LEgn7OAWDRKvdJ53)
- [AC motor 6W 110-120VAC](https://transmotec.com/Download/Datasheets/Transmotec-Datasheet-AI-006W.pdf)

# Run the Streamlit app
1. Select the bash terminal in AWS Cloud9 and change directory.

```
cd ~/environment/genai-for-energy-manufacturing/root-cause-analysis
```

2. Run the streamlit command from the terminal.

```
streamlit run rca_app.py --server.port 8080
```

Ignore the Network URL and External URL links displayed by the Streamlit command. Instead, we will use AWS Cloud9's preview feature.

3. In AWS Cloud9, select Preview -> Preview Running Application.

![root cause analysis](/static/root-cause-analysis/cloud9-preview.png)

You should see a web page like below:

![root cause analysis](/static/root-cause-analysis/root-cause-analysis_options.png)

4. Try out sample sensor data and see the results.
   
5. Close the preview tab in AWS Cloud9. Return to the terminal and press Control-C to exit the application.
