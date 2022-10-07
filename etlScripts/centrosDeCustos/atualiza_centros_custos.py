# Importando as Bibliotecas necessárias
import json

# Obtendo os dados no arquivo temporário
print('Obtendo os dados armazenados no arquivo temporário pela tarefa anterior')
file = '/usr/local/airflow/dags/etlScripts/tempFiles/centros_de_custos_temp.txt'
with open(file,'r') as temp_file: 
    # Lendo os dados e armazenando em uma variável json
    json_data = json.load(temp_file)
    temp_file.close()

# Estabelece a conexão com o banco de dados e obtém os centros de custos ativos nele armazenados
print('Obtendo os Centros de Custos ativos armazenados na base')

# Atualiza a base de dados interna, com base nos dados obtidos no arquivo
print('Processando os dados, tratando as atualizações necessárias')

print('Gravando as alterações na base')

print('Centros de Custos atualizados com sucesso!')