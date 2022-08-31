import json

carros = {"marca": "honda", "modelo": "HRV", "cor": "prata"}

carros = json.dumps(carros)  # coverter de dictionay -> json

print(carros)


# coverter de json -> dictionary
"""
carros_json = '{"marca": "honda", "modelo": "HRV", "cor": "prata"}'

carros = json.loads(carros_json)

print(carros)
"""
