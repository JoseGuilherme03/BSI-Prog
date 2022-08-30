# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto, - à vista no cartão: 5% de desconto, - em até 2x no cartão:preço normal, - 3x ou mais no cartão: 20% de juros

preçoproduto = float(input("Informe o preço do produto: "))
formadepagamento = float(
    input(
        """
        Informe sua forma de pagamento:
        [ 1 ] à vista dinheiro/cheque
        [ 2 ] à vista cartão
        [ 3 ] 2x no cartão
        [ 4 ] 3x ou mais no cartão
        """
    )
)



def descontodoproduto(preçoproduto, formadepagamento):
    dinheiro_cheque = preçoproduto - (preçoproduto * 10) / 100
    cartao_a_vista = preçoproduto - (preçoproduto * 5) / 100
    juroscartao = preçoproduto + (preçoproduto * 20) / 100

    if formadepagamento == 1:
        print(
            f"Na forma de pagamento cheque/dinheiro você recebeu um desconto de 10% e o produto passou a custar {dinheiro_cheque}"
        )
    elif formadepagamento == 2:
        print(
            f"Na forma de pagamento cartão à vista você recebeu um desconto de 5% e o produto passou a custar {cartao_a_vista}"
        )
    elif formadepagamento == 3:
        parcela = preçoproduto / 2
        print(
            f"Na forma de pagamento até 2x no cartão o produto ira custar 2 parcelas de R${parcela} reais. Totalizando {preçoproduto}"
        )
    elif formadepagamento == 4:
        totalparcela = int(input('Quantas vezes ira parcelar? '))
        parcela = (preçoproduto + juroscartao) / totalparcela 

        print(
            f"Na forma de pagamento parcelado em 3x ou mais no cartão ira ser cobrado um juros de 20% e o produto ira a custar {totalparcela} vezes de R${parcela} reias. Totalizando R${juroscartao} reais"
        )
    else:
        print('\033[0;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!!\033[m')


descontodoproduto(preçoproduto, formadepagamento)
