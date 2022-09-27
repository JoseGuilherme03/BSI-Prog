pessoa = {}
galera = []
totpessoas = 0
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print(galera)
media = soma / len(galera)

print(f'foram cadastradas {len(galera)} pessoas')
print(f'A média de idade é de {media:.2f} anos')
print(f'A(s) mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}',end=' ')
print()
print(f'A(s) pessoas com idade acima da média foram: ',end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}',end=' ')
print()
print('>>>ENCERRADO<<<')





    
    







