# Escreva um programa para aprovar o empreśtimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ala não pode exeder 30% do sálario ou então o empréstimo será negado.

valordacasa = float(input("Informe o valor da casa: "))
salario = float(input("Informe seu sálario mensal: "))
anosapagar = float(input("Informe em quantos anos deseja pagar a casa: "))


def emprestimobancario(valordacasa, salario, anosapagar):
    valordaprestacao = valordacasa / (anosapagar * 12)
    limitedaprestação = (salario * 30) / 100

    if valordaprestacao > limitedaprestação:
        print(
            f"Com o sálario de R${salario:.2f} reais, a parcela da casa ficou no valor R${valordaprestacao:.2f} reias, maior que 30% do seu sálario.\033[0;31m Seu empréstimo foi negado!!\033[m"
        )
    else:
        print(
            f"Com o sálario de R${salario:.2f} reais, a parcela da casa ficou no valor R${valordaprestacao:.2f} reias, menor que 30% do seu sálario.\033[0;32m Seu empréstimo foi aceito!!\033[m "
        )


emprestimobancario(valordacasa, salario, anosapagar)
