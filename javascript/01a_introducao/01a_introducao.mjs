

// Lista de exercícios 1 - variáveis e operadores

export function somaInteiros(a, b) {
    /*
    Recebe dois números inteiros, e retorna a sua soma.

    Argumentos:
        a (número): 1o valor
        b (número): 2o valor

    Retorna:
        número: a soma dos dois valores.
    */
   return a + b
}


export function metrosParaMilimetros(metros) {
    /*
    Recebe um valor em metros, e retorna o valor em milímetros,
        sabendo que 1 metro equivale a 1000 milimetros.

    Argumento:
        metros (número): um valor em metros

    Retorna:
        número: o valor convertido para milimetros.
    */
   return metros * 1000
}


export function tempoParaPercorrerUmaDistancia(distancia, velocidade) {
    /*
    Recebe uma distância e a velocidade de movimentação, e retorna
        as horas que seriam gastas para percorrer em linha reta.

    Argumentos:
        distancia (número): a distância, em kilômetros.
        velocidade (número): a velocidade, em kilômetros por hora.

    Retorna:
        número: o tempo, em horas.
    */
   return (distancia / velocidade).toFixed(2)
}

export function aumentoSalarial(salario, porcentagem) {
    /*
    Recebe um salário e sua porcentagem de aumento, e retorna
        o novo salário.

    Argumentos:
        salario (número): o salário original.
        porcentagem (número): o percentual de aumento, entre 0 e 100.

    Retorna:
        número: o novo salário, com duas casas decimais.
    */
   var novo_salario = ((salario * porcentagem) / 100) + salario
   return novo_salario.toFixed(2)

}

export function precoComDesconto(precoOriginal, percentualDesconto) {
    /*
    Recebe um preço e sua porcentagem de desconto, e retorna
        o novo preço.

    Argumentos:
        precoOriginal (número): o preco original do produto.
        percentualDesconto (número): o percentual de desconto, entre 0 e 100.

    Retorna:
        número: o preço final, após o desconto, com duas casas decimais.
    */
   var novo_preco = precoOriginal - ((precoOriginal * percentualDesconto) / 100) 
   return novo_preco.toFixed(2)
}

export function diasParaSegundos(dias, horas, minutos, segundos) {
    /*
    Recebe uma data em dias com horas, minutos e segundos, e retorna
    a data em segundos.

    Argumentos:
        dias (número): a quantidade de dias.
        horas (número): a quantidade de horas.
        minutos (número): a quantidade de minutos.
        segundos (número): a quantidade de segundos.

    Retorna:
        número: a quantidade de segundos equivalente aos valores de dias, horas, minutos e segundos.
    */
   var dias_s = dias * 24 * 60 * 60
   var horas_s = horas * 60 * 60
   var minutos_s = minutos * 60
   return dias_s + horas_s + minutos_s + segundos
}

export function celsiusParaFahrenheit(celsius) {
    /*
    Recebe uma temperatura em graus Celsius, e retorna a temperatura
        em graus Fahrenheit.

    Argumento:
        celsius (número): a temperatura em graus Celsius.

    Retorna:
        número: a temperatura em graus Farenheit.

    */
   return (celsius * 9/5) + 32
}

export function fahrenheitParaCelsius(fahrenheit) {
    /*
    Recebe uma temperatura em graus Fahrenheit, e retorna a temperatura
        em graus Celsius.

    Argumento:
        farenheit (número): a temperatura em graus Fahrenheit.

    Retorna:
        número: a temperatura em graus Celsius.
    */
   return ((fahrenheit - 32) * (5/9)).toFixed(2)
}

export function precoAluguelCarro(dias, km) {
    /*
    Recebe uma quantidade de dias que o carro foi alugado e a
        quantidade de quilômetros rodados, e retorna o valor a ser pago.
        1 dia: 60 reais mais R$ 0,15 por km rodado.

    Argumentos:
        dias (número): quantidade de dias que o carro foi alugado.
        km (número): quantos quilômetros o carro rodou.

    Retorna:
        número: o preço do aluguel do carro, com 2 casas decimais,
                conforme a fórmula dada no enunciado.
    */
   var aluguel = (dias * 60) + (km * 0.15)
   return aluguel.toFixed(2)
}

export function diasPerdidosPorFumar(cigarrosFumadosPorDia, anosFumando) {
    /*
    Recebe uma quantidade de cigarros fumados por dia e a quantidade
        de anos que fuma, e retorna o total de dias perdidos, sabendo que
        cada cigarro reduz a vida em 10 minutos.

    Argumentos:
        cigarrosFumadosPorDia (número): a quantidade de cigarros fumados por dia.
        anosFumando (número): a quantidade de anos que a pessoa fumou.

    Retorna:
        número: a quantidade de dias que a pessoa perdeu por fumar.
    */
   var total_cigarro = cigarrosFumadosPorDia * (anosFumando * 365)
   var tempo_perdido = (total_cigarro * 10) / 1440
   return tempo_perdido.toFixed(2)

}

export function doisElevadoADez() {
    /*
    Calcula dois elevado a um milhão, e retorna a quantidade de
    algarismos.

    Retorna:
        número: a quantidade de algarismos que o resultado contém.
    */
   return String(2 ** 10).length
}

export function mediaFinalAprovadoReprovado(p1, p2, ep1, ep2) {
    /*
    Recebe as notas das 2 provas e 2 exercícios de programação e retorna
        se o aluno foi ou não aprovado. As provas têm peso 7 e os exercícios
        têm peso 3. Cada parcial tem peso igual.
        Uma forma de resolver é calcular a 1a parcial, com a média ponderada entre
        p1 e ep1, depois calcular a 2a parcial, com as notas de p2 e ep2 e depois
        calcular a média aritmética entre a 1a e a 2a parcial.

    Argumentos:
        p1 (número): a nota da primeira prova.
        p2 (número): a nota da segunda prova.
        ep1 (número): a nota do 1o exercício.
        ep2 (número): a nota do 2o exercício.

    Retorna:
        bool: True ou False, dependendo da média ser maior ou igual a 7 ou não.

    */
   var media1 = (p1 * 7) + (ep1 * 3) / 10
   var media2 = (p2 * 7) + (ep2 * 3) / 10
   return (media1 + media2) / 2 >= 7
}

export function salarioLiquido(valorHora, horasMensais) {
    /*
    Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.

    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto.

    Argumentos:
        valorHora (número): o valor hora pago ao funcionário.
        horasMensais (número): a quantidade de horas trabalhadas no mes.

    Retorna:
        número: o salário líquido, após todos os descontos.
    */
   var salario  = valorHora * horasMensais
   var inss = (salario * 8) / 100
   var ir = (salario * 11) / 100
   var sindicato = (salario * 5) / 100
   return salario - (inss + ir + sindicato)

}

export function duziasOvos(ovos) {
    /*
    Receba o número de ovos e devolva a quantidade de dúzias
        correspondente. Considere sempre dúzias cheias, arredondando pra
        cima se necessário.

    Argumento:
        ovos (número): a quantidade de ovos.

    Retorna:
        número: a quantidade de dúzias correspondente à quantidade de ovos,
            arredondado pra cima.
    */
   return Math.ceil(ovos / 12)
}

export function latasTinta(metrosPintar) {
    /*
    Recebe quantos metros quadrados precisa pintar,
        e retorna a quantidade de latas de tinta a comprar.
        A cobertura da tinta é de 3 metros por litro de tinta.
        Cada lata possui 18 litros de tinta.

    Argumento:
        metrosPintar (número): a quantidade de metros quadrados a pintar.

    Retorna:
        número: a quantidade de latas de tinta, arredondado pra cima.
    */
   return Math.ceil(metrosPintar / 54)
}

export function decomporNumero(numero) {
    /*
    Leia um número inteiro menor que 1000 e devolva a quantidade de
        centenas, dezenas e unidades do mesmo.
        Obs.: não utilize operações com strings.

    Argumento:
        numero (número): um número menor que 1000.

    Retorna:
        tupla de inteiros, com as centenas, dezenas e unidades do numero.
    */
   var centenas = Math.floor(numero / 100) % 10
   var dezenas = Math.floor(numero / 10) % 10
   var unidades = Math.floor(numero / 1) % 10
   return [centenas,dezenas,unidades]
}

export function mediaPonderada(prova, trabalho, exercicio) {
    /*
    Calcule a média ponderada, sabendo que os pesos são os seguintes:
    - prova: peso 7
    - trabalho: peso 2
    - exercício : peso 1

    Dica: eliminar os números mágicos.

    Argumentos:
        prova (float): nota de uma prova, entre 0 e 10.
        trabalho (float): nota do trabalho, entre 0 e 10.
        exercicio (float): nota do exercício, entre 0 e 10.

    Retorna:
        float: média ponderada das notas, com 1 casa decimal
    */
   return (prova * 7 + trabalho * 2 + exercicio) / 10
}

export function aluguelAirBnB(valorDiaria, dias) {
    /*
    Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 75,00 para limpeza e 5% de taxa de administração sobre o valor
    do aluguel, sem a taxa de limpeza

    Argumentos:
        valor_diaria (float): o valor da diária
        dias (int): a quantidade de dias de hospedagem

    Retorna:
        float: o valor do aluguel, com duas casas decimais
    */
   var total = valorDiaria * dias
   var taxa_adm = total * 5 / 100
   return (total + taxa_adm + 75).toFixed(2)
}
