#Recebe uma temperatura em graus Fahrenheit, e retorna a temperatura em graus Celsius


def fahrenheit_para_celsius(fahrnheit):
    conversao = ( fahrnheit - 32) * 5) / 9)
    print(f'\nA temperatura {fahrnheit:.2f}°F corresponde a {conversao:.2f}°C !')


fahrnheit = float(input('informe a temperatura em °F: '))

fahrenheit_para_celsius(fahrnheit)




