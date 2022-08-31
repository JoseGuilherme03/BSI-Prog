import json
from turtle import xcor

# dictionary -> obejto json
carros_dictionary = {"marca": "honda", "modelo": "HRV", "cor": "prata"}

# list -> array json
carros_list = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]

# tuple -> array json
carros_tuple = ("honda", "volkswagem", "ford", "fiat", "chevrolet")

# Passando parâmetros no json
carros_json = json.dumps(
    carros_dictionary, indent=4, separators=(":", " = "), sort_keys=True
)

print(carros_json)
