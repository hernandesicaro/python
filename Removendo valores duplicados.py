import pandas as pd

data = pd.read_excel("base_vendas.xlsx")
print(data)
print(type(data))
print(data.shape)

print("\n")

#queremos saber o número de vendedores únicos

uni_vend =  data.nunique()
print(uni_vend)
print("\n")
#perceba que ele faz um resumo de quantos valores unicos tem em cada variável


#agora vamos verificar quais são os valores que estão duplicados
#subset pega a coluna que vc quer
#keep first mantém só a primeira observação
vend_dup = data.duplicated(subset = "Vendedor", keep = "first")
print(vend_dup)
print("\n")
vend_dupf = data.duplicated(subset = "Vendedor", keep = False)
print(vend_dupf)
#o true é quando ele verifica que o anterior é igual
#então o que o duplicated faz é verificar se n-1 = n

#se deixarmos keep = false ele considera todas as observações duplicadas como true


print("\n")
#agora eu vou adicionar a coluna de duplicados no dataframe original
data["Confere Dupla"]= data.duplicated(subset= "Vendedor", keep = "first")
print(data)

print("\n")
#agora eu vou dropar as duplicidades
data_d = pd.read_excel("base_vendas.xlsx")
data_d["Confere Dupla"] = data.duplicated(subset="Vendedor", keep = "first")
print(data_d)
print("\n")
data_d = data_d.drop_duplicates(subset= "Vendedor", keep = "first")
print(data_d)
#no caso mantém só o primeiro valor que não é duplicado
print("\n")

