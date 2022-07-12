#Leia um número inteiro e imprima a tabuada do próprio. 

n = int(input("Digite o número para sua tabuada: "))

print('\033[32m----- TABUADA -----\033[m')
print('-='* 10)

for c in range(1, 11):
    print(f"""     {n} X {c} = {c * n}  """)
print('-=' * 10)
