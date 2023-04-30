import pandas as pd

vendas = pd.read_excel("left/vendas.xlsx")
vendedores = pd.read_excel("left/vendedores.xlsx")

list = [vendas, vendedores]

for x in list:
    print(x.shape,
          type(x),
          x.columns.values.tolist())

print("\n")
#verificando as vendas e os vendedores - aqui usamos how left join
join1 = pd.merge(
    vendas,
    vendedores,
    on = "Id Vendedor",
    how = "left",
    suffixes = (" Vendas", " Checagem"))

print(join1)
#ou seja, ele manteve o dataset inteiro da esuqereda e juntou com o segundo dataset
# e manteve o id do vendedor pelo dataset da esquerda
#vamos remover os duplicados/NAs
print("\n")
join_clean = join1.dropna()
print(join_clean)

#lembrando que se eu quisesse colocar algum valor diferente
#no lugar de NAs eu poderia usar o .fillna

#removendo a coluna que usamos so pra checar qual vendedor tinha no segundo dataset
print("\n")
del join_clean["Vendedor Checagem"]
print(join_clean)

