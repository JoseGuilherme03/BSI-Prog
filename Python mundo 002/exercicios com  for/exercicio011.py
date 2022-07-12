#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheresmenor20 = 0

for p in range(1,5):
    print('-' * 5,f'{p}° PESSOA','-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenor20 += 1

mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O nome do homem mais velho é {nomevelho}')
print(f'Ao total são {mulheresmenor20} mulhere(s) menor de 20 anos')

