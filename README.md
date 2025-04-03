# api-aws

Este projeto é uma API Serverless construída com AWS SAM (Serverless Application Model). Ele inclui funcionalidades para upload de imagens, categorização, autenticação de usuários e recuperação de produtos.

## 📌 Visão Geral

A aplicação utiliza vários serviços da AWS, incluindo:
- **S3** para armazenamento de imagens.
- **DynamoDB** para armazenar metadados.
- **Cognito** para autenticação de usuários.
- **Lambda** para execução de funções serverless.
- **SQS** para processamento assíncrono.
- **SNS** para notificações.

## 🚀 Recursos

### 1️⃣ Upload de Imagem
Armazena imagens no **S3** e gera URLs pré-assinadas para upload.

### 2️⃣ Autenticação de Usuário
Gerenciado pelo **Cognito**, permitindo login com email e senha.

### 3️⃣ Categorização de Imagem
Usa **AWS Rekognition** para identificar labels e enviar para **SQS**.

### 4️⃣ Geração de Conteúdo
Utiliza **AWS Bedrock** para criar descrições e títulos de produtos com base nas imagens enviadas.

### 5️⃣ Gerenciamento de Produtos
Permite buscar produtos armazenados no **DynamoDB** via API.

## 🛠 Tecnologias Utilizadas
- **AWS SAM** (Serverless Application Model)
- **AWS Lambda**
- **Amazon S3**
- **Amazon DynamoDB**
- **Amazon Cognito**
- **Amazon Rekognition**
- **Amazon SQS**
- **Amazon SNS**
- **AWS Bedrock**

## 📂 Estrutura do Projeto

![Diagrama do projeto original](/assets/Diagrama.png)

## 🔧 Instalação e Deploy
### 1️⃣ Pré-requisitos
Certifique-se de ter instalado:
- AWS CLI configurado
- AWS SAM CLI
- Python 3.13

### 2️⃣ Construção do Projeto
```sh
sam build
```

### 3️⃣ Implantação
```sh
sam deploy --guided
```

## 📌 Endpoints da API
| Rota                  | Método | Descrição |
|-----------------------|--------|-----------|
| `/presigned-url`      | GET    | Gera uma URL pré-assinada para upload de imagem |
| `/products`           | GET    | Retorna todos os produtos |
| `/products/{id}`      | GET    | Retorna detalhes de um produto específico |

## 🔑 Autenticação
Os usuários devem se autenticar via Cognito para acessar funcionalidades protegidas.

📢 **Observação:** Certifique-se de configurar corretamente suas credenciais AWS antes de implantar este projeto!

