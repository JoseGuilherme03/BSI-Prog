aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'aprovado'
elif aluno['media'] >= 5.0:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')