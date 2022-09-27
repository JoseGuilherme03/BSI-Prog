#Escreva um programa quer leia a velocidade de um carro.Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade atual do carro: '))

multa = (velocidade - 80) * 7

print(f'Sua velocidade é de {velocidade}km/h')

if velocidade > 80:
    print('\033[4;31mVoce foi MULTADO por exeder a velocidade permitida\033[m')

if velocidade > 80:
    print(f'Sua multa é de R${multa :.2f} reais')

else:
    print('\033[4;32mTenha um bom dia!! dirija com segurança\033[m')
