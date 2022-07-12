primeirotermo = int(input('Informe o termo da PA: '))
razao = int(input('Informe a razão da PA: '))

cont = 1

while cont <= 10:
    print(f'{primeirotermo} → ', end='')
    primeirotermo += razao
    cont += 1
print('FIM')