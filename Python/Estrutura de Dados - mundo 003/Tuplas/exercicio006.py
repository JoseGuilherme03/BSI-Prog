palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)


for p in palavras:
    print(f"\n\nNa palavra {p.upper()} temos as vogais ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
