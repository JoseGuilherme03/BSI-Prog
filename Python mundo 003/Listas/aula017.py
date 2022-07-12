'''num = [1,2,4,5]
palavras = ['jose','ana','luiz','maria']
num.append(6)
num.insert(2,3)
if 'jose' in palavras:
    palavras.pop(0)
print(palavras)
print(num)'''


valores = []

for c in range(1,5):
    valores.append(int(input('Digite um valor: ')))


for c, v in enumerate(valores):
    print(f' Na posição {c} encontrei o valor {v}!')

