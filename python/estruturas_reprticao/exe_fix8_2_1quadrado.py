#1
quadrado = []

while True:
    numer = float(input("DIgite um número [Digite -1 para sair]: "))

    if (numer == -1):
        break
    quadrado = numer ** 2
    quadrado.append(numer)
print("Quadrados dos números digitados são: \n", quadrado)