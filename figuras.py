import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data/plot_data.xlsx')
print(type(data), data.shape)

#vamos trabalhar com figuras
#dentro do plt.figure colocamos o tamanho
fig = plt.figure(figsize=(40, 20))



#subplot
#1 é a linha, 3 quantidade de colunas, 1 posição do gráfico
#aqui fazemos a figura onde vamos adicionar os gráficos
#é o template básico onde colocamos os subplots
fig.add_subplot(131)

plt.bar(data['Frutas'],
        data['Total Vendas'],
        label="plot de total de vendas de frutas")
plt.legend()
plt.title('gráfico 1')

#tem que colocar o add.subplot antes de cada gráfico

fig.add_subplot(132)

#no gráfico de pizza o primeiro argumento é o que vc quer representar o tamanho
#e o lables é o nome de cada seção
plt.pie(data['Total Vendas'],
        labels=data["Frutas"])
plt.title('gráfico 2')

#para fazer um terceiro gráfico
#lembrando que temos que colocar sempre o add_subplot
fig.add_subplot(133)
plt.stem(data["Frutas"],
         data["Total Vendas"],
         label="gráfico de stem")
plt.legend()
plt.title('gráfico 3')


#agora eu vou fazer um quarto gráfico
#só pra ilustrar quando temos duas linhas e qual posição vai

fig.add_subplot(235)

plt.bar(data["Frutas"],
        data["Total Vendas"],
        color="tab:red",
        label="Total de vendas - gráfico 4")
plt.legend()
plt.title("gráfico 4")




#a posição do gráfico começa da esquerda pra direita de cima pra baixo
#1 2 3
#4 5 6 ...


plt.savefig('figurateste.pdf')
plt.show()