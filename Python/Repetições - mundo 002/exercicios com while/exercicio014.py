barato = ''
s = 0
totmil = 0
barato = 0
c = 0
menor = 0

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preço > 1000:
        totmil += 1
    if c == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome

    c += 1
    s += preço
    if resp == 'N':
        break

print('-' * 10,'FIM DO PROGRAMA', '-' * 10)
print(f'O total de compra(s) foi R${s:.2f} reias')
print(f'Temos {totmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f} reias ')
