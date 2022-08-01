'''
Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

E-mail da diretoria: seugmail+diretoria@gmail.com
Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

Comandos pyautogui: https://pyautogui.readthedocs.io/en/latest/quickstart.html
'''


import pyautogui as py
import webbrowser
from time import sleep
import pyperclip
import pandas as pd


py.PAUSE = 1


# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
webbrowser.open('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga') # Entra no link
sleep(5)


# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
py.click(x=484, y=319)
py.press('enter')
sleep(2)


# Passo 3: Fazer o download do relatório
py.click(x=1027, y=308, button='right')
py.click(x=1203, y=825)
sleep(5)


# Passo 4: Calcular os indicadores
planilha = pd.read_excel('/home/jose/Downloads/Vendas - Dez.xlsx') # Localiza e lê a planilha
faturamento = planilha['Valor Final'].sum() #Soma a coluna desejada
quantidade = planilha['Quantidade'].sum() #Soma a coluna desejada


# Passo 5: Entrar no email
webbrowser.open('https://mail.google.com/mail/u/0/?ogbl#inbox')
sleep(3)


# Passo 6: Enviar por e-mail o resultado
py.click(x=51, y=222)
py.write('jg8229074@gmail.com')
py.press('tab') # seleciona o e-mail
py.press('tab') # pula pro assunto
py.write('Relatorio de Vendas')
py.press('tab')
texto = f'''
    Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Jose Guilherme.
'''
py.write(texto)
py.hotkey('ctrl','enter')
