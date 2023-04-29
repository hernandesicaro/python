import pandas as pd

sellers = pd.read_excel("merge/sellers.xlsx")
prod = pd.read_excel("merge/products.xlsx")
sales = pd.read_excel("merge/sales.xlsx")


print(sellers.shape)
print(type(sellers))
print("\n")

print(prod.shape)
print(type(prod))
print("\n")

print(sales.shape)
print(type(sales))
print("\n")

#-------------------------------------------------

#vamos dar o merge entre os vendedores e as vendas
#a planilha de vendedores tem as metas
#e a planilha de vendas tem as vendas realizadas

data1 = sales.merge(sellers)
print(data1)
print("\n")

#no pandas o .merge acha a key variable automaticamente - imagino que pelo nome
#diferente do stata que temos que declarar em qual variável que queremos o merge
#stata -> merge m:m "key variable" using "example.dta"

data2 = sales.merge(prod)
print(data2)
print("\n")

print(data2.columns)
print(data2.shape)
print("\n")

#-----------------------------------------------
#
# resumo = data2[["Vendedor", "Produto", "Total Vendas"]]
# print(resumo)
