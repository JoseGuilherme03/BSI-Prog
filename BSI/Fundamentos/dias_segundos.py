# Recebe uma data em dias com horas, minutos e segundos, e retorna a data em segundos.


def dias_para_segundos(dias, horas, minutos, segundos):
    conversao = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + (segundos)
    print(
        f"\nA quantidade de segundos equivalente aos valores de dias,horas,minutos e segundos é {conversao}"
    )


dias = int(input("\nDigite a quantidade de dias: "))
horas = int(input("\nDigite a quantidade de horas: "))
minutos = int(input("\nDigite a quantidade de minutos: "))
segundos = int(input("\nDigite a quantidade de segundos: "))

dias_para_segundos(dias, horas, minutos, segundos)
