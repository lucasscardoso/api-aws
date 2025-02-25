import json
import boto3 # Importando a biblioteca boto3 para trabalhar com os serviços da AWS
import os # Para recuperar variáveis de ambiente

 
rekognition_client = boto3.client('rekognition') # Criando um cliente para o serviço Rekognition
sqs_client = boto3.client('sqs')
 
def lambda_handler(event, context):
   
    # FileName (nome do arquivo) que será enviado para o S3
    # Content-type  (tipo do arquivo) que será enviado para o S3
   
    # https://y3qyccqdtj.execute-api.us-east-2.amazonaws.com/Prod/hello?fileName=arquivo.txt&contentType=text/plain
 
   #captura do evento de put do aws s3
   bucket_name = event['Records'][0]['s3']['bucket']['name']
   file_name = event['Records'][0]['s3']['object']['key']

   print(event)
   print(bucket_name)
   print(file_name)
   
    #chama o evento de deteccao de labels do rekognition
   response = rekognition_client.detect_labels(
       Image={'S3Object': {'Bucket': bucket_name,'Name': file_name} },
       MaxLabels=10,
       MinConfidence=80
    )
   
   #lista de labels detectaDOS
   labels = [label['Name'] for label in response['Labels']]

   sqs_client.send_message(
      QueueUrl=os.environ['SQS_URL'], 
      MessageBody=json.dumps({
           'bucket_name': bucket_name,
           'key': file_name,
           'labels': labels
        })
        )

   print(labels)
 
   return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Processamento de Labels realizado com sucesso",
        }),
    }
 