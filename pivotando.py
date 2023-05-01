import pandas as pd

data = pd.read_excel("dados/pivotar.xlsx")
print(data.shape, type(data))
print("\n")
print(data)

print("\n")

pivot1 = data.pivot(index="Data Venda",
                    columns= "Cliente",
                    values= "Preço com Desconto")
print(pivot1)
print("\n")

#pivotou em termos da data(index) e os clientes viraram as colunas(columns), e dentro das linhas os
#valores foram o preço com desconto (values)

pivot2 = data.pivot(index="Cliente",
                    columns= "Data Venda",
                    values= "Preço com Desconto")
print(pivot2)
#acho que o comando de pivotar no pandas é mais intuitivo que no R
#lembrando que pivot não aceita linhas com observações repetidas
#tem que usar pivot_table
#nao suporta agregação de valores repetidos

