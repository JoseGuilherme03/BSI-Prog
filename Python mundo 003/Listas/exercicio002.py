#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


numeros = []

while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado. Não irei adicionar')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).upper().strip() [0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Você digitou os números {sorted(numeros)}')




