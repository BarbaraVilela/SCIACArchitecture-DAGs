# Importando as Bibliotecas necessárias
import requests
import json

# Acessando a API do Sistema da Estrutura Organizacional do Município
print("Fazendo a requisição GET no serviço web do Sistema da Estrutura Organizacional do Município...")
request = requests.get("https://sciac-api-fake.azurewebsites.net/")
json_data = json.loads(request.content)

print("Gravando os dados em um arquivo temporário, a ser consumido pela próxima tarefa...")
# Abrindo/criando o arquivo e limpando seu conteúdo, caso haja
temp_file = open("centros_de_custos_temp.txt","r+") 
temp_file.truncate(0)

# Gravando os dados obtidos e fechando o arquivo
temp_file.writelines (json.dumps(json_data))
temp_file.close()

print("Coleta de Centros de Custos concluída com sucesso!")