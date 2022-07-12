#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


cont = 0
soma = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Soma dos {cont} números pares é {soma}')