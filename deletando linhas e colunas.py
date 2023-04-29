import pandas as pd

data = pd.read_excel("sample.xlsx")
print(data)

#para saber a dimensão do dataframe
print(data.shape)

#para saber a classe do objeto
print(type(data))

print("\n")
#deletando missing values - deleta todas as linhas que tem pelo menos um NA
data2 = data.dropna()
print(data2)

#agora vamos remover uma coluna qualquer
print("\n")
del data2["Produto"]
print(data2)

#deletando mais de uma coluna - pra isso eu vou carregar de novo o dataframe do exemplo

print("\n")
df = pd.read_excel("sample.xlsx")
#para deletar columas usamos o pd.drop
df = df.drop(columns=["Produto", "Total Vendas"])
print(df)
#só lembrando que da pra renomear com o mesmo nome e fazendo modificações igual ao R X = talcoisadeX

print("\n")
#excluindo linhas quaisquer
df2 = pd.read_excel("sample.xlsx")
df2 = df2.drop(1, axis=0)
print(df2)


print("\n")
#deletando mais de uma linha ao mesmo tempo
df2 = df2.drop([3,6] ,axis = 0)
print(df2)
