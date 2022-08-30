""" Nas variáveis:
- () => TUPLAS
- [] => LISTAS
- {} => DICIONÁRIOS """
# Tuplas são imutáveis


lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(sorted(lanche)) # => colocar a tupla de forma organizada.



for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]}")
print("Comi pra caramba!!")



"""for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra Caramba!!')
"""



"""for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
"""


'''
pessoa = ('Jose', 18 , 'Masculino' , 65)
print(f
Nome da pessoa: {pessoa[0]}
idade: {pessoa[1]}
Sexo: {pessoa[2]}
peso : {pessoa[-1]}
)
'''