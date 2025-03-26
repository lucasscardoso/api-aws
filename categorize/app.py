import json
import boto3
import os

rekognition_client = boto3.client('rekognition')
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        print("Evento S3 recebido:")
        print(json.dumps(event, indent=2))  # Imprime o evento S3 formatado

        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']

        print(f"Bucket: {bucket_name}, Arquivo: {file_name}")

        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': bucket_name, 'Name': file_name}},
            MaxLabels=10,
            MinConfidence=50
        )

        labels = [label['Name'] for label in response['Labels']]

        sqs_client.send_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageBody=json.dumps({
                'bucket_name': bucket_name,
                'key': file_name,
                'labels': labels
            })
        )

        print(f"Labels detectadas: {labels}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Processamento de Labels realizado com sucesso"
            })
        }
    except Exception as e:
        print(f"Erro durante o processamento: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"Erro: {e}"
            })
        }