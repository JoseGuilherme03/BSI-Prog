#Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento. Para sálario superiores a R$1250,00 calcule um aumento de 10%.Para inferiores ou iguais, o aumneto é de 15%.

salario = float(input('Informe o sálario do funcionário: '))

aumento10 = salario + ((salario * 10) / 100)
aumento15 = salario + ((salario * 15) / 100)

if salario > 1250:
    print (f'Com o aumento de 10% o sálario do funcionário deixa de ser R${salario:.2f} reais e passa a ser R${aumento10:.2f} reais')
    
else:
    print(f'Com o aumento de 15% o sálario do funcionário deixa de ser R${salario:.2f} reais e passa a ser R${aumento15:.2f} reais')