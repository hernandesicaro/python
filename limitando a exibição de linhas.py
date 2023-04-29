import pandas as pd

#abrindo o arquivo do excel
vendas_df = pd.read_excel("Vendas_Jan.xlsx")
print(vendas_df)

#obs: eu tive que instalar o openpyxl - "pip install openpyxl"

#para saber quantas linhas tem o dataframe
print(vendas_df.index)
#step é 1 por que vai de 1 em 1 - linha por linha

#exibindo o numero de colunas - exibe o nome de todas as colunas do dataframe
print(vendas_df.columns)

#exibindo x primeiras linhas - o head mostra as 5 primeiras
print(vendas_df.head())

#exibindo as x primeiras linhas
print(vendas_df.head(12))

#se quiser printar as ultimas 5 linhas
print(vendas_df.tail())

#ou se quiser printar as ultimas x linhas
print(vendas_df.tail(3))

#printando so determinadas colunas - vc se refere às colunas pelo nome
print(vendas_df["Produto"])

#---------------------------------------------------------------------------
#filtrando a exibição das observações

#aparentemente da pra renomear so assigning assim
vendas = vendas_df

print(vendas.head())

df = vendas

print(df["Vendedor"])
#para dar print em mais de uma coluna tem que colcoar dois colchetes
print(df[["Vendedor", "Total Vendas"]])
print("\n")

#printando um range de linhas
print(df.loc[0:2])
print("\n")

#filtrando as linhas de acordo com uma regra

#primeiro eu crio uma variável que localiza em qual coluna
#de determinado dataframe que ela assume os valores que eu quero
vendas_Leonardo_Almeida_df = df.loc[df["Vendedor"] == "Leonardo Almeida"]

print(vendas_Leonardo_Almeida_df)
print("\n")
#prefiro filtrar assim direto no print
print(df.loc[df["Vendedor"] == "Leonardo Almeida"])

print("\n")
#se eu quiser filtrar e mostrar só uma coluna
print(df.loc[df["Vendedor"] == "Leonardo Almeida", ["Vendedor", "Total Vendas"]])
#dentro do .loc seleciona as colunas que vc quer

print("\n")

#se eu quiser printar apenas o vendedor (coluna) da linha(pelo índice)  4
print(df.loc[4,"Vendedor"]) #é o paulo santos

print("\n")

#método shape mostra a dimensão do dataframe
print(df.shape) #28 linhas e 4 colunas

#para transpor um dataframe
trans = df.T
print(trans)