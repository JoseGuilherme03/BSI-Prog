# Recebe uma distância e a velocidade de movimentação, e retorna as horas que seriam gastas para percorrer em linha reta


def tempo_para_percorrer_uma_distancia(velocidade, distancia):
    tempo = velocidade / distancia
    print(
        f"Para percorrer uma distância de {distancia}km numa velocidade de {velocidade}km/h você levara {tempo}hrs"
    )


velocidade = float(input("Digite a sua velocidade: "))
distancia = float(input("Digite a distância a ser percorrida: "))

tempo_para_percorrer_uma_distancia(velocidade, distancia)

