from time import sleep


def maior(*num):
    
    print('Analisando os valores passados...')
    for v in num:
        print(v,end=' ',flush=True)
        sleep(0.5)
    print()    
    if len(num) > 0:
        print(f'Foram informado(s) {len(num)} valore(s) ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print('NÃO FOI INFORMADO NENHUM NÚMERO')
    print('-=' * 30)


#Programa Principal
maior(5,6,8,7,9)
maior(5,10,15,50)
maior()
