from biblioteca.interfacee import *
from biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Limpar dados Cadastrados','Sair do Sistema'])

    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        # Opção para cadastrar pessoas
        cabeçalho('NOVO CADASTRO')
        resp = ' '
        nome = []
        idade = []
        while resp not in 'Nn':
            nome.append(str(input('Nome: ')).strip())
            idade.append(leiaint('Idade: '))
            resp = str(input('Quer continuar? [S/N] '))
        cadastrar(arq,nome,idade)
    elif resp == 3:
        # Opção que limpa os dados cadastrados no arquivo
        limpar(arq)
    elif resp == 4:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO!! Digite uma opção válida!\033[m')
    sleep(2)
