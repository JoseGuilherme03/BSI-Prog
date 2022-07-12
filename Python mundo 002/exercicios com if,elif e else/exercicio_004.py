# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alsitar ao serviço militar.-Se é a hora de se alistar.-Se já passou do tempo do alistamneto.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
anonascimento = int(input("Informe sua data de nascimento: "))


def alistamentomilitar(anonascimento):
    anoatual = date.today().year
    idade = anoatual - anonascimento
    tempoquefalta = 18 - idade
    tempoquepassou = idade - 18
    
    if idade < 18:
        anoalistamento = anoatual + tempoquefalta
        print(f"Ainda vai se alistar, falta {tempoquefalta} ano(s)")
        print(f'Seu alistamento vai ser em {anoalistamento}')
    elif idade == 18:
        print("\033[0;32mÉ hora de se alistar\033[m")
    else:
        anoalistamento = anoatual - tempoquepassou
        print(f"Já passou do tempo de se alistar, faz {tempoquepassou} ano(s) ")
        print(f'Seu alistamento foi em {anoalistamento}')


alistamentomilitar(anonascimento)
