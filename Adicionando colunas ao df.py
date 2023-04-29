import pandas as pd
import numpy as np

notas_df = pd.DataFrame({
    "nome":["Ana", "Pedro", "João"],
    "nota 1": [9, 7, 10],
    "nota 2": [6, 9, 8],
    "nota 3": [7, 5, 10],
    "nota 4": [10, 10, 6]
})

print(notas_df)

#agora eu vou adicionar uma coluna - append basicamente

print("\n")

notas_df["Média"] = ((notas_df["nota 1"] + notas_df["nota 2"] + notas_df["nota 3"] + notas_df["nota 4"])/4)

#se eu colocasse ao invés de média, o nome de uma coluna já existente eu só substituiria os valores originais

print(notas_df)

print("\n")

notas_df["Faltas"] = (5, 3, 2)
notas_df["Faltas_2"] = 1
print(notas_df)
#se eu colocasse só um número ele inputaria o mesmo valor para todas as observações

novasfaltas = [9, 9, 9]

#para saber a classe do objeto podemos dar print no seu tipo
print(type(novasfaltas))

notas_df["Faltas"] = novasfaltas #inputando a lista como a coluna de faltas - substituindo
print(notas_df)

#alterando apenas um valor de uma observação

#loc de localização
notas_df.loc[1, "nota 2"] = 12
print(notas_df)

notas_df.loc[1, "nota 1"] = 1000
print(notas_df)
#tem que ser pelo nome da coluna mesmo - se colocar só o numero da coluna ele nao entende que é a posição da coluna

#mas tem que recalcular a média - para isso substituimos o valor da coluna média


notas_df["Média"] = ((notas_df["nota 1"] + notas_df["nota 2"] + notas_df["nota 3"] + notas_df["nota 4"])/4)
print(notas_df)

notas_df["Olar"] = ("Z")
print(notas_df)

#criando novas linhas - é concat do pandas - tem outras maneiras de fazer isso

# Tem outros jeitos de fazer isso, mas por enquanto usando so o concatenar
# está ok

# Para comentar multiplas linhas o
# comando é control + barra

new_row = {"nome": "ele", "nota 1": 10, "nota 2": 10, "nota 3": 10, "nota 4": 10, "Média": 10, "Faltas": 10,
           "Faltas_2": 1, "Olar": "z"}

notas_df = pd.concat([notas_df, pd.DataFrame([new_row])], ignore_index=True)
print(notas_df)


