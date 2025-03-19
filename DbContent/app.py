import boto3
import json
import logging
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
            response = table.scan()
            products = response['Items']

            return {
                'statusCode': 200,
                'body': json.dumps(products)
            }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }
    
