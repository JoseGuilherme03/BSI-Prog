# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


from random import sample
from time import sleep
print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)

njogos = int(input('Quantos jogos você quer que eu sorteie? '))
numeros = []
for n in range (1,61):
    numeros.append(n)

for j in range (1,njogos + 1):
    print(f'Jogo{j}: {sample(numeros,6)}')
    sleep(1)

print('-=' * 5,'< BOA SORTE >','-=' * 5)



