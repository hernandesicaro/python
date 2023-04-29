import pandas as pd

data = pd.read_excel("ordenar.xlsx")
print(data)
print(type(data))
print(data.shape)

print("\n")
#ordenando a coluna de vendedores A-Z
#o by é a coluna que queremos fazer o sort
data1 = data.sort_values(by="Vendedor")
print(data1)
print("\n")

#podemos ordenar qualquer coluna pelo by
print("\n")
#ordenando a coluna de produto
data2 = data.sort_values(by="Produto")
print(data2)
#mas desordena a coluna do vendedor
print("\n")


print("\n")
data3 = data.sort_values(by="Total Vendas")
print(data3)
#aqui ordenamos de menor para maior
#para ordenar os valores numéricos não precisa mudar o comando, o sort values by funciona igual
print("\n")


#ordenando por mais colunas
print("\n")
data4=data.sort_values(by=["Vendedor", "Produto"])
print(data4)
#é so declarar as demais variáveis em colchetes dentro do by
print("\n")


#ordenando inversamente
print("\n")
data5 = data.sort_values(by="Vendedor", ascending=False)
print(data5)
print("\n")

#ordenando os valores de maior para menor - só dar ascending false
data6 = data.sort_values(by="Total Vendas", ascending=False)
print(data6)

#se eu quiser tirar a média de vendas por vendedor eu tenho que retirar as colunas
#que não dão pra fazer a média - tipo data e nomes
print("\n")
df = data.drop(columns=["Produto","Data Venda"])
print(df.groupby("Vendedor").mean())
#assim vai


