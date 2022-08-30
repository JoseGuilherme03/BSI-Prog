#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta. 
# - Mostre a soma de todos os valores pares digitados 
# - Mostre a soma dos valores da ultima coluna
# - Mostre o maior valor da segunda linha

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = 0
scoluna = 0
mai = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um número para [{l},{c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
 
print('-=' * 30)
print(f'A soma de todos os valores par digitados é {spar}')
for l in range(0,3):
    scoluna += matriz[l][2]
print(f'A soma dos valores da última coluna é {scoluna}')
for c in range(0,3):
    if c == 0:
        mai = matriz[c][1]
    elif matriz[c][1] > mai:
        mai = matriz[c][1]
print(f'O maior valor da segunda linha é {mai}')


