from datetime import date

ano = date.today().year
dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] - nasc ) + 35

print('-=' * 30)

for k, v in dados.items():
    print(f'   -{k} tem o valor {v}')