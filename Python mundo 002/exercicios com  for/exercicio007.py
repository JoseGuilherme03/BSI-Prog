

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


numero = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m ', end='')
        tot += 1
    else:
        print('\033[31m ', end='')
    print(c, end='')
print(f'\n\033[mO número {numero} foi divisivel {tot} vezes')
if tot == 2:
    print(f'E por isso o número {numero} é PRIMO')
else:
    print(f'E por isso o número {numero} NÃO é PRIMO')


