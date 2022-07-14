#latasTinta - Recebe quantos metros quadrados precisa pintar, e retorna a quantidade de latas de tinta para comprar. A cobertura da tinta é de 3 metros por litro de tinta. Cada lata possui 18 litros de tinta.

import math


def tinta(metro_quadrado):
    litros = metro_quadrado / 3
    lata = litros / 18
    print(f'\nA quantidades de latas necessárias para pintar {metro_quadrado} mts² é {math.ceil (lata)} latas')


metro_quadrado = float(input('\nInforme em mts² a área a ser pintada: '))

tinta(metro_quadrado)
