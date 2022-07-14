#Recebe um valor em metros, e retorna o valor em milímetros, sabendo que 1 metro equivale a 1000 mm.


def mts_para_mm(metros):
    conversao = metros * 1000
    print(f'O valor de {metros}mts convertido para mm vale {conversao}mm')

    
metros = float(input('Digite o valor em mts: '))

mts_para_mm(metros)



