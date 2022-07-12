# Mostre que tipo de triângulo as retas formam
# Equilatero:todos os lados iguais, Isósceles: dois lados iguais, Escaleno:todos os lados diferentes


r1 = int(input("Informe o comprimento do primeiro segmento: "))
r2 = int(input("Informe o comprimento do segundo segmento: "))
r3 = int(input("Informe o comprimento do terceiro segmento: "))


def tipodetriangulo(r1, r2, r3):
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
        print(f"Os segmentos acima PODEM FORMAR um triângulo", end=" ")
        if r1 == r2 == r3:
            print("EQUILÁTERO")
        elif r1 != r2 != r3 != r1:
            print("ESCALENO")
        else:
            print("ISÓSCELES")
    else:
        print("Os segmentos acima NÃO PODEM formar um triângulo")


tipodetriangulo(r1, r2, r3)
