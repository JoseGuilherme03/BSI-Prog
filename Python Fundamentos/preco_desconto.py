#Recebe um preço e sua porcentagem de desconto, e retorna o novo preço.


def preço_com_desconto(produto,desconto):
    reajuste = produto - (produto * desconto) /100
    print(f'O valor do produto era de R${produto:.2f} reais com o desconto de {desconto:.2f}% porcento passou a custar R${reajuste:.2f} reais')


produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o porcentual de desconto: '))

preço_com_desconto(produto, desconto)

