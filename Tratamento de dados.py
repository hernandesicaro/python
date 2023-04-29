import pandas as pd


data = pd.read_excel("Tratamento_Dados.xlsx")
print(data)

#verificando o tamanho do dataframe
print(data.shape)
#verificando o tipo do objeto
print(type(data))


print("\n")
#substituir os NAs com a média dos valores presentes
data["Total Vendas"] = data["Total Vendas"].fillna(data["Total Vendas"].mean())
#pegando a coluna que tem os dados NA, e preenchendo com a média dos valores existentes
print(data)


print("\n")
data = pd.read_excel("Tratamento_Dados.xlsx")
#Agora eu vou colocar um valor qualquer no lugar dos NAs
data["Total Vendas"] = data["Total Vendas"].fillna(5)
print(data)

print("\n")
data = pd.read_excel("Tratamento_Dados.xlsx")
#posso também colocar uma string vazia ou falar qualquer coisa
data["Total Vendas"]=data["Total Vendas"].fillna("")
print(data)

print("\n")
#agora vamos pegar o último valor não NA e replicar para as linhas que tem NA
#prrenche com o ultimo registro valido encontrado
data = pd.read_excel("Tratamento_Dados.xlsx")
data["Total Vendas"]=data["Total Vendas"].ffill()
print(data)


print("\n")
data = pd.read_excel("Tratamento_Dados.xlsx")
#value_counts conta quantas linhas/vendas foram feitas
qtd_venda = data["Vendedor"].value_counts()
print(qtd_venda)
#conta quantas ocorrências da variável apareceram

print("\n")
data = pd.read_excel("Tratamento_Dados.xlsx")

#agrupando variáveis
#fazendo a média de vendas por vendedor
#mean by group
print(data.groupby(["Vendedor"]).mean())



