#salarioLiquido - Recebe quanto ganha por hora e quantas horas trabalho ao mês, e retorna o salário líquido.
    #Descontos:
    #- INSS é 8% do salário bruto
    #- IR é 11% do salário bruto
    #- Sindicato é 5% do salário bruto.


def salario(horas_trabalhadas,ganho):
    salario_bruto = ganho * horas_trabalhadas
    INSS = ((8 * salario_bruto) / 100)
    IR = ((11 * salario_bruto) / 100)
    sindicato = ((5 * salario_bruto) /100)
    salario_liquido = salario_bruto - (INSS + IR + sindicato)
    print(f'\nSeu salário bruto é R${salario_bruto} reais com os descontos passa a ser R${salario_liquido} reais')


horas_trabalhadas = float(input('\nInforme as hrs trabalhadas no mês: '))
ganho = float(input('Informe seu ganho por hora: '))

salario(horas_trabalhadas,ganho)

