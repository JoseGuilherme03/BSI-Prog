import pandas as pd
import plotly.express as px


# Passo 1: Importar a base de dados
tabela = pd.read_csv('telecom_users.csv')


# Passo 2: Visualizar a base de dados
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados
tabela = tabela.drop('Unnamed: 0',axis='columns')
tabela = tabela.drop('IDCliente',axis='columns')
print(tabela)

# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'],errors='coerce')


# - Valores vazios
# deletando as colunas  vazias
tabela = tabela.dropna(how='all',axis='columns')
# deletando as linhas vazias
tabela = tabela.dropna(how='any', axis='index')


# Passo 4: Análise Inicial
# Como estão os cancelamentos
print(tabela['Churn'].value_counts())
print('')
# Porcentagem formatada em relação ao valor total
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))


# Passo 5: Análise Mais completa

# Criar Gráfico
# mostrar grafico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
