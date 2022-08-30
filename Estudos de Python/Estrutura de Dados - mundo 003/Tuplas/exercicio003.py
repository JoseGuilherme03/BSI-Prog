from random import sample

lista = (1,2,3,4,5,6,7,8,9,10)
sorteio = sample(lista,5)

print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
