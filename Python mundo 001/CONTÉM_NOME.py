#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

pessoa = str(input('Informe o nome da pessoa: ')).strip()

print('Seu nome tem "SILVA"?')
print('SILVA' in pessoa.upper())
