# Recebe uma quantidade de cigarros fumados por dia e a quantidade de anos que fuma, e retorna o total de dias perdidos, sabendo que cada cigarro reduz a vida em 10 minutos.

from math import ceil


def dias_perdidos_por_fumar(dias, ano):
    total_cigarros_fumados = (dias * 365) * ano
    dias_perdidos = ((total_cigarros_fumados * 10) / 60) / 24
    print(
        f"\nOs dias de vida perdidos por conta do cigarro corresponde a {ceil(dias_perdidos)} dias \n"
    )


dias = int(input("\nInforme a quantidade de cigarros fumados por dia: "))
ano = int(input("\nInforme a quantidade de anos que fuma: "))

dias_perdidos_por_fumar(dias, ano)
