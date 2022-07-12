#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
# - Quantas pessoas foram cadastradas 
# - Lista das pessoas mais pesadas 
# - Lista da pessoas mais leves


temporario = []
principal = []
mai = 0
men = 0

while True:
    temporario.append(str(input('Digite o nome da pessoa: ')))
    temporario.append(float(input('Digite o peso da pessoa: ')))
    if len(principal) == 0:
        mai = men = temporario[1]
    else:
        if temporario[1] > mai:
            mai = temporario[1]
        if temporario[1] < men:
            men = temporario[1]

    principal.append(temporario[:])
    temporario.clear()
    resp = input('Quer continuar: [S/N] ')
    if resp in 'Nn':
        break

print(f'Foram cadastrado {len(principal)} pessoas')
print(f'O maior peso foi {mai}kg.De ',end='')
for p in principal:
    if p[1] == mai:
        print(p[0],end=' ')
print('')
print(f'O menor peso foi {men}kg. De ',end='')
for p in principal:
    if p[1] == men:
        print(p[0],end='')
print('')








































'''
dados = []
peso = []
pessoas = []
cont = 0

while True:
    pessoas.append(str(input("Digite o nome da pessoa: ")).upper())
    peso.append(float(input("Digite o peso da pessoa: ")))
    cont += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Você quer continuar: [S/N] ")).strip().upper()
    if resp == "N":
        break



pmin = min(peso)
pmax = max(peso)
localmax = peso.index(pmax)
localmin = peso.index(pmin)


print("-=" * 30)
print(f'O total de pessoas cadastradas foi {cont}')
print(f'A pessoa com maior peso foi {pessoas[localmax]} com {pmax} kg')
print(f'A pessoa com menor peso foi {pessoas[localmin]} com {pmin}kg')'''
