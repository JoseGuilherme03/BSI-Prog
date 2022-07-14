import math

x = float(input('digite o cateto oposto: '))
y = float(input('digite o cateto adjascente: '))

hipo = math.hypot (x,y)

#print(f'o comprimento da hipotenusa é {math.sqrt (hipo):.2f}')
print(f'O comprimento da hipotenusa é {hipo:.2f}')
