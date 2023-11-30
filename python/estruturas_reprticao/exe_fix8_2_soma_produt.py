#2
preco = []

while True:
    numer = float(input("Digite um número [Digite -1 para sair]: "))

    if numer == -1:
        break

    preco.append(numer)

total = sum(preco)

print("Lista de preçosa inseridos: ", preco)
print("O valor final da soma dos preços é: ", total)
