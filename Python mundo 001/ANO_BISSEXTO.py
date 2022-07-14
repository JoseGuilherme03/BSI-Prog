#Faça um programa que leia um anoa qualquer e mostre se ele é bissexto

from datetime import date
ano = int(input('Informe um ano, se quiser analisar o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano BISSEXTO')

else:
    print(f'O ano {ano} NÂO é BISSEXTO')