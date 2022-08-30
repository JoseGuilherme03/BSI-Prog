# Crie um programa que leia o nome completo de uma pessoa e mostre:

# - O nome com todas as letras maiuscúlas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar os espaços)
# - Quantas letras tem o primeiro nome


nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em letras letras maiscúlas é {nome.upper()}')

print(f'Seu nome em letras minúsculas é {nome.lower()}')

print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras')

print(f'Seu primeiro nome tem {nome.find(" ")} letras')


