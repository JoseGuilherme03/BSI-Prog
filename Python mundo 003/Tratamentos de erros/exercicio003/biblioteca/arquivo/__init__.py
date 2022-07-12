from biblioteca.interfacee import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO!! na criação do arquivo\033[m')
    else:
        print(f'\033[33mArquivo {nome} criado com sucesso!!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('\033[31mERRO ao ler o arquivo\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar (arq,nome='<desconhecido>',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('\033[31mHOUVE UM ERRO, ao tentar abrir o arquivo\033[m')
    else:
        try:
            for nome,idade in zip(nome,idade):
                a.write(f'{nome};{idade}\n')
        except:
            print('HOUVE UM ERRO!! na hora de escrever os dados!')
        else:
            a.close()


def limpar(nome):
    try:
        a = open(nome,'r+')
    except:
        print('HOUVE UM ERRO!! ao tentar abrir o arquivo')
    else:
        a.truncate(0)
        print(f'O arquivo {nome} está limpo')
    finally:
        a.close()
    
