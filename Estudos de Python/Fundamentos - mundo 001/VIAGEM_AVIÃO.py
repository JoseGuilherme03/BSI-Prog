#Desenvolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas

viagem = int(input('Informe a distancia da sua viagem: '))

if viagem <= 200:
    preço = viagem * 0.50
    print(f'Sua viagem de {viagem}km a passagem irá custar R${preço} reais')

else:
    preço = viagem * 0.45
    print(f'Sua vaijem de {viagem}km a passagem irá custar R${preço} reais')    