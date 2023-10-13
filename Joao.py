# PROJETO - Explorando IA Generativa em um Pipeline de ETL com Python

#==========================================
# Primeira parte
#Importando Pandas para ler nossa tabela de dados com os User_ID (Arquivo.CSV)
import pandas as pd

df = pd.read_csv('SDW2023.csv')     #Lendo o arquivo
user_ids = df['UserID'].tolist()    #Alterando o retornado em lista
print(user_ids)                     #Print para verificar o retorno da leitura

#==========================================
# Segunda Parte
#Importando Requests e Json para interação com a api através da URL
import requests
import json

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app' #Atribuindo URL a uma variavel

def get_user (id):                                      #Criando uma função para coletar os dados da URL
    response = requests.get(f'{sdw2023_api_url}/users/{id}')            #Atribuindo a uma variavel os dados coletado da API (200 ou 404)
    return response.json() if response.status_code == 200 else None     #Coletando biblioteca atraves do JSON 

users = [user for id in user_ids if (user := get_user(id)) is not None] 
#print(json.dumps(users, indent=2))


import openai

openai_key = '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'
openai.api_key = openai_key

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista de marketing bancário."},
            {"role": "user", "content": f"Crie uma mensagem para {user['name']} sobre a importancia dos investimentos (maximo de 15 caracteres)"}
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    #print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

def update_users(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    sucess = update_users(user)
    print(f"User {user['name']} updated? {sucess}!")
