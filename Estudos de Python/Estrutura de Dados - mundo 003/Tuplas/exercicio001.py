"""cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete,','dezoito','dezenove','vinte')

# Opção de programa para parar após o resultado
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if n >= 0 and n <= 20:
        print(f'Você digitou o número {cont[n]}')
        break
    print('TENTE NOVAMENTE.')"""


# Opção de programa para escolher se deseja parar após o resultado
cont = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete,",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    n = int(input("Digite um número de 0 a 20: "))
    if n >= 0 and n <= 20:
        print(f"Você digitou o número {cont[n]}")
        resp = " "
        while resp not in "SN":
            resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp == "N":
            break
