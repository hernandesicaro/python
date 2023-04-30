import pandas as pd

l1 = pd.read_excel("inner/loja1.xlsx")
l2 = pd.read_excel("inner/loja2.xlsx")

lojas = [l1,l2]

for x in lojas:
    print(x.shape)
    print(type(x))

#inner join - verifica as observações de ambos os datasets
#inner join é o overlap baseado em alguma variável

#dica = pode selecionar uma frase inteira e dar shift + ' para deixar tudo entre aspas
print("\n")
#fazendo o primeiro inner join
join1 = pd.merge(l1,l2, on = ["Vendedor"],
                 how = "inner")
#diferente do merge simples, aqui precisamos declarar em qual variável estamos fazendo o merge
#a opção on= é onde declaramos a variável e o how é como queremos o merge
print(join1)
print("\n")

#perceba que o python renomeou pra gente com _x a loja 1 e _y as variáveis da loja 2

#esse comando lista todas as colunas de um dataframe
print(join1.columns.values.tolist())
print("\n")

#eu posso escolher quais variáveis permanecerão depois do merge
#para isso é so declarar as colunas no dataframe
#e o suffixes vc esccolhe como ele vai renomear as colunas com mesmo nome dos diferentes datasets
resumo = pd.merge(l1,l2[["Vendedor", "Total Vendas"]],
                  on = ["Vendedor"],
                  how = "inner",
                  suffixes=(" Loja 1", " Loja 2"))
print(resumo)
resumo.to_excel("resumo.xlsx")

