numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: ")),
)

print(f"Você digitou os valores {numeros}")
if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3) +1}° posição")
else:
    print("O valor 3 não foi digitado")
print(f"O número 9 apareceu {numeros.count(9)} vezes")
print(f"Os valores par foram: ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=",")
