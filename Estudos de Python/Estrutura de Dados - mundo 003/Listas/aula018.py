dados = [['jose',18],['Isaak',22],['Gabriel',19],['João',18]]
mai = men = 0
for c in dados:
    print(f'O nome do candidado {c[0]} e ele tem {c[1]} anos')

print('-=' * 30)
for p in dados:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        mai += 1
    else:
        print(f'{p[0]} é menor de idade')
        men += 1
print('-=' * 30)

print(f'Ao total temos {mai} pessoas maiores de idade')
print(f'Ao total temos {men} pessoas menores de idade')



