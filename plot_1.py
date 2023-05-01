import pandas as pd

#temos que instalar o matplotlib
#pip install matplotlib (no terminal)

import matplotlib.pyplot as plt

data = pd.read_excel("data/plot_data.xlsx")
print(type(data), data.shape)

#para verificar a versão de algum pacote é so digitar pip show [nome do pacote]

# plt.plot(data["Frutas"], data["Total Vendas"])
# plt.show()

#fazendo um gráfico de barras simples
plt.bar(data["Frutas"], data["Total Vendas"])

#melhorando a apresentação do gráfico
plt.title("Valor total de vendas por Fruta")
plt.xlabel("Frutas")
plt.ylabel("Valor (R$)")


plt.savefig("first_plot.pdf")
plt.show()