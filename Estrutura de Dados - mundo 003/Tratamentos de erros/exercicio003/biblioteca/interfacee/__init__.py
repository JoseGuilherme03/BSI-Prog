def linha(tam=42):
    return '-' * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAl')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m ')
        c +=1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            valor = int(valor)
            ok = True
        else:
            print(f'\033[31mERRO!! Digite um número inteiro valido \033[m')
        if ok == True:
            break
    return valor


