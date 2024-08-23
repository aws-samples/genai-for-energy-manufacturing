import boto3

# Set up Bedrock client

kb_id = 'JGHYSNHPKU'
session = boto3.Session()
bedrock = session.client(service_name='bedrock-agent-runtime') 

claude_model_ids = [ ["Claude 3 Sonnet", "anthropic.claude-3-sonnet-20240229-v1:0"], ["Claude Instant", "anthropic.claude-instant-v1"]]

def ask_bedrock_llm_with_knowledge_base(query: str, model_arn: str, kb_id: str) -> str:
    response = bedrock.retrieve_and_generate(
        input={
            'text': query
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_arn
            }
        },
    )

    return response