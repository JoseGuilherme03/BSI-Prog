carteira = float(input('quantos reais você tem na carteira? R$ :'))

euro = 5.15
conversao = carteira / euro

print(f'Com R${carteira} reais você podera comprar EUR${round(conversao,2)} euros')