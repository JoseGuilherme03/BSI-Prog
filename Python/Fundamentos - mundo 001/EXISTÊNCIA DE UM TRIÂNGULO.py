#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triangulo.

print('-=' * 30)
print('           CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO                ')
print('-=' * 30)

r1 = int(input('Informe o comprimento do primeiro segmento: ')) 
r2 = int(input('Informe o comprimento do segundo segmento: '))
r3 = int(input('Informe o comprimento do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f'Com os segmentos {r1,r2,r3} é possivel montar um triângulo')

else: 
    print(f'Com os segmentos {r1,r2,r3} NÃo é possivel montar um triângulo')