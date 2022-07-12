# Escreva um número que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

num = int(input("Informe um número inteiro qualquer: "))
base = int(
    input(
    """Escolha uma das bases para conversão:
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL
    """
    )
)


def basenumerica(num, base):
    if base == 1:
        print(f"O número {num} convertido para binário fica {bin(num)[2:]}")
    elif base == 2:
        print(f"O número {num} convertido para octal fica {oct(num)[2:]}")
    elif base == 3:
        print(f"O número {num} convertido para hexadecimal fica {hex(num)[2:]}")
    else:
        print('Opção INVÁLIDA.Tente novamente.')


basenumerica(num, base)
