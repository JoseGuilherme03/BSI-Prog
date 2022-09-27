import math

area = float(input('digite a área a ser pintada em mts²:'))

tinta = area / 3 
baldes = math.ceil (tinta / 18 )

preço = baldes * 80

print(f'Para preencher uma área de {area}mts² será necessário {baldes} balde(s) de tinta.')

print(f'Com o valor de R$80,00 reais cada balde de tinta o valor total sera de R${preço} reais')





