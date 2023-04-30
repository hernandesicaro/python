import pandas as pd

l1 = pd.read_excel("full/loja_1.xlsx")
l2 = pd.read_excel("full/loja_2.xlsx")

list = [l1,l2]

#só lembrando que eu posso colocar vários objetos dentro de um mesmo print
for x in list:
    print(type(x), x.shape)

print("\n")


#é mais fácil criar um lista de opbjetos de passar dentro do concat
#mas na pratica nao faz diferença se declararmos todos os
#objetos dentro dele
join1 = pd.concat(list)
print(join1)
#full join é quando fazemos um merge e mantemos ambos
#os datasets mesmo nas observações que não deram merge
#no caso do stata, por exemplo,
#é como se tivéssemos mantido _merge == 1 e _merge == 2

print("\n")
#agora vamos remover as observações duplicadas
join2 = join1.drop_duplicates(subset = "Id Vendedor")
#o subset é a variável que vc ta declarando na qual
#quer retirar os termos duplicados
#no stata seria duplicates drop id vendedor
print(join2)

