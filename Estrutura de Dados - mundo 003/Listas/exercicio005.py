# Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# - A quantidade de números digitados
# - A lista em ordem decrescente
# - E mostre se o valor 5 aparece na lista e em que posição está  

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(numeros)} números')
print(f'A lista em ordem decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista e está na posição {numeros.index(5)}')
else:
    print('O valor 5 não faz parte da lista')

