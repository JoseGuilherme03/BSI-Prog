
def area(largura,comprimento):
    calculo = largura * comprimento
    print('-=' * 20)
    print('   ÁREA DE UM TERRENO   ')
    print(f'A área de um terreno {largura}x{comprimento} é de {calculo}m²')
    print('-=' * 20)


# Programa Principal
largura = float(input('Largura do terreno (mts): '))
comprimento = float(input('Comprimento do terreno (mts): '))
area(largura,comprimento)

