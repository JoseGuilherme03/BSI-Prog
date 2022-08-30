#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).upper().strip() [0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Os valores que você adicionou na lista foram: {valores}')
print(f'Os valores impar da lista são: {lista_impar}')
print(f'Os valores par da lista são: {lista_par}')
    