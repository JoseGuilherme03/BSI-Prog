# Marco André <marcoandre@gmail.com>
# Lista de exercícios de Fixação 5b

# Nessa lista você pode resolver os problemas utilizando o que você preferir:
# if, else, elif, for, while, métodos da lista e string, métodos embutidos no Python.

# Tente usar if ternário e outras formas de resolver com menos linhas de código.

# O objetivo é fixar todo o conteúdo já visto e desenvolver a lógica e o
# raciocínio com problemas novos.


from itertools import count
from operator import index


def comeco_ou_fim_6(nums):
    """
    Verifica se 6 é o primeiro ou último elemento da lista nums.
    comeco_ou_fim_6([1, 2, 6]) -> True
    comeco_ou_fim_6([6, 1, 2, 3]) -> True
    comeco_ou_fim_6([3, 2, 1]) -> False
    """
    return 6 == nums[0] or 6 == nums[-1]


def inicio_fim_igual(nums):
    """
    Retorna True se a lista nums possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    inicio_fim_igual([1, 2, 3]) -> False
    inicio_fim_igual([1, 2, 3, 1]) -> True
    inicio_fim_igual([1, 2, 1]) -> True
    """
    return len(nums) > 0 and nums[0] == nums[-1]


def extremidades_iguais(a, b):
    """
    Dada duas listas a e b verifica se os dois primeiros são
    iguais ou os dois últimos são iguais.
    Suponha que as listas tenham pelo menos um elemento.
    extremidades_iguais([1, 2, 3], [7, 3]) -> True
    extremidades_iguais([1, 2, 3], [7, 3, 2]) -> False
    extremidades_iguais([1, 2, 3], [1, 3]) -> True
    """
    return a[0] == b[0] or a[-1] == b[-1]



def maior_ponta(nums):
    """
    Dada uma lista não vazia, cria uma nova lista onde todos
    os elementos são o maior das duas pontas
    obs.: não é o maior de todos os itens, mas entre as duas pontas
    maior_ponta([1, 2, 3]) -> [3, 3, 3]
    maior_ponta([1, 3, 2]) -> [2, 2, 2]
    """
    new_nums = nums[0] if nums[0] >= nums[-1] else nums[-1]
    return [new_nums for i in nums]


def soma_2_primeiros(nums):
    """
    Dada uma lista de inteiros de qualquer tamanho retorna a soma dos
    dois primeiros elementos.
    Se a lista tiver menos de dois elementos, soma o que for possível.
    """
    return nums[0] + nums[1] if len(nums) >= 2 else sum(nums)

    
    
    
def meio_do_caminho(a, b):
    """
    sejam duas listas de inteiros a e b
    retorna uma lista de tamanho 2 contendo os elementos do
    meio de a e b, suponha que as listas tem tamanho ímpar
    meio_do_caminho([1, 2, 3], [4, 5, 6]) -> [2, 5]
    meio_do_caminho([7, 7, 7], [3, 8, 0]) -> [7, 8]
    meio_do_caminho([5, 2, 9], [1, 4, 5]) -> [2, 4]
    """
    return [a[len(a) // 2] , b[len(b) // 2]]


def numero_invertido(numero):
    """Receba um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321"""
    numero = str(numero)[::-1]
    return int(numero)


def gago(texto):
    """Receba um texto e devolva-o repetindo a primeira letra de cada palavra, junto com um traço
    gago("preciso tirar dez") -> "p-preciso t-tirar d-dez"
    gago("eu deveria ter estudado mais") -> "e-eu d-deveria t-ter e-estudado m-mais"
    """
    texto = texto.split(' ')
    texto_gago = ''
    for palavra in texto:
        texto_gago += f'{palavra[0]}-{palavra} '
    return texto_gago.strip()


def saudacao(nome, hora):
    """Escreva uma saudação para a pessoa, dependendo do horário do dia:
    Entre 5 e 12: dia
    Entre 12 e 18: tarde
    Entre 18 e 5: noite"""
    
    if hora in range(5,12):
        return f'Bom dia {nome}'
    elif hora in range(12,19):
        return f'Boa tarde {nome}'
    else:
        return f'Boa noite {nome}'


def rosquinhas(n):
    """
    Para um inteiro n retorna uma string na forma '<n> rosquinhas'
    onde n é o valor passado como argumento.
    Caso n >= 10 devo retornar 'muitas' em lugar do número.
    rosquinhas(5) -> '5 rosquinhas'
    rosquinhas(23) -> 'muitas rosquinhas'
    """
   
    return f'{str(n)} rosquinhas' if int(n) < 10 else 'muitas rosquinhas'



def pontas(s):
    """
    Dada uma string s, retorna uma string com as duas primeiras e as duas
    últimas letras da string original s
    Assim 'palmeiras' retorna 'paas'
    No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
    """
    return s[0:2] + s[-2:] if len(s) >= 2 else ''
    


def fixa_primeiro(s):
    """
    Dada uma string s, retorna uma string onde todas as ocorrências
    do primeiro caracter são trocados por '*', exceto para o primeiro
    Assim 'abacate' retorna 'ab*c*te'
    Dica: use s.replace(stra, strb)
    """
    palavra = s.replace(s[0],'*')
    return s[0] + palavra[1:]



def nomes_pontas(n):
    """Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    """
    n = n.split()
    n = [n[0],n[-1]]
    return ' '.join(n).upper()


def nomes_pontas_e_iniciais_do_meio(n):
    """Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome,
    e as inciais dos nomes do meio, em maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO A L MENDES"
    """
    n = n.split()
    nome_abreviado = []

    for p, nome in enumerate(n):
        if p == 0 or p == len(n)-1:
            nome_abreviado.append(nome)
        else:
            if nome not in 'dadedo':
                nome_abreviado.append(nome[0])

    return ' '.join(nome_abreviado).upper()

        
        


def mistura2(a, b):
    """
    Sejam duas strings a e b
    Retorno uma string '<a> <b>' separada por um espaço
    com as duas letras trocadas de cada string
      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'
    """
    return b[0:2] + a[2:] + ' ' + a[0:2] + b[2:]




def tres_maiusculas(texto):
    """Encontre a primeira ocorrência de 3 letras maiúsculas consecutivas
    no texto."""
    posicoes = []
    for p,letra in enumerate(texto):
        if letra == letra.upper():
            posicoes.append(p)
    if len(posicoes) >= 3:
        for p in posicoes:
            if texto[p] == texto[p+1] and texto[p] == texto[p+2]:
                return p
    else:
        return None
    


def im_pares_unicos(lista):
    """Separe em listas os impares e pares únicos (não considere duplicidades),
    dos inteiros da 'lista'
    """
    par = []
    impar = []
    for numero in lista:
        if numero not in par and numero % 2 == 0:
            par.append(numero)
        else:
            if numero not in impar and numero % 2 != 0:
                impar.append(numero)
    return par,impar



## Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("comeco_ou_fim_6")
    test(comeco_ou_fim_6([1, 2, 6]), True)
    test(comeco_ou_fim_6([6, 1, 2, 3]), True)
    test(comeco_ou_fim_6([3, 2, 1]), False)
    test(comeco_ou_fim_6([3, 6, 1]), False)
    test(comeco_ou_fim_6([3, 6]), True)
    test(comeco_ou_fim_6([6]), True)
    test(comeco_ou_fim_6([3]), False)

    print("inicio_fim_igual")
    test(inicio_fim_igual([1, 2, 3]), False)
    test(inicio_fim_igual([1, 2, 3, 1]), True)
    test(inicio_fim_igual([1, 2, 1]), True)
    test(inicio_fim_igual([7]), True)
    test(inicio_fim_igual([]), False)
    test(inicio_fim_igual([7, 7]), True)

    print("extremidades_iguais")
    test(extremidades_iguais([1, 2, 3], [7, 3]), True)
    test(extremidades_iguais([1, 2, 3], [7, 3, 2]), False)
    test(extremidades_iguais([1, 2, 3], [1, 3]), True)
    test(extremidades_iguais([1, 2, 3], [1]), True)
    test(extremidades_iguais([1, 2, 3], [2]), False)

    print("maior_ponta")
    test(maior_ponta([1, 2, 3]), [3, 3, 3])
    test(maior_ponta([11, 5, 9]), [11, 11, 11])
    test(maior_ponta([11, 5, 3, 9]), [11, 11, 11, 11])
    test(maior_ponta([2, 11, 3]), [3, 3, 3])
    test(maior_ponta([11, 3, 3]), [11, 11, 11])
    test(maior_ponta([3, 11, 11]), [11, 11, 11])
    test(maior_ponta([2, 2, 2]), [2, 2, 2])
    test(maior_ponta([2, 11, 2]), [2, 2, 2])
    test(maior_ponta([0, 0, 1]), [1, 1, 1])

    print("soma_2_primeiros")
    test(soma_2_primeiros([1, 2, 3]), 3)
    test(soma_2_primeiros([1, 1]), 2)
    test(soma_2_primeiros([1, 1, 1, 1]), 2)
    test(soma_2_primeiros([1, 2]), 3)
    test(soma_2_primeiros([1]), 1)
    test(soma_2_primeiros([]), 0)
    test(soma_2_primeiros([4, 5, 6]), 9)
    test(soma_2_primeiros([4]), 4)

    print("meio_do_caminho")
    test(meio_do_caminho([1, 2, 3], [4, 5, 6]), [2, 5])
    test(meio_do_caminho([7, 7, 7], [3, 8, 0]), [7, 8])
    test(meio_do_caminho([5, 2, 9], [1, 4, 5]), [2, 4])
    test(meio_do_caminho([1, 9, 7], [4, 8, 8]), [9, 8])
    test(meio_do_caminho([1, 2, 3], [3, 1, 4]), [2, 1])
    test(meio_do_caminho([1, 2, 3, 4, 5], [2, 3, 5, 4, 1]), [3, 5])

    print("número invertido")
    test(numero_invertido(1), 1)
    test(numero_invertido(0), 0)
    test(numero_invertido(10), 1)
    test(numero_invertido(1111), 1111)
    test(numero_invertido(00000), 0)
    test(numero_invertido(1234), 4321)
    test(numero_invertido(2013), 3102)
    test(numero_invertido(20130711), 11703102)

    print("Gago")
    test(gago("O"), "O-O")
    test(gago("O O"), "O-O O-O")
    test(gago("Oi"), "O-Oi")
    test(gago("beleza?"), "b-beleza?")
    test(gago("tudo bem?"), "t-tudo b-bem?")
    test(gago("nota dez!"), "n-nota d-dez!")
    test(gago("preciso tirar dez"), "p-preciso t-tirar d-dez")
    test(gago("eu deveria ter estudado mais"), "e-eu d-deveria t-ter e-estudado m-mais")

    print("Saudação")
    test(saudacao("Jorge", 4), "Boa noite Jorge")
    test(saudacao("Jorge", 5), "Bom dia Jorge")
    test(saudacao("Jorge", 11), "Bom dia Jorge")
    test(saudacao("Maria", 12), "Boa tarde Maria")
    test(saudacao("Maria", 18), "Boa tarde Maria")
    test(saudacao("Suzana", 19), "Boa noite Suzana")
    test(saudacao("Suzana", 24), "Boa noite Suzana")
    test(saudacao("Bruna", 2), "Boa noite Bruna")

    print("rosquinhas")
    test(rosquinhas(4), "4 rosquinhas")
    test(rosquinhas(9), "9 rosquinhas")
    test(rosquinhas(10), "muitas rosquinhas")
    test(rosquinhas(99), "muitas rosquinhas")

    print("pontas")
    test(pontas("palmeiras"), "paas")
    test(pontas("algoritmos"), "alos")
    test(pontas("a"), "")
    test(pontas("xyz"), "xyyz")

    print("fixa_primeiro")
    test(fixa_primeiro("abacate"), "ab*c*te")
    test(fixa_primeiro("babble"), "ba**le")
    test(fixa_primeiro("aardvark"), "a*rdv*rk")
    test(fixa_primeiro("google"), "goo*le")
    test(fixa_primeiro("donut"), "donut")

    print("nomes_pontas")
    test(nomes_pontas("Ivo Riegel"), "IVO RIEGEL")
    test(nomes_pontas("Eduardo da Silva"), "EDUARDO SILVA")
    test(nomes_pontas("Fernando José Braz"), "FERNANDO BRAZ")
    test(nomes_pontas("Marco André Lopes Mendes"), "MARCO MENDES")
    test(nomes_pontas("Paulo César de Oliveira"), "PAULO OLIVEIRA")

    print("nomes_pontas_e_iniciais_do_meio")
    test(
        nomes_pontas_e_iniciais_do_meio("Marco André Lopes Mendes"), "MARCO A L MENDES"
    )
    test(nomes_pontas_e_iniciais_do_meio("Li Xing Li Wu"), "LI X L WU")
    test(nomes_pontas_e_iniciais_do_meio("Xing Li Wu Li"), "XING L W LI")
    test(nomes_pontas_e_iniciais_do_meio("Paulo César de Oliveira"), "PAULO C OLIVEIRA")
    test(nomes_pontas_e_iniciais_do_meio("Fernando José Braz"), "FERNANDO J BRAZ")
    test(nomes_pontas_e_iniciais_do_meio("Eduardo da Silva"), "EDUARDO SILVA")
    test(
        nomes_pontas_e_iniciais_do_meio("Jefferson de Oliveira Chaves"),
        "JEFFERSON O CHAVES",
    )

    print("mistura2")
    test(mistura2("mix", "pod"), "pox mid")
    test(mistura2("dog", "dinner"), "dig donner")
    test(mistura2("gnash", "sport"), "spash gnort")
    test(mistura2("pezzy", "firm"), "fizzy perm")

    print("3 maiúsculas")
    test(tres_maiusculas("MMM"), 0)
    test(tres_maiusculas("sKKKsdddfffGGGkkklmn"), 1)
    test(tres_maiusculas("ssdddfffGGGkkklmn"), 8)
    test(tres_maiusculas("ssdddfffgggkkklGGG"), 15)
    test(tres_maiusculas("ssdddfffgggkkklmn"), None)
    test(tres_maiusculas("ssdddfffgggkkklnG"), None)
    test(tres_maiusculas("ssdddfffgggkkklmGG"), None)
    test(tres_maiusculas("sSdDdfffgggKkkklmn"), None)

    print(" Lista de pares e impares únicos:")
    test(
        im_pares_unicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]),
    )
    test(im_pares_unicos([1, 3, 5, 7, 9]), ([], [1, 3, 5, 7, 9]))
    test(im_pares_unicos([2, 4, 6, 8, 10]), ([2, 4, 6, 8, 10], []))
    test(
        im_pares_unicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3]),
        ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]),
    )


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
