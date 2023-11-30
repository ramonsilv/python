import math


a = float(input("Informe o valor A: "))
b = float(input("Informe o valor B: "))
c = float(input("Informe o valor C: "))

delta = (b ** 2) - 4 * a * c

x1 = (-b - math.sqrt(delta)) / (2 * a)
x2 = (-b + math.sqrt(delta)) / (2 * a)

print("O Valor da Raiz 1 é: ", x1)
print("O Valor de Delta é: ", delta)
print("O Valor da Raiz 2 é: ", x2)