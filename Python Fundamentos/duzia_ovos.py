# duziasOvos - Receba o número de ovos e devolva a quantidade de dúzias correspondente. Considere sempre dúzias cheias, arredondando pra cima se necessário.

import math


def duzias(ovos):
    duzias = ovos / 12
    print(f"\nA quantidade de {ovos} ovos corresponde a {math.ceil (duzias)} duzias")


ovos = int(input("\nInforme o número de ovos: "))

duzias(ovos)
