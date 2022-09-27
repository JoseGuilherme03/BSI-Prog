# Crie um programa que jogue jokenpo com o computador

from random import randint



print(
    """Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")
jogador = int(input("Sua jogada: "))
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)
print("-=" * 20)
print(f"     O computador jogou {itens[computador]}")
print(f"     O jogador jogou {itens[jogador]}")
print("-=" * 20)
if computador == 0:  # COMPUTADOR JOGOU PEDRA
    if jogador == 1:
        print("JOGADOR GANHOU!!")
    elif jogador == 0:
        print("EMPATE!!")
    elif jogador == 2:
        print("COMPUTADOR GANHOU!!")
    else:
        ("\033[0;31mJOGADA INVÁLIDA!!\033\[m")
if computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("COMPUTADOR GANHOU!!")
    elif jogador == 1:
        print("EMPATE!!")
    elif jogador == 2:
        print("JOGADOR GANHOU!!")
    else:
        ("\033[0;31mJOGADA INVÁLIDA!!\033[m")
if computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print("JOGADOR GANHOU!!")
    elif jogador == 1:
        print("COMPUTADOR GANHOU!!")
    elif jogador == 2:
        print("EMPATE!!")
    else:
        print("\033[0;31mJOGADA INVÁLIDA!!\033[m")



