# Synthetic Image Generation for Predictive Maintenance
Augmenting Predictive Maintenance with Synthetic Image Generation

# Lab Introduction

Final product:

![synthetic image generation](/static/predictive-maintenance/pm_app.png)

In this lab, we will build a synthetic image generation application using [Amazon Bedrock](https://aws.amazon.com/bedrock/), [Titan Image Generator](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-image-models.html), and Streamlit. We will use Amazon Bedrock's Titan Image Generator to generate synthetic images of the described conditions. While this is a relatively simple example, it showcases how to integrate generative AI models to create synthetic training data for computer vision tasks like predictive maintenance.

You can build the application code by copying the code snippets below and pasting them into the indicated Python files.


# Use Cases
Incorporating synthetic image generation into your predictive maintenance workflow can significantly enhance the accuracy and robustness of your computer vision models. By generating diverse and realistic images of degraded equipment conditions, you can:

- Augment your training data with rare or challenging scenarios that may be underrepresented in real-world datasets.
- Improve your model's ability to detect and classify various types of equipment degradation, such as rust, corrosion, water damage, or other forms of wear and tear.
- Reduce the need for costly and time-consuming manual data collection and annotation processes.

You can build the application code by copying the code snippets below and pasting into the indicated Python file.

# Architecture
![synthetic image generation](/static/predictive-maintenance/architecture.png)

This application consists of two files: one for the Streamlit front-end, and one for the supporting library to make calls to Bedrock.

# Run the Streamlit App
1. Select the bash terminal in your development environment and change the directory.

```bash
cd ~/environment/genai-for-energy-manufacturing/predictive-maintenance
```

2. Run the Streamlit command from the terminal.

```bash
streamlit run pm_app.py --server.port 8080
```

Ignore the Network URL and External URL links displayed by the Streamlit command. Instead, we will use AWS Cloud9's preview feature.

3. In AWS Cloud9, select Preview -> Preview Running Application.

![root cause analysis](/static/root-cause-analysis/cloud9-preview.png)

You should see a web page like the one below:

![predictive maintenance](/static/predictive-maintenance/pm_app.png)

4. Try entering different types of degradation conditions, and observe the generated text descriptions and synthetic images.

5. Close the web browser tab and return to the terminal. Press Control-C to exit the application.

### Troubeshotting app?
run this command to release port 8080

```bash
fuser -k 8080/tcp
```

