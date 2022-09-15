import requests
import json

    request = requests.get("https://sciac-api-fake.azurewebsites.net/")
    todos = json.loads(request.content)
    print(todos)

print(“Executada a coleta dos dados”)