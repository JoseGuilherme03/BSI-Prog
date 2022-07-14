
carteira = float(input('quantos reais você tem na carteira? R$'))
dólar = 4.66
conversao = (carteira / dólar)

print(f'Com R$ {round(carteira,2)} reais você consegue comprar U$ {round(conversao,2)} dólares')