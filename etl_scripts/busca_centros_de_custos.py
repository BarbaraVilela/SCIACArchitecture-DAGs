import requests
import json
# Fazendo a requisição para a API que retorna a Estrutura Organizacional do Município
print("Requisição para serviço web do Sistema da Estrutura Organizacional do Município")
request = requests.get("https://sciac-api-fake.azurewebsites.net/")
json_data = json.loads(request.content)

# Gravando os dados obtidos em um arquivo temporário
print("Gravando os dados em um arquivo temporário, a ser consumido pela próxima tarefa")
temp_file = open("centros_de_custos_temp.txt","w") 
temp_file.writelines (json.dumps(json_data))
temp_file.close()


print("Executada a coleta dos dados")