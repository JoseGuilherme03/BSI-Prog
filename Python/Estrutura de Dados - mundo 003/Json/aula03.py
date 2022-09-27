import json

carros_json = '{"marca": "honda", "modelo": "HRV", "cores":["verde","azul","amarelo","vermelho"]}'

carros = json.loads(carros_json)

for valor in carros["cores"]:
    print(valor)