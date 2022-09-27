def linha(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

while True:
    print(linha('SISTEMA DE AJUDA PyHELP'))
    resp = str(input('Função ou Biblioteca > ')).strip().lower()
    if resp == 'fim':
        break
    print(linha(f'Acessando o manual do comando "{resp}"'))
    print(f'{help(resp)}')




