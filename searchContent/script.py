import boto3

# esse script só foi utilizado uma unica vez para atualizar a tabela, pois  como eu nao queria utilizar scan no script principal,
# por motivos do projeto crescer e ele ficar fracamente acoplado, utilizei uma tabela secundaria onde ela vai armazenar somente os ids
# que ja foram migrados, assim o script principal vai verificar se o id ja foi migrado, se sim ele ignora, se nao ele migra.
dynamodb = boto3.resource('dynamodb')

# Nome das tabelas
source_table = dynamodb.Table('api-aws-BedrockMetadataImagesS3table-BCX4LAN0KUX4')
destination_table = dynamodb.Table('ProductIdsTable')

def migrate_existing_ids():
    # Scan para buscar todos os itens da tabela original (utilizei scan por motivos didáticos, a tabela é pequena, estudando verifiquei que em casos onde as tabelas 
    #são maiores, seria melhor criar um indice)

    response = source_table.scan()
    items = response.get('Items', [])

    for item in items:
        product_id = item['id']

        # Verifica se o ID já existe 
        existing_item = destination_table.get_item(Key={'id': product_id})
        if 'Item' not in existing_item:
            destination_table.put_item(Item={'id': product_id})
            print(f"ID {product_id} migrado com sucesso.")
        else:
            print(f"ID {product_id} já existe, ignorando.")

    print("🚀 Migração concluída!")

# Executa a migração
migrate_existing_ids()