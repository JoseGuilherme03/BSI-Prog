// Lista de exercícios - Estruturas de repetição while

// ATENÇÃO !!!
// Todos os exercícios devem ser resolvidos com "while".
// Não utilize "for", métodos das estruturas de dados ou funções embutidas.

export function quantidadeImpares(inicio, fim) {
    /*
    Determine a quantidade de números ímpares num intervalo.

    Argumentos:
        inicio (int): o limite inferior do intervalo;
        fim (int): o limite superior do intervalo;

    Retorna:
        int: a quantidade de números ímpares no intervalo.
    */
    inicio ++
    var impar = 0
    while (inicio < fim){
        if (inicio % 2 != 0){
            impar ++
        } 
        inicio ++
    }
    return impar
}

export function somaInteiros(inicio, fim) {
    /*
    Calcule a soma dos números inteiros no intervalo dado.
    Considere que os limites do intervalo podem ser informados
    como números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9

    Argumentos:
        inicio (int): um dos limite do intervalo, excluindo-o;
        fim (int): o outro limite do intervalo, excluindo-o;

    Retorna:
        float: a soma dos valores dentro do intervalo dado.
    */
    var soma = 0
    if (inicio > fim){
        var aux = inicio
        inicio = fim
        fim = aux
    }
    inicio ++
    while (inicio < fim){
        soma += inicio
        inicio ++
    }
    return soma
    
    
   
}

export function potencia(base, expoente) {
    /*
    Calcule a base elevada ao expoente manualmente.
    Não utilize coisas como:'base ** expoente' ou a função Math.pow().

    Argumentos:
        base (int): o valor base;
        expoente (int): o expoente;

    Retorna:
        int: o resultado de base elevado ao expoente.
    */
   var soma = 1
   var cont = 1
   while (cont <= expoente){
    soma *= base
    cont ++
   }
   return soma
}

export function crescimentoPopulacional(
    populacao1,
    populacao2,
    crescimento1,
    crescimento2
) {
    /*
    Calcule quantos anos levará para a 'população1'
    ultrapassar a 'população2', baseado em suas porcentagens de crescimento.

    Argumentos:
        populacao1 (int): a população da 1a cidade;
        populacao2 (int): a população da 2a cidade;
        crescimento1 (float): o percentual de crescimento anual da população da 1a cidade;
        crescimento2 (float): o percentual de crescimento anual da população da 1a cidade;

    Retorna:
        int: a quantidade de anos que levará para a população da cidade 1 utrapassar a população da cidade 2.
    */

    
    var anos = 0
      
    if (populacao1 > populacao2 || crescimento1 < crescimento2){
           return 0
        }
    else{
        while (populacao2 > populacao1){
                populacao1 += (populacao1 * crescimento1) / 100
                populacao2 += (populacao2 * crescimento2) / 100
                anos ++
        }
    }
    return anos
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
   var lista = []
   var n1 = 0
   var n2 = 1
   while (n > 0){
        var n3 = n1 + n2
        n1 = n2
        n2 = n3
        lista.push(n1)
        n --
   }
   return lista

}

export function fatorial(numero) {
    /*
    Calcule e retorne o fatorial do numero informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é: 4 * 3 * 2 * 1 e retorna 24.

    Argumento:
        numero (int): o número do qual se quer calcular o fatorial.

    Retorna:
        int: o fatorial de numero.
    */
    var cont = numero 
    var soma = 1
    while(cont != 0){
        soma *= numero
        numero --
        cont --
    }
    return soma
}

export function éPrimo(valor) {
    /*
    Verifique se o valor informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1.

    Argumento:
        valor (int): um número inteiro.

    Retorna:
        bool: true ou false, se o valor e ou não primo.
    */
   var res = 0
   var cont = 0
   while (cont <= valor){
        if (valor % cont == 0){
            res ++
        }
        cont ++
   }
   return res == 2
}

export function quantidadePrimos(inicio, fim) {
    /*
    Retorne a quantidade de primos entre os valores informados, 
        incluindo os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        int: a quantidade de números primos dentro do intervalo especificado.
    */
   var res = 0
   while (inicio <= fim){
    if (éPrimo(inicio)){
        res ++
    }
    inicio ++
   }
   return res
}

export function listaPrimos(inicio, fim) {
    /*
    Retorne uma lista de primos entre os valores informados, 
        incluindo os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    */
   var lista = []
   while (inicio <= fim){
        if (éPrimo(inicio)){
            lista.push(inicio)
        }
        inicio ++
   }
   return lista
}

export function serie1(n) {
    /*
    Dado n, calcule o valor de:
        s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    Argumento:
        n (int): o valor final da série;

    Retorna:
        float: a soma dos valores da série, segundo a fórmula e o valor de n informados.

    */
   var divisior = 1
   var cont = 2
   var soma  = 1
   while (cont <= n){
        soma += divisior / cont
        cont ++
   }
   return Number(soma.toFixed(2))

}

export function serie2(n) {
    /*
    Dado n, calcule o valor de:
        s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

    Argumento:
        n (int): o valor final da série;

    Retorna:
        float: a soma dos valores da série, segundo a fórmula e o valor de n informados.
    */
    var cont = 1
    var m = 1
    var soma = 0
    while (cont <= n){
    soma += cont/m
    m += 2
    cont ++ 
    }
    return Number(soma.toFixed(2))
}


export function seriePi(n) {
    /*
    Calcule o valor de pi através da série:
        4/1 - 4/3 + 4/5 - 4/7 + ... - 4/m, sendo informado
        o número n de iterações.

    Argumento:
        n (int): o valor final da série;

    Retorna:
        float: o valor de pi calculado.
    */


    var divisor = 1
    var num = 4
    var soma = 0
    var cont = 0
    while (cont < n){
        if (cont % 2 != 0){
            soma -= num / divisor
        }
        else{
            soma += num / divisor
        }
        divisor += 2
        cont ++
    }
    return Number(soma.toFixed(6))
}
