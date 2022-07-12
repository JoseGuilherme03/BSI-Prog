'''
pessoas = {'nome': 'josé','idade': 18,'peso':50}
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''


estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Informe a uf do estado: '))
    estado['sigla'] = str(input('Informe a sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end = ' ')



    
'''
dados = []
nomes = {1:'jose',2:'isaak',3:'gabriel'}
lugar = {1:'barra velha',2:'são paulo',3:'barra do sul'}

dados.append(nomes)
dados.append(lugar)

print(f'{dados[0][1]} mora na cidade de {dados[1][1]}')
'''