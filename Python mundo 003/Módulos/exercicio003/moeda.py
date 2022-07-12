


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
