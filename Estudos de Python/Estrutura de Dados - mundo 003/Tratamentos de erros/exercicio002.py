import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site pudim não está acessível no momento.')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso\033[m')
