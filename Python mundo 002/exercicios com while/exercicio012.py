from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)

vitorias = 0

while True:
    impar_ou_par = str(input('Par ou impar: [P/I] ')).strip().upper()
    jogador = int(input(f'Pense em um número de 0 a 10: '))
    computador = randint(0,10)
    resultado = jogador + computador

    print('-' * 20)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {resultado}')
    print('-' * 20)

    if impar_ou_par == 'P' and resultado % 2 != 0 or impar_ou_par == 'I' and resultado % 2 == 0:
        break
    else:
        print('\033[32mVOCÊ VENCEU!! essa rodada. Vamos jogar novamente\033[m')
    vitorias += 1

print('\033[31mGAME OVER!!\033[m')
print(f'Você ganhou {vitorias} rodadas consecutivas')
    
    
