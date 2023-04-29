print("Hello World") #TODO 1: I still have to understand the concept of this thing called "world"

import pandas as pd
import numpy as np

#lemrando que para criar um data frame do zero temos:


df_teste = pd.DataFrame({
    "Modelo": ["X", "Y", "Z"],
    "Custo": [1,2,3]
    })

print(df_teste)
#nomeia as colunas antes e entre colchetes coloca os valores das linhas

print("\n------------------------------")
#lembrando que \n quebra a linha - só para deixar melhor na visuaização