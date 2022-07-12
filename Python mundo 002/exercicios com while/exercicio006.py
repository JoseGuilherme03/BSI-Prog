from pickletools import TAKEN_FROM_ARGUMENT1


primeirotermo = int(input('Informe o termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeirotermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')  
    mais = int(input('Mais quantos termos você deseja adicionar: '))
print(f'PA finalizada foram mostrados {total} termos')
     

