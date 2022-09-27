s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break #desconsidera a flag  e faz parar.
    s += n
    c += 1


print(f'A soma de {c} números informados é {s}')
