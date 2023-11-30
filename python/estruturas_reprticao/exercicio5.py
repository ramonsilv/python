# EXERCÍCIO 5
# Peça ao usuário que informe o total de produtos que deseja levar, em seguida solicite o preço de cada produto e efetue a soma de todos eles.

produto = float(input())
n = 0
for i in range(produto):
    preco = float(input("Informe o número desejado: "))
    n += preco 
print(n)