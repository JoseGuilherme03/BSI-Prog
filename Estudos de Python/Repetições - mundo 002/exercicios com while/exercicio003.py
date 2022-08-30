n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo valor: "))
opcao = 0
while opcao != 5:
    print(
"""Escolha o que deseja fazer conforme o menu: 
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
"""
    )
    opcao = int(input("Sua opção: "))
    if opcao == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif opcao == 2:
        print(f"{n1} X {n2} = {n1*n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n1 == n2:
            print("Os dois números são iguais")
        else:
            print(f"O maior número é {n2}")
    elif opcao == 4:
        n1 = int(input("Informe o primeiro número: "))
        n2 = int(input("Informe o segundo valor: "))
    elif opcao == 5:
        print("FIM DO PROGRAMA.Volte sempre")
    else:
        print("Opção Inválida, tente novamente.")

    print("=-=" * 10)
