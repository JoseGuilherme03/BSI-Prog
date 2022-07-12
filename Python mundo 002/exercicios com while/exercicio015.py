print('-=' * 20)
print('BANCO CEV')
print('-=' * 20)

valor = int(input('Informe o valor que deseja sacar: R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        elif ced == 20:
            ced = 1
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('FIM DO PROGRAMA')
        

