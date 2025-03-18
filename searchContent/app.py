import json
import boto3 # Importando a biblioteca boto3 para trabalhar com os serviços da AWS


dynamodb = boto3.resource('dynamodb')
product_table = dynamodb.Table(os.environ['TABLE_NAME'])
product_ids_table = dynamodb.Table('ProductIdsTable')


def migrate_ids():
    # Recuperando todos os itens da tabela de origem
    response = product_table.scan()

    # Extraindo os IDs dos itens recuperados
    items = response.get('Items', [])

    # Inserindo os IDs na tabela de destino
    for item in items:
        product_id = item.get('id')  # Supondo que 'id' seja a chave de partição
        
        if product_id:
            # Inserindo o ID na nova tabela
            product_ids_table.put_item(
                Item={
                    'id': product_id  # Inserindo o ID na nova tabela
                }
            )
            print(f"ID {product_id} inserido na nova tabela.")

    print("Migração concluída.")

# Chamada para migrar os IDs
migrate_ids()