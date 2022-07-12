#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


ficha = []

while True:
    nome = str(input('NOME: ')).upper().strip()
    n1 = float(input('Primeira NOTA: '))
    n2 = float(input('Segunda NOTA: '))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1,n2],media])
    resp = str(input('Quer continuar: [S/N] ')).upper().strip()
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"N°":<4} {"NOME":<10} {"MÉDIA":>8} ')
print('-' * 26)

for i,a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')

print('-' * 30)
while True:
    notas = int(input('Digite o indice do aluno que deseja ver a nota: (n° 999 encerra o programa) '))
    if notas == 999:
        print('FINALIZANDO...')
        break
    if notas <= len(ficha) -1:
        print(f'As notas de {ficha[notas][0]} é {ficha[notas][1]}')
    
print('<<<<<<< VOLTE SEMPRE >>>>>>>')




