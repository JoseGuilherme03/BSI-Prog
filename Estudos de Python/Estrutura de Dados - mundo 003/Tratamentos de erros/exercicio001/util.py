def leiaint(msg):
    ok = False
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o número\033[m')
            valor = 0
        except (ValueError,TypeError):
            print(f'\033[31mERRO!! Digite um número inteiro valido \033[m')
        else:
            ok = True
            if ok == True:
                break
    return valor

def leiafloat(msg):
    ok = False
    while True:
        try:
            valor = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar o número\033[m')
        except (ValueError,TypeError):
            print(f'\033[31mERRO!! Digite um número float válido \033[m')
        else:
            ok = True
            if ok == True:
                break
    return valor

        
    








    

        
