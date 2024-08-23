import json
import boto3
import textract
import anthropic
from typing import Dict

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

def call_bedrock_claude_2(prompt_text, max_tokens_to_sample=1024):
    body = {
        "prompt": anthropic.HUMAN_PROMPT+prompt_text+anthropic.AI_PROMPT,
        "max_tokens_to_sample": max_tokens_to_sample
    }
    return invoke_model("anthropic.claude-v2", body)['completion']

def call_bedrock_claude_instant(prompt_text, max_tokens_to_sample=1024):
    body = {
        "prompt": anthropic.HUMAN_PROMPT+prompt_text+anthropic.AI_PROMPT,
        "max_tokens_to_sample": max_tokens_to_sample
    }  
    return invoke_model("anthropic.claude-instant-v1", body)['completion']

def call_bedrock_titan(prompt_text, max_token_count=3072, temperature=0.7, top_p=1, stop_sequences=[]):
    body = {
        "inputText": prompt_text,
        "textGenerationConfig": {
            "maxTokenCount": max_token_count,
            "stopSequences": [],
            "temperature": temperature,
            "topP": top_p,
        }
    } 
    return invoke_model("amazon.titan-text-express-v1", body)['results'][0]['outputText']

def invoke_model(model_id, body):
  response = bedrock.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json", 
    body=bytes(json.dumps(body), 'utf-8')
  )

  return json.loads(response['body'].readlines()[0])
    
def call_bedrock(model, prompt_text):
    func = models[model]
    return func(prompt_text).replace("$","\$")

def upload_file_get_summary(file_name, model):
    motor_contents = process_file(file_name, model)
    prompt_text = 'Describe the motor specifications based on the raw data below:\n'+ motor_contents
    
    summary = call_bedrock(model, prompt_text).replace("$","\$")
    return motor_contents, summary 

def process_file(file_name, model):
    contents = textract.process(file_name).decode('utf-8')
    chunk = char_limits[model]
    motor_contents = contents[:chunk].replace('$','\$')
    return truncate_to_words(motor_contents)

def truncate_to_words(content, max_words=800):
    words = content.split()
    return ' '.join(words[:max_words])

models: Dict[str, callable] = {
  "bedrock titan": call_bedrock_titan,
  "bedrock claude instant": call_bedrock_claude_instant,
  "bedrock claude 2": call_bedrock_claude_2
}

char_limits: Dict[str, int] = {
  "bedrock titan": 4000,  
  "bedrock claude 2": 10000,
  "bedrock claude instant": 10000
}