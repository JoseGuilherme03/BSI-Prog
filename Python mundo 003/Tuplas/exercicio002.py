


times = (
    "Corinthians",
    "Palmeiras",
    "Santos",
    "Grêmio",
    "Cruzeiro",
    "Flamengo",
    "Vasco",
    "Chapecoense",
    "Atlético",
    "Botafogo",
    "Atlético PR",
    "Bahia",
    "São Paulo",
    "Fluminese",
    "Sport Recife",
    "EC Vitória",
    "Coritiba",
    "Avaí",
    "Ponte Preta",
    "Atlético-GO",
)

print("-=" * 20)
print(f"Lista de times do Brasileirão: {times}")
print("-=" * 20)
print(f"Os 5 primeiros são: {times[:5]}")
print("-=" * 20)
print(f"Os 4 últimos são: {times[-4:]}")
print("-=" * 20)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 20)
print(f'Em que posicão está a Chapecoense: {times.index("Chapecoense") + 1}° posição')

