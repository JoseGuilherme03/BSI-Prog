#Recebe uma temperatura em graus Celsius, e retorna a temperatura em graus Fahrenheit.


def celsius_para_fahrenheit(celsius):
    conversao = (celsius * 1.8) + 32
    print(f'\nA temperatura {celsius}°C corresponde a {conversao}°F !')

celsius = float(input('\ninforme a temperatura em °C: '))

celsius_para_fahrenheit(celsius)



