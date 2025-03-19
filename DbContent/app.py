import boto3
import json
import logging
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def listAll_products(event, context):
    try:
        response = table.scan()
        return response['Items']
    except Exception as e:
        logger.error(f"Erro ao consultar os produtos: {e}")
        raise  

def get_product_by_id(event, context):
        try:
            product_id = event['pathParameters']['id']
            response = table.get_item(Key={'id': product_id})

            if 'Item' in response:
                product = response['Item']
                return {
                    'statusCode': 200,
                    'body': json.dumps(product)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Produto não encontrado'})
                }
        except Exception as e:
            logger.error(f"Erro ao localizar o item com ID: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }    
    

def lambda_handler(event, context):
    try:
        path = event['path']
        method = event['httpMethod']

        if path == '/products' and method == 'GET':
            products = listAll_products(event, context)
            return {
                'statusCode': 200,
                'body': json.dumps(products)
            }
        elif path.startswith('/products/') and method == 'GET':
            return get_product_by_id(event, context)
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'não foi possivel Localizar o Produto'})
            }
    except Exception as e:
        logger.error(f"Error in lambda_handler: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
