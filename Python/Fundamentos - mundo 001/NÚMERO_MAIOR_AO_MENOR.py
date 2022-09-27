#Faça um programa que leia tres múmeros e mostre qual é o número maior e qual é o número menor.

from re import A
from regex import B, F


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a

#Verificando quem é menor
if b < c and b < a: 
    menor = b
if c < b and c < a:
    menor = c

#Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')






