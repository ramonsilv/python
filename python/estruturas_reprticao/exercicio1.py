# EXERCÍCIO 1​
# Calcular e mostrar a tabuada de 1 a 10 de um número inteiro positivo qualquer informado pelo usuário.​

tabuada = int(input("Informe a número da tabuada desejada: "))

for i in range(1,11):
    result = tabuada * i
    print(tabuada, " x ", i, " = ", result)