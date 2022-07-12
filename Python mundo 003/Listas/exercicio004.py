#Adicione valores a uma lista única e coloque os em ordem crescente.

valores = []
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(sorted(valores))