# Importando as Bibliotecas necessárias
import requests

# Acessando a API do Sistema da Estrutura Organizacional do Município
print('Fazendo a requisição GET no serviço web do Sistema da Estrutura Organizacional do Município...')
request = requests.get("https://sciac-api-fake.azurewebsites.net/")
data = request.content.decode('utf-8')

print('Gravando os dados em um arquivo temporário, a ser consumido pela próxima tarefa...')
# Abrindo/criando o arquivo e limpando seu conteúdo, caso haja
file = '/usr/local/airflow/dags/etlScripts/tempFiles/centros_de_custos_temp.txt'
with open(file,'w') as temp_file: 
    temp_file.truncate(0)
    # Gravando os dados obtidos e fechando o arquivo
    temp_file.write(data)
    temp_file.close()

print('Coleta de Centros de Custos concluída com sucesso!')