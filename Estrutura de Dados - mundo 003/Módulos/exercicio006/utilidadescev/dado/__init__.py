def leiadinheiro(msg):
    valor = 0
    valido = False
    while True:
        valor = str(input(msg)).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO!! Digite um preço válido\033[m')
        else:
            valor = float(valor)
            valido = True
        if valido == True:
            break
    return valor
