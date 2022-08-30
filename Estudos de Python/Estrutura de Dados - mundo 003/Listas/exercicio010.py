#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[],[]]


for v in range(1,8):
    n = int(input(f'Digite o {v}° número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
    

print(f'Os valores digitados foram {valores}')
print(f'Os valores par são {valores[0]}')
print(f'Os valores impar são {valores[1]}')
    

    

























