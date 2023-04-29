#mais exemplos de criação de dataframes

import pandas as pd
import numpy as np

random_3 = pd.DataFrame(np.random.rand(15,10)*100)
print(random_3)

#alterando o título das colunas
#column renomea as colunas de um dataframe
random_4 = pd.DataFrame(np.random.rand(15,10)*100, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
print(random_4)

#exibe os títulos de todas as colunas
print(random_4.columns)

#criando um dataframe a partir de um dicionário
df_notas = pd.DataFrame({
    "Nome":["Ana", "Pedro", "João"],
    "Média":[9,7,10]
})
#assim ele cria por coluna 
print(df_notas)