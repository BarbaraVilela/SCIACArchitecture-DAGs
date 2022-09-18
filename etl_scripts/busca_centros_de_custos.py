import requests
import json

# Acessa a API do Sistema da Estrutura Organizacional do Município
print("Faz a requisição GET no serviço web do Sistema da Estrutura Organizacional do Município")
request = requests.get("https://sciac-api-fake.azurewebsites.net/")
json_data = json.loads(request.content)

print("Grava os dados em um arquivo temporário, a ser consumido pela próxima tarefa")
# Abre/cria o arquivo e limpa seu conteúdo, caso haja
temp_file = open("centros_de_custos_temp.txt","r+") 
temp_file.truncate(0)

# Grava os dados obtidos e fecha o arquivo
temp_file.writelines (json.dumps(json_data))
temp_file.close()

print("Coleta de Centros de Custos concluída com sucesso!")