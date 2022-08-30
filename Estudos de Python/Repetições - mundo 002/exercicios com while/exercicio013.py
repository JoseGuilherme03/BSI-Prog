totmulher20 = 0
tothomem = 0
tot18 = 0
while True:
    print('-=' * 20)
    print('CADASTRE UMA PESSOA')
    print('-=' * 20)

    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    if continuar == 'N':
        break

print(f'Total de pessoa(s) com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomem} homen(s) cadastrados')
print(f'E temos {totmulher20} mulhere(s) com menos de 20 anos')


    

