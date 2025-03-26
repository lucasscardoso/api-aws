import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        user_name = event['userName']
        user_attributes = event['request']['userAttributes']
        email = user_attributes['email']
        birthdate = user_attributes.get('birthdate', 'N/A')

        item = {
            'id': email,
            'birthdate': birthdate
        }

        table.put_item(Item=item)

        print('Dados do usuário armazenados no DynamoDB.')
        return event

    except Exception as e:
        print(f'Erro ao armazenar dados no DynamoDB: {e}')
        raise e
