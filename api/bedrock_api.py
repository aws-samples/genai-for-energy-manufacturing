import json
import boto3
import anthropic
#
session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime')

#
bedrock_model_id = "anthropic.claude-v2" #set the foundation model

prompt = "What is the largest city in New Hampshire?" #the prompt to send to the model

body = json.dumps({
    "prompt": anthropic.HUMAN_PROMPT+prompt+anthropic.AI_PROMPT,
    "max_tokens_to_sample": 1024 
}) #build the request payload

#
response = bedrock.invoke_model(body=body, modelId=bedrock_model_id, accept='application/json', contentType='application/json') #send the payload to Bedrock

#
response_body = json.loads(response.get('body').read()) # read the response

response_text = response_body.get("completion")

print(response_text)
