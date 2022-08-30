dados = {}
gols = []

dados['nome'] = str(input('Nome: '))
dados['partidas'] = int(input('Número de partidas: '))

for p in range(1,dados['partidas']+1):
    gols.append(int(input(f'Quantos gols na partida {p}: ')))


totgols = sum(gols)
dados['gols'] = gols[:]
dados['total'] = totgols

print('-=' * 30)
print(dados)
print('-=' * 30)

for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for i,v in enumerate(dados['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols')
print(f'foi um total de {dados["total"]}')