#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


primeirotermo = int(input('Informe o termo da PA: '))
razao = int(input('Informe a razão da PA: '))

cont = 1

while cont <= 10:
    print(f'{primeirotermo} → ', end='')
    primeirotermo += razao
    cont += 1
print('FIM')