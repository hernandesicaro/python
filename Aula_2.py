import pandas
import pandas as pd
import numpy as np

#Comentários no python é com hashtag
#criando lista de datas com date_range
df_datas = pd.date_range("20221201", periods=31)
print(df_datas)

#\n quebra linhas quanda dá o print
print("\n-------------- Segundo data frame ------------")
df_data_m = pd.date_range("20230131", periods=12, freq='M')
print(df_data_m)
print("\n")
#com frequencia de meses o date_range considera o ultimo dia

#-------------------------------------
#o panda cria o dataframe e o numpy que dá os numeros aleatorios
random = pd.DataFrame(np.random.rand(5,1))
print("\n ------------ Numeros aleatórios-----------")
print(random)
print("\n")

#-----------------------------
random_2 = pd.DataFrame(np.random.rand(15,10)*100)
print(random_2)
