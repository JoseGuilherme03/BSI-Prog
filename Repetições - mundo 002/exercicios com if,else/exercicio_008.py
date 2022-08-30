# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5:Abaixo do peso/ -Entre 18.5 e 25:Peso Ideal/ - 25 até 30: Sobrepeso/ -30 até 40:Obesidade/ -acima de 40:Obesidade mórbida

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))


def imcideal(peso,altura):
    imc = peso / (pow(altura,2))
    print(f"O IMC dessa pessoa é de {imc:.1f} ")
    if imc < 18.5:
        print("A pessoa está ABAIXO DO PESO")
    elif imc >= 18.5 and imc <= 25:
        print("A pessoa está no PESO IDEAL")
    elif imc > 25 and imc < 30:
        ("A pessoa está SOBREPESO")
    elif imc >= 30 and imc <= 40:
        print("A pessoa está OBESA")
    else:
        print("A pessoa está com obesidade mórbida")


imcideal(peso,altura)
