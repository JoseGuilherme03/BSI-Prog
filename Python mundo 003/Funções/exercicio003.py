from time import sleep


def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        for cont in range(i, f+1, p):
            print(cont,end=' ',flush=True)
            sleep(0.3)
    else:
        for c in range(i,f-1,-p):
            print(c,end=' ',flush=True)
            sleep(0.3)
    print('Fim!!')

# Programa Principal 
contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)