#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:


frase = (input('Digite uma frase: '))
inverso = frase[::-1].upper().strip().replace(' ','')
if inverso == inverso[::-1]:
    print(f'O inverso de {frase} é {inverso}')
    print('O texto é PALINDROMO')
else:
    print(f'O inverso de {frase} é {inverso}')
    print('O texto não é PALINDROMO')