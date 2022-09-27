n = int(input('Informe um número: '))
c = n
f = 1
print(f'calculando o fatorial de {n}!')
while c != 0:
    print(c, end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

