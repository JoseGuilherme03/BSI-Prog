def leiadinheiro(msg):
    valor = 0
    valido = False
    while True:
        valor = str(input(msg))
        if valor.isalpha():
            print(f'\033[31mERRO!! Digite um preço válido\033[m')
        else:
            valor = float(valor)
            valido = True
        if valido == True:
            break
    return valor
