#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#-Média abaixo de 5.0: REPROVADO,-Média entre 5.0 e 6.9: RECUPERAÇÃO, -Média 7.0 ou superior: APROVADO


nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))


def media(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media < 5.0:
        print('O aluno está \033[0;31mREPROVADO\033[m')
    elif 7 > media >= 5:
        print('O aluno está em \033[0;33mRECUPERAÇÃO\033[m')
    else:
        print('O aluno está \033[0;32mAPROVADO\033[m')


media(nota1,nota2)

