#EXERCÍCIO - FINAL CURSO

import pandas as pd


# 1 - Após carregar os dados, deixe somente as colunas de Vendedor e Total Vendas
# 2 - Com o groupby use a coluna de vendedor para criar um resumo do vendedor e a soma total das vendas
# 3 - Salve o dataFrame como um arquivo de Excel csv

data = pd.read_excel("exercicio.xlsx")
print(data.shape, type(data))


data=data.drop(columns=["Produto", "Data Venda"])
print(data)

data=data.groupby(["Vendedor"]).sum()
print(data)

data.to_csv(path_or_buf="out.csv")

#-------------------------------------------------
#teste com datas

data1=pd.read_excel("exercicio.xlsx")

data1=data1.groupby(["Data Venda"]).sum()
#nao tive problema aqui
print(data1)


#pode ser que haja problema com o csv direto, que pode vir com a coluna
#numérica como texto, para isso, poderíamos usar
#o str replace e o astype float

# deletarDuasColunas["Total Vendas"] = deletarDuasColunas["Total Vendas"].str.replace(",", ".")
#
# #Convertendo a coluna de Total Vendas de Texo para Float
# deletarDuasColunas["Total Vendas"] = deletarDuasColunas["Total Vendas"].astype(float)
