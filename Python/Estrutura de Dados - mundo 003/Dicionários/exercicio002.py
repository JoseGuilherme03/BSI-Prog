from operator import itemgetter
from random import randint
from time import sleep

jogadores = {}
ranking = []

for j in range(1,5):
    jogadores[f'jogador{j}'] = randint(1,6)

print('    >>> VALORES SORTEADOS <<<')
for k,v in jogadores.items():
    sleep(1)
    print(f'    O {k} tirou {v} no dado')
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

print('-=' * 20)
print('    === RANKING DOS JOGADORES ===')

for i,v in enumerate(ranking):
    sleep(1)
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}')