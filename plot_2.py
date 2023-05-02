import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#continuamos a usar o mesmo dataset da aula passada

data = pd.read_excel('data/plot_data.xlsx')

print(type(data), data.shape)
print("\n")

#o label estamos declarando qual vai ser o texto



#caso eu queira deixar cada barra de uma cor
# bar_colors = ['red', 'blue', 'red', 'orange', 'cyan']
#
# plt.bar(data["Frutas"],
#         data["Total Vendas"],
#         label="Total de Vendas",
#         color=bar_colors)
#
# #para exibir a legenda temos que ter o seguinte comando
# plt.legend()
# plt.show()


plt.bar(data["Frutas"],
        data["Total Vendas"],
        label="Total de Vendas",
        color='tab:red')

plt.title('Faturamento por fruta')



#set label locations
#ticks é quantos pontos do intervalo ele mostra no eixo x e no eixo y
plt.xticks(np.arange(0,5, step=1))

#para eu colocar um intervalo de tantos em tantos unidades que ele pula
#tem que usar o numpy (evenly spaced values within a given interval)
plt.yticks(np.arange(0,110, step=10))

#truncando/delimitando o que mostra nos eixos - claro que vai ficar zuado nesse caso
#mas é apenas ilustrativo
# plt.axis(xmin=0, xmax = 5, ymin=0, ymax=99)

#se eu quiser deixar automático o que mostra nos eixos é so colocar
plt.axis("auto")

#ajustando o nome dos eixos
plt.xlabel('Tipo de Fruta', size='20')
plt.ylabel('Venda total em R$', size='20')

#o annotate coloca quaisquer pontos no gráfico
#vc escolhe o título e o ponto onde ele vai ser plotado
# plt.annotate('Abacate', (0, 10))

#para mostrar a legenda (que se declara como label no plot)
plt.legend()

#lembrando que o plt.show() vai depois do comando de salvar
plt.savefig("second_plot.pdf")
plt.show()