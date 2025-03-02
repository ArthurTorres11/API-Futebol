import requests
import os 
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Carregar a chave da API do arquivo .env
API_KEY = os.getenv("API_KEY")  # A chave agora vem do arquivo .env

BASE_URL = "https://api.api-futebol.com.br/v1"

# Exemplo de ID do jogador
player_id = 10  
url = f"{BASE_URL}/campeonatos"  # Verifique o endpoint correto

# Configurar os headers para a requisição
headers = {
    "Authorization": f"Bearer {API_KEY}"  # Adiciona o espaço correto após 'Bearer'
}

# Fazer a requisição
response = requests.get(url, headers=headers)

# Verificar a resposta
if response.status_code == 200:
    data = response.json()  # Dados retornados da API
    print(data)
else:
    print(f"Erro: {response.status_code} - {response.text}")
