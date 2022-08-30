
resp = 'S'
quant = 0
soma = 0
maior = 0
menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
media = soma / quant
print('ACABOU')
print(f'A média dos {quant} números informados é {round(media,2)}')
print(f'O maior número é {maior} e o menor é {menor}')