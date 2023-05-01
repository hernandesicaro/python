import pandas as pd
#lembrando que podemos selecionar t'odo o endereço e depois dar shift+" pra deixar entre aspas
data = pd.read_excel("dados/pivotar2.xlsx")

print(data.shape, type(data))

print("\n")

#Primeiro pivot
#vamos colocar como as linhas a data de venda, como coluna os clientes, e o valores como
#o preço com desconto

#lembrando que ele faz a média

p1 = data.pivot_table(index = "Data Venda",
                      columns= "Cliente",
                      values = "Preço com Desconto")
print(p1)
print("\n")

#ele faz média por default, se quiser só uma soma

p2 = data.pivot_table(index= "Data Venda",
                      columns= "Cliente",
                      values= "Preço com Desconto",
                      aggfunc= "sum")
print(p2)
print("\n")

#aggfunc tipo de cálculo que o pivot table vai fazer

p3=data.pivot_table(index="Cliente",
                    columns="Data Venda",
                    values="Preço com Desconto",
                    aggfunc="sum")
print(p3)
print("\n")

#agora queremos duas categorias de valor nas células
#uma é o preço com desconto e outra é o preço total
#para isso no argumento de values colocamos
#as colunas que queremos entre colchetes

#teremos varias colunas com cada cliente separadas em preço total e com desconto
p4=data.pivot_table(index="Data Venda",
                    columns="Cliente",
                    values=["Preço Total","Preço com Desconto"],
                    aggfunc="sum")
p4.to_excel("outputp4.xlsx") #vou fazer um arquivo em excel so pra ver melhor o resultado

print(p4)
print("\n")

#agora queremos que mostre cada cliente e segmentado por qual produto ele comprou
p5 = data.pivot_table(index="Data Venda",
                columns=["Cliente","Produto"],
                values="Preço com Desconto",
                aggfunc="sum")
p5.to_excel("outputp5.xlsx")

print(p5)
print("\n")

#com mais um nivel de informação
p6 = data.pivot_table(index="Data Venda",
                columns=["Cliente","Produto"],
                values=["Preço com Desconto", "Preço Total"],
                aggfunc="sum")
p6.to_excel("outputp6.xlsx")

print(p6)
print("\n")

#agora vamos tratar  - vamos usar como base o que fizemos em p5

#vamos substituir todos os NA com zeros - é so usar o fillna()
p5=p5.fillna(0)
print(p5)



