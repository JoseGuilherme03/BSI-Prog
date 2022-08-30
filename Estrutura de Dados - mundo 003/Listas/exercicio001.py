#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

from operator import index


valores = []

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        vmax = vmin = valores[c]
    else:
        if valores[c] > vmax:
            vmax = valores[c]
        if valores[c] < vmin:
            vmin = valores[c]

print('-=' * 30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi o {max(valores)} nas posições ' , end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f'{c}...' , end='')

print(f'\nO menor valor foi {min(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f'{c}...', end='')
















'''print(f'O maior valor foi o {vmax} nas posições ',end='')

for i, v in enumerate(valores):
    if v == vmax:
        print(f'{i}... ',end='')

print(f'\nO menor valor foi o {vmin} nas posições ',end='')

for i, v in enumerate(valores):
    if v == vmin:
        print(f'{i}... ',end='')'''





