

def aumentar(preço=0,taxa=0,formato=False):
    res = preço + (preço * taxa) / 100
    if formato == True:
        return moeda(res)
    else:
        return res


def diminuir(preço=0,taxa=0,formato=False):
    res = preço - (preço * taxa) / 100
    if formato == False:
        return res
    else:
        return moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    if formato == False:
        return res
    else:
        return moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    if formato == False:
        return res
    else:
        return moeda(res)


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preco,aumento,reducao):
    print('-'* 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco,aumento,True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco,reducao,True)}')
    print('-' * 30)
