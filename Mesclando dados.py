import pandas as pd
#o comando pra achar todos os valores e dar replace é CTRL + R
#lembrando que é assim que referencia pastas - tudo dentro das aspas e com barra "/"

#vamos nomear todos os dataframes que queremos concatenar
jan = pd.read_excel("mesclando/vendas_jan.xlsx")
fev = pd.read_excel("mesclando/vendas_fev.xlsx")
mar = pd.read_excel("mesclando/vendas_mar.xlsx")
#lembrando que nao tem mais append
#dai dentro do concat colocamos todos os objetos entre colchetes e separados por virgula
final = pd.concat([jan, fev, mar])

print(final)
print(final.shape)

print(final.sort_values("Total Vendas", ascending=False))
#entao para dar append em dataframes é so vc nomear cada dataframe, montar uma lista dentro do concat
print("\n")
#exportando para csv o arquivo concatenado
final.to_csv(index = False, path_or_buf = "mesclando/final.csv")

#-------------------------------------------------------------------------
print("\n")
#mostrando apenas 3 colunas selecionadas
data2 = final[["Vendedor", "Data Venda", "Total Vendas"]]
print(data2)
print("\n")


#o keys atribui um grupo para cada objeto concatenado respectivamente
data_grupos = pd.concat([jan, fev, mar], keys = ["Janeiro", "Fevereiro", "Março"])
print(data_grupos)
#visualizando o grupo do fevereiro que fica implicito quando da um print normal
print(data_grupos.loc["Fevereiro"])