import requests
import json

print("Requisição para serviço web do Sistema da Estrutura Organizacional do Município")
request = requests.get("https://sciac-api-fake.azurewebsites.net/")
todos = json.loads(request.content)
print(todos)

print("Executada a coleta dos dados")