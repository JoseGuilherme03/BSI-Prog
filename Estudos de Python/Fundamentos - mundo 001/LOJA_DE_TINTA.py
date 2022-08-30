

import math


area = float(input('digite a área a ser pintada em mts² :\n'))        

litros =  (area / 6) * 1.1
lata = math.ceil (litros / 18)
galao = math.ceil (litros / 3.6)
preco_lata = lata * 80
preco_galao = galao * 25

mix_latas = round (litros / 18)
mix_galoes = round ((litros - mix_latas * 18) / 3.6)

if ((litros - (mix_latas * 18) % 3.6 !=0)):
    mix_galoes += 1
    preco_mix = (mix_latas * 80) + (mix_galoes * 25)

print(f'''Para pintar uma área de {area}mts² apenas com lata(s) sera necessário {lata} lata(s) de tinta(s).
Com o valor de cada lata custando R$80,00 reais o valor total sera R${preco_lata} reais\n''')

print(f'''Para pintar uma área de {area}mts² apenas com galão sera necessário {galao} galões de tinta.
Com o valor de cada galão custando R$25,00 reais o valor total sera R${preco_galao} reais\n ''')

print(f'''Para pintar uma área de {area}mts² mesclando entre galões e latas sera necessário {mix_latas} lata(s) e {mix_galoes} galão(ões).
O valor total sera de R${preco_mix} reais ''')





