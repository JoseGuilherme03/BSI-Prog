
parar = 999
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))

while n != parar:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
    
print('acabou')
print(f'Foram informados {cont} números e a soma deles é igual {soma}.')