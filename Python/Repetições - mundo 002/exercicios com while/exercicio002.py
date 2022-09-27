from random import randint
from time import sleep

computador = randint(0, 5)  # faz o computador PENSAR...
print("-=-" * 20)
print("Vou pensar em um número entre 0 a 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...\n")
sleep(3)

tentativas = 1

while jogador != computador:
    if jogador > computador:
        print("MENOS...")
    else:
        print("MAIS...")
    jogador = int(
        input("Você errou!!. Tente acertar o número que número eu pensei novamente: ")
    )
    print("PROCESSANDO...\n")
    sleep(3)
    tentativas += 1

if computador == jogador:
    print("PARABÉNS!! Voce ganhou!!")
print(f"O número de tentativas até acertar foi {tentativas}")
