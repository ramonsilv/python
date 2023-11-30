# EXERCÍCIO 1​
# Mostre o quadrado de qualquer número digitado pelo usuário. A condição de parada será quando o usuário digitar o valor -1. Até que isso ocorra, o programa deve continuar recebendo novos números e mostrando o quadrado de cada um deles.

num = float(input("DIgite um número [Digite -1 para sair]: "))

while (num != -1):
    print(num ** 2)
    num = float(input(""))