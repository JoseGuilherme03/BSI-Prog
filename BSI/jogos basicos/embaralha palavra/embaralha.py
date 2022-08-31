# Desafio Proposto
"""
Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo é acertar a palavra em até 5 tentativas. Informe sempre quantas tentativas ele ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo (que mude de forma aleatória). Ao final, mostre a palavra correta e o número de tentativas que ele utilizou.
"""

from time import sleep
from random import choice
from funcoes import *


palavra_sorteada = 'jose'#choice(open("palavras.txt").read().split()) # Vai abrir o arquivo.txt e sorteia uma palavra)  

dificuldade = menu('Nivel de Dificuldade:',['Facil','Intermediário','Dificil'])

tema = menu('Tema da Palavras:',['Cidades','Fruta','Países','Objetos'])

    



#print(
#    f"\033[93mTente desvendar essa palavra ->\033[m \033[32m{embaralha_palavra(palavra_sorteada)}\033[m"
#)


