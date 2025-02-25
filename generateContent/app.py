import json
import boto3 # Importando a biblioteca boto3 para trabalhar com os serviços da AWS
import os # Para recuperar variáveis de ambiente


bedrock_client = boto3.client("bedrock-runtime")
model_id = os.environ['MODEL_ID'] # ID do modelo de Machine Learning criado no Bedrock
prompt_title = os.environ['PROMPT_TITLE'] # Título do prompt criado no Bedrock
prompt_description = os.environ['PROMPT_DESCRIPTION'] # Descrição do prompt criado no Bedrock


def invoke_bedrock(prompt):
    # Função para invocar o modelo de Machine Learning criado no Bedrock
    request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "temperature": 0.5,
        "messages":[
            {
                "role":"user",
                "content": [{"type":"text", "text": prompt}]
            }
        ]
    }
    
    # Carrega o request em formato JSON
    json_request = json.dumps(request)
    
    # Invoca o modelo de Machine Learning
    response = bedrock_client.invoke_model(modelId=model_id, body=json_request)
    
    # Carrega a resposta em formato JSON
    model_response = json.loads(response['body'].read())
    
    # Recupera o texto da resposta
    text_response = model_response['content'][0]['text']
    
    print (text_response)
    
    return text_response

def lambda_handler(event, context):
    # Capturar evento SQS
    if 'Records' in event:
        for record in event['Records']:
            message_body = json.loads(record['body'])
            print(message_body)
            
            labels = message_body.get('labels',{})
            
            prompt_title_final = f"{prompt_title}  Clothing, Shirt, T-Shirt"
            
            response = invoke_bedrock(prompt_title_final)
            
            print(response)