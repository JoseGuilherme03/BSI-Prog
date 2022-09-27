# Leia um número inteiro menor que 1000 e devolva a quantidade de centenas, dezenas e unidades do mesmo. Obs.: não utilize operações com strings.


def decompor_número(numero):
    centenas = numero // 100 % 10
    dezenas = numero // 10 % 10
    unidades = numero // 1 % 10
    print(
        f"\nO número de centenas, dezenas e unidades referente ao número {numero} => {centenas} centenas,{dezenas} dezenas e {unidades} unidades."
    )


numero = int(input("\nDigite um número menor que 1000: "))

decompor_número(numero)
