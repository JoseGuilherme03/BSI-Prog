#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número de 0 a 9999: '))

centena = numero // 100 %10
dezena = numero // 10 %10
unidade = numero // 1%10

print(f'O digito de centena é {centena}')
print(f'O digito de dezena é {dezena}')
print(f'O digito em unidades é {unidade}')
