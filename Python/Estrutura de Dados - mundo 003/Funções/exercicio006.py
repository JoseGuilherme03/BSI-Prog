
def voto(nascimento):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos:  VOTO OBRIGATÓRIO'
    elif idade < 18 and  idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL' 


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))


    
