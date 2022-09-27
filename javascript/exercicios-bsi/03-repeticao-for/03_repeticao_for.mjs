// Lista de exercícios - Estruturas de repetição For

// ATENÇÃO !!!
// Todos os exercícios devem ser resolvidos com "for". Não utilize while ou funções prontas.
// Utilize "for (const item of array)" para acessar os itens do array.
// Utilize "for (const [i, item] of array.entries()) para acessar os índices e elementos do array.
// Utilize "for (const item in objeto)" acessar os índices do array.
// Uitlize "for (let i = 0; i < n; i++)" nas demais situações.

export function soma(lista) {
    /*
    Retorna a soma dos elementos de uma lista.

    Argumentos:
        lista (lista de floats): Uma lista de valores float.

    Retorna:
        float: a soma dos elementos da lista.
    */
   var soma = 0
   for (let num of lista){
    soma += num
   }
   return soma
}

export function media(lista) {
    /*
    Retorna a média das elementos da lista.

    Argumento:
        lista (array): uma lista de elementos (float).

    Retorna:
        float: a média das elementos.
     */
    return soma(lista) / lista.length
    
}

export function mediaSaltosLista(saltos) {
    /*
    Receba uma lista com os saltos de um atleta e calcule a média \n
        dos seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.

    Argumento:
        saltos (array): uma lista com os saltos (float) de um atleta.

    Retorna:
        float: a média dos saltos, de acordo com o enunciado.
    */
    var mai = Math.max(...saltos)
    var men = Math.min(...saltos)
    var soma = 0
    var tam = (saltos.length) - 2
    for(var s of saltos){
        soma += s
    }
    return (soma - (mai + men)) / tam
}
     

export function trocaCaixa(texto) {
    /*
    Vogais ficam em caixa alta (maiúsculas). \n
        Consoantes ficam em caixa baixa (minúsculas).

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        string: o texto convertido, conforme o enunciado.
    */
   var novo_texto = ''
   var vogais = ['a','e','i','o','u','A','E','I','O','U']
   for (var letra of texto){
    if (vogais.includes(letra)){
        novo_texto += letra.toUpperCase()
    }else{
        novo_texto += letra.toLowerCase()
    }
   }
   return novo_texto
}

export function leet(texto) {
    /*
    Converte texto em leet. Veja os testes para exemplos.
    Dicionário para usar na conversão:
        troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        string: o texto convertido, conforme o enunciado.
    */
   
    var troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}
    var novo_texto = ''
    for (var letra of texto){
        if (letra.toLowerCase() in troca){
            novo_texto += troca[letra.toLowerCase()]
        }else{
            novo_texto += letra
        }
    }
    return novo_texto
}

export function quantidadeImpares(inicio, fim) {
    /*
    Determine a quantidade de números ímpares num intervalo, excluindo os valores limite do intervalo.

    Argumentos:
        inicio (int): o limite inferior do intervalo, excluindo-o;
        fim (int): o limite superior do intervalo, excluindo-o;

    Retorna:
        int: a quantidade de números dentro do intervalo dado.
    */
    var cont = 0
    for (var i = inicio + 1; i < fim; i++){
        if (i % 2 != 0){
            cont ++
        }
    }
    return cont
}
export function somaInteiros(inicio, fim) {
    /*
    Calcule a soma dos números inteiros no intervalo dado.
    Considere que os limites do intervalo podem ser informados
    como números negativos ou fora de ordem e você terá que tratar isso.
    Ex: 1 e 5 ou 5 e 1, retorna 9

    Argumentos:
        inicio (int): um dos limite do intervalo, incluindo-o;
        fim (int): o outro limite do intervalo, incluindo-o;

    Retorna:
        float: a soma dos valores dentro do intervalo dado.
    */
    if (inicio < fim){
        for (var soma = 0;inicio <= fim; inicio ++){
        soma += inicio
        }
    }else{
        for (var soma = 0;fim <= inicio; fim ++){
            soma += fim
        }
    }   
    return soma

}

export function serie(n) {
    /*
    Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    Argumento:
        n (int): o valor final da série;

    Retorna:
        float: a soma dos valores da série, segundo a fórmula e o valor de n informados.

    */
   var soma = 1
   for (var cont = 2;cont <= n;cont ++){
        soma += 1/cont
   }
   return Number(soma.toFixed(2))
}

export function inverteOrdemElementos(lista) {
    /*
    Inverta a ordem dos elementos da lista.

    Argumento:
        lista (array): uma lista de elementos, independente de tipo.

    Retorna:
        array: uma lista com os elementos em ordem inversa.
    */
    var lista_invertida = []
    for (var i = lista.length;i >= 0; i--){
        lista_invertida.push(lista[i])
    }
    return lista_invertida

}

export function intercalaListas(lista1, lista2) {
    /*
    Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    Intercalar significa que a nova lista terá o 1o elemento da 1a lista,
    seguido do 1o elemento da 2a lista, seguido do 2o elemento da 1o lista,
    seguido do 2o elemento da 2a lista e assim por diante.

    Argumentos:
        lista1 (array): uma lista de elementos, independente de tipo;
        lista2 (array): uma lista de elementos, independente de tipo;

    Retorna:
        array: uma lista com os elementos intercalados das duas listas recebidas.
    */
    var lista_intercalada = []
    for (var i = 0;i <= lista1.length; i++){
        lista_intercalada.push(lista1[i])
        lista_intercalada.push(lista2[i])
    }
    return lista_intercalada

}

export function separaParesImpares(lista) {
    /*
    Separe em listas os pares e ímpares, dos inteiros da lista recebida.

    Argumento:
        lista (lista de inteiros): uma lista de elementos int;

    Retorna:
        uma tupla com duas listas de inteiros sendo a primeira uma lista com os pares
        e a segunda uma ista com os ímpares.
    */
   var par = []
   var impar = []
   for (var i of lista){
    if (i % 2 == 0){
        par.push(i)
    }else{
        impar.push(i)
    }
   }
   return [par,impar]
}
export function maiorMenor(lista) {
    /*
    Calcule o maior e o menor número da lista recebida.

    Argumento:
        lista (array): uma lista de elementos float;

    Retorna:
        uma tupla com dois números inteiros, o maior e o menor da lista.
    */
   var maior = 0
   var menor = 0
   var cont = 0
   for(var i of lista){
    if (cont == 0){
        maior = i
        menor =  i
    }
    if (i > maior){
        maior = i
    }
    if (i < menor){
        menor = i
    }
    cont ++
   }
   return [maior,menor]
}

export function darTroco(valorAPagar, valorEmDinheiro) {
    /*
    Calcule o troco a devolver ao cliente com notas de 1,2,5,10,20,50.
        A resposta deve conter a quantidade de cada nota, sem considerar centavos.

    Argumentos:
        valorAPagar (float): o valor da conta
        valorEmDinheiro (float): o valor que foi dado para pagar a conta.

    Retorna:
        uma lista de uma tuplas, onde cada dupla contém dois valores:
        o valor da nota e a quantidade daquela nota.
        Se a quantidade de notas for igual a zero, não deve aparecer na lista.
    */
    var troco = valorEmDinheiro - valorAPagar
    var notas = [50,20,10,5,2,1]
    var lista = []
    for (var i of notas){
        if (troco >= i){
            var quantidade = Math.floor(troco/i)
            lista.push([i,quantidade])
            troco -= (i * quantidade)
        }
    }
    return lista
   

}

export function mesesAcimaMediaAnual(temperaturas) {
    /*
    Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses
    que possuem temperatura superior á média anual.

    Argumentos:
        temperaturas (lista de floats): as temperaturas médias de cada mês no ano, em ordem.

    Retorna:
        lista de inteiros: uma lista com o número correspondente ao mês em que a
        temperatura média foi maior que a temperatura média anual.
    */
   var lista = []
   var cont = 0
   var media_anual = media(temperaturas)
   for (var i of temperaturas){
    if (i > media_anual){
        lista.push(cont)
    }
    cont ++
   }
   return lista
}

export function maiores13(idades, alturas) {
    /*
    Receba as idades e alturas de diversas pessoas, em duas
        listas separadas e de igual comprimento.
        Calcule a media das alturas e retorne as alturas daqueles que
        possuem 'idades' maior que 13 e altura inferior a media da turma.

    Argumentos:
        idades (lista de inteiros): Uma lista de idades;
        alturas (lista de floats): uma lista de alturas;

    Retorna:
        uma lista de alturas dos alunos, conforme o criério definido.
    */
   var lista = []
   var posicao = 0
   var media_altura = media(alturas)
   for (var i of idades){
    if (i > 13 && alturas[posicao] < media_altura){
        lista.push(alturas[posicao])
    }
    posicao ++
   }
   return lista
}

export function testaPrimo(numero) {
    /*
    Verifique se o valor informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1.

    Argumento:
        numero (int): um número inteiro.

    Retorna:
        bool: true ou false, se o valor e ou não primo.
    */
   var primo = 0
   for (var cont = 1;cont <= numero ; cont ++){
    numero % cont == 0 ? primo ++:primo += 0
   }
   return primo == 2
}

export function listaDePrimos(inicio, fim) {
    /*
    Retorne uma lista de primos entre os valores informados, incluindo
    os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    */
   for (var lista = [];inicio <= fim; inicio ++){
    if (testaPrimo(inicio)){
        lista.push(inicio)
    }
   }
   return lista
}

export function fibonacci(n) {
    /*
    Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...

    Argumento:
        n (int): a quantidade de elementos que serão gerados.

    Retorna:
        uma lista de elementos inteiros correspondendo aos n primeiros elementos da série
        de Fibonacci.
    */
   var n1 = 0
   var n2 = 1
   var resultados = []
   for (var cont = 0 ;cont < n;cont ++){
    var n3 = n1 + n2
    n1 = n2
    n2 = n3
    resultados.push(n1)
   }
   return resultados
}

export function altera_salarios(salarios) {
    /*
    Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00

    Argumento:
        salarios (lista de floats): os salários originais.

    Retorna:
        uma lista de elementos float, correspondendo aos salários corrigidos.
    */
   var porcentagem =  0
   var lista = []
   var salario_minimo = 724
   for (var s of salarios){
        if (s <= salario_minimo  ){
            porcentagem = 20

        }else if (s <= salario_minimo * 2){
            porcentagem = 15

        }else if (s <= salario_minimo * 5){
            porcentagem = 10

        }else{
            porcentagem = 5
        }
        var aumento = s + ((s * porcentagem) / 100)
        lista.push(aumento)   
    }
    return lista
}
