#Crie um programa que leia um número INTEIRO na tela e mostre se ele é PAR ou ÍMPAR


numero = int(input('Digite um número: '))

resultado = numero % 2

if resultado == 0 :
    print(f'O número {numero} é PAR')
    
else:
    print(f'O número {numero} é ÍMPAR')
