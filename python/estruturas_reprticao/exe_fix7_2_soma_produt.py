# EXERCÍCIO 2
# Leia o preço de vários produtos e efetue a soma de todos eles. Pare de ler novos preços quando o usuário digitar -1. Em seguida, mostre o valor final da soma.

soma = 0
preco = float(input())

while(preco != -1):
    soma += preco
    preco = float(input())
print(soma)