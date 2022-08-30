# Recebe a quantidade de dias que o carro foi alugado e a quantidade de quilômetros rodados, e retorna o valor a ser pago. 1 dia: 60 reais mais R$ 0,15 por km rodado.


def preco_aluguel_carro(dias, km):
    valor = (dias * 60) + (km * 0.15)
    print(
        f"O valor a ser pago referente aos dias alugados e km rodados é R${valor} reais"
    )


dias = float(input("\nInforme a quantidade de dias que o carro foi alugado: "))
km = float(input("\nInforme a quantidade de km rodados: "))

preco_aluguel_carro(dias, km)
