import json
import boto3
from pypdf import PdfReader
from typing import Dict
import whisper
from pydub import AudioSegment 

claude_system_prompt = [{"text": '''You are Claude, an AI assistant created by Anthropic to be helpful,
                harmless, and honest. Your goal is to provide informative and substantive responses
                to queries while avoiding potential harms.'''}]

models: Dict[str, callable] = {
    "bedrock titan": ["amazon.titan-text-express-v1", []],
    "bedrock claude 3 sonnet": ["anthropic.claude-3-sonnet-20240229-v1:0", claude_system_prompt],
    "bedrock claude 2": ["anthropic.claude-v2:1", claude_system_prompt],
    "bedrock claude instant": ["anthropic.claude-instant-v1", claude_system_prompt],
    "bedrock llama 3": ["meta.llama3-8b-instruct-v1:0", []],
    "bedrock mistral large": ["mistral.mistral-large-2402-v1:0", []]
}

char_limits: Dict[str, int] = {
    "bedrock titan": 100000,
    "bedrock claude 3 sonnet": 200000,
    "bedrock claude 2": 200000,
    "bedrock claude instant": 100000,
    "bedrock llama 3": 8000,
    "bedrock mistral large": 32000
}

# creates boto3 session, Bedrock and Rekognition clients
session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')
rekognition = boto3.client(service_name='rekognition')


def converse_model(model_id, messages, system_prompts=[], inference_config={}, additional_model_fields={}):
    response = bedrock.converse(
        modelId=model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    messages.append(response['output']['message'])
    return messages


def call_bedrock(model, messages):
    model_id = models[model][0]
    system_prompts = models[model][1]
    return converse_model(model_id, messages, system_prompts)


# Conversational chat function
def get_answers(chat_history, query, model):
    if query == "cancel":
        return [{"content": [{"text": 'It was swell chatting with you. Goodbye for now'}]}]
    else:
        chat_history.append({"role": "user", "content": [{"text": query}]})
        return call_bedrock(model, chat_history)


# Extract description from images.
def detect_labels(bytes_data):
    label_text = ''
    response = rekognition.detect_labels(
        Image={'Bytes': bytes_data},
        Features=['GENERAL_LABELS']
    )
    text_res = rekognition.detect_text(
        Image={'Bytes': bytes_data}
    )

    celeb_res = rekognition.recognize_celebrities(
        Image={'Bytes': bytes_data}
    )

    for celeb in celeb_res['CelebrityFaces']:
        label_text += celeb['Name'] + ' '

    for text in text_res['TextDetections']:
        if text['Confidence'] > 90:
            label_text += text['DetectedText'] + ' '

    for label in response['Labels']:
        if label['Confidence'] > 90:
            label_text += label['Name'] + ' '

    return label_text


# Parse PDF files.
def read_pdf(filename, model):
    # creating a pdf reader object
    reader = PdfReader(filename)
    # getting a specific page from the pdf file
    raw_text = []
    image_texts = []
    image_count = 0
    for page in reader.pages:
        image_text, image_count = extract_text_from_image(page, image_count)
        image_texts.append(image_text)
        raw_text.append(page.extract_text())
    content = '\n'.join(image_texts)
    content += '\n'.join(raw_text)

    return truncate_content(content,model) 


def extract_text_from_image(page, image_count):
    image_text = ''
    for image_file_object in page.images:
        try:
            resp = detect_labels(image_file_object.data)
            if resp is not None and resp != '':
                image_text += f"image_{image_count}: {resp}"
        except Exception as e:
            print(f"Error extracting text from image {image_count}: {e}")
        image_count += 1

    return image_text, image_count


def extract_text_from_audio(file_name):
    whisper_model = whisper.load_model("base")
    return whisper_model.transcribe(file_name,fp16=False)


def convert_audio_format(file_name):
    # convert first 5 mins of all file formats to wav
    sound = AudioSegment.from_file(file_name, duration=300) 
    sound.export(f'{file_name.split(".")[0]}.wav', format="wav") 
    file_name = f'{file_name.split(".")[0]}.wav'
    return file_name

# helper functions for preprocessing / chunking strategy
def truncate_content(contents, model):
    chunk = char_limits[model]
    new_contents = contents[:chunk].replace('$', '\$')
    return truncate_to_words(new_contents)


def truncate_to_words(content, max_words=800):
    words = content.split()
    return ' '.join(words[:max_words])

