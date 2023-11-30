a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor da lado B: "))
c = float(input("Digite o valor do ldao C: "))

if a == b and b == c:
    tipo = "Equilátero"
elif a == b or b == c or a == c:
    tipo = "Isósceles"
else:
    tipo = "escaleno"

print(f"O triângulo com lados A = {a}, B = {b} e c = {c} é um triãngulo {tipo}.")