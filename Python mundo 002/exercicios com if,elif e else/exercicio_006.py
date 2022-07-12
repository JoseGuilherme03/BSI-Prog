#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos:mirim, até 14 anos:infantil,até 19 anos:junior,até 25 anos:sênior,acima:master

from datetime import date
anonascimento = int(input('Informe sua data de nascimento: '))

def categoriananatação(anonascimento):
    idade = date.today().year - anonascimento
    if idade <= 9:
        print('A categoria do atleta é MIRIM')
    elif idade <= 14:
        print('A categotia do atleta é INFANTIL')
    elif idade <= 19:
        print('A categoria do atleta é JUNIOR')
    elif idade <= 25:
        print('A categoria do atleta é SÊNIOR')
    else:
        print('A categoria do atleta é MASTER')


categoriananatação(anonascimento)

