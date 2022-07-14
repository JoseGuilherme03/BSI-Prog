x = int(input('digite um valor em metros'))
km = x / 1000
hm = x / 100
dam = x / 10
dm = x * 10
cm = x * 100
mm = x * 1000

print(f'''a medida de {x} corresponde a:
\n{km}
\n{hm}
\n{dam}
\n{dm}
\n{cm}
\n{mm}
''')

