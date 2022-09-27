def notas(*num,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['media'] = round(sum(num) / len(num) ,3)
    if sit == True:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados

# PROGRAMA PRINCIPAL
resp = notas(5.5,2.5,10,6.5,sit=True)
print(resp)


