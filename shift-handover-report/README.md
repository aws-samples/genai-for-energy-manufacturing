
# Generate Shift Handover Report

Generate Shift Handover Report using Bedrock, Amazon Rekognition, Whisper Transcribe and Streamlit

# Lab introduction

Final product:

![synthetic image generation](/static/shift-handover-report/shift-handover-report_options.png)

In this lab, we will build a simple chat application designed to generate summaries for shift handover reports during shift changes at industrial facilities, ensuring smooth and efficient communication between shifts using [Amazon Rekognition](https://aws.amazon.com/rekognition), [Amazon Bedrock](https://aws.amazon.com/bedrock), [Whisper Transcribe](https://github.com/openai/whisper) and Streamlit. We will upload PDF, images, audio files, extract all contents, pass the extracted data to selected Generative AI models via Bedrock, generate summaries, and allow users to chat with the document. While this is a fairly straightforward example, it demonstrates the usage of Bedrock Converse to provides a consistent interface that works with all GenAI models that support messages.

### Bderock Converse API
We will use [Bderock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html) to send messages to the specified Amazon Bedrock model. Converse provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models.

# Use cases
Integrating GenAI into your shift handover report process can significantly enhance the clarity, comprehensiveness, and efficiency of information transfer between shifts. By summarizing equipment health, work activity, photos, voice memos, and ERP changes, this application ensures that critical information is effectively communicated during shift changes at industrial facilities. This approach is particularly useful for the following use cases:

- **Summarizing Equipment Health:** Automatically compile and summarize the health status of critical equipment, highlighting any issues or maintenance performed during the shift.
- **Documenting Work Activity:** Generate a concise summary of all work activities completed, ongoing tasks, and any outstanding issues that need attention in the next shift.
- **Incorporating Visual Data:** Integrate photos and images of equipment, maintenance logs, or incident reports to provide a visual context to the summary.
- **Transcribing Voice Memos:** Convert voice memos into text and integrate them into the report, ensuring verbal updates are captured and communicated effectively.
- **Tracking ERP Changes:** Summarize any changes or updates made in the ERP system, ensuring all modifications are documented and communicated to the incoming shift.
- **Facilitating Effective Handover:** Provide a comprehensive yet concise summary for day/night shifts, ensuring all essential information is communicated clearly and operations can be handed over smoothly and efficiently.

By utilizing this application, industrial facilities can improve the accuracy and efficiency of shift handovers, reduce the risk of miscommunication, and ensure seamless continuity in operations.

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Architecture
![synthetic image generation](/static/shift-handover-report/intro.jpg)

![synthetic image generation](/static/shift-handover-report/arch.png)

This application consists of two files: one for the Streamlit front end, and one for the supporting library to make calls to the backend services (Amazon Bedrock, Amazon Rekognition, Whisper Transcribe).

## Prerequisites: Install ffmpeg (required for audio files processing)
1. Select the bash terminal in AWS Cloud9 and run the following commands
```
sudo apt --fix-broken install
sudo apt install ffmpeg
```

If any popup appears, just click OK or hit the Enter button.

# Sample files
Download and upload the following file 

- [Marsh Risk Engineering Position Paper 07 Shift Handover](https://www.marsh.com/content/dam/marsh/Documents/PDF/ru/en/Marsh-Risk-Engineering-Position-Paper-07-Shift-Handover.pdf)

# Run the Streamlit app
1. While in the terminal, change directory.

```
cd ~/environment/genai-for-energy-manufacturing/shift-handover-report
```

2. Run the streamlit command from the terminal.

```
streamlit run shr_app.py --server.port 8080
```

Ignore the Network URL and External URL links displayed by the Streamlit command. Instead, we will use AWS Cloud9's preview feature.

3. In AWS Cloud9, select Preview -> Preview Running Application.

![shift handover report](/static/shift-handover-report/cloud9-preview.png)

You should see a web page like below:

![shift handover report](/static/shift-handover-report/shift-handover-report_options.png)

4. Try out the application and see how different models perform when building a conversation with your documents.

### Enter prompts and see the responses
Let's ask the following questions and see what happens:
   - Did we drill today?
   - Who was the operator?
   - Have there been any safety incidents?

Close the preview tab in AWS Cloud9. Return to the terminal and press Control-C to exit the application.
