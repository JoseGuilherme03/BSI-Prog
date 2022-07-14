# Recebe um salário e sua porcentagem de aumento, e retorna  o novo salário.


def aumento_salarial(salario, porcentagem):
    aumento = salario + (salario * porcentagem) / 100
    print(f"Seu sálario é de R${salario} reais após o aumento passou a ser R${aumento}")


salario = float(input("\nDigite seu sálario: R$ "))
porcentagem = float(input("\nDigite a porcentagem do seu aumento: "))

aumento_salarial(salario, porcentagem)
