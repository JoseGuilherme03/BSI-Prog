# Recebe dois números inteiros, e retorna a sua soma.


def soma_dois_inteiros(num1, num2):
    s = num1 + num2
    print(f"A soma dos dois número é {s} ")


num1 = int(input("\nDigite  um número: "))
num2 = int(input("\nDigite um número: "))

soma_dois_inteiros(num1, num2)


def soma_dois_inteiros(num1,num2):
    soma = num1 + num2
    return soma


assert (soma_dois_inteiros(0, 0), 0)
assert (soma_dois_inteiros(-1, 0), -1)
assert (soma_dois_inteiros(1, 1), 2)
assert (soma_dois_inteiros(0, -1), -1)
assert (soma_dois_inteiros(10, 10), 20)
assert (soma_dois_inteiros(-10, -10), -20)
assert (soma_dois_inteiros(-10, 20), 10)
