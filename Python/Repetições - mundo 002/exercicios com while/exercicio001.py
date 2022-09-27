# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.




sexo = str(input("Informe o sexo da pessoa: [M/F] ")).upper().strip()[0]
while sexo not in "MF":
    sexo = (
        str(input("Dados inválidos. Informe seu sexo novamente: ")).upper().strip()[0]
    )
print(f"Dados {sexo} informados com sucesso!!")
