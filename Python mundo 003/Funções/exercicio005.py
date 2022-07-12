from random import randint, sample
from time import sleep

def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ',end='', flush=True)
        sleep(0.3)
    print('PRONTO!!')

    
def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando todos os valores pares de {lst}, temos {soma}')

# Programa Principal
numeros = []
sorteia(numeros)
somapar(numeros)


