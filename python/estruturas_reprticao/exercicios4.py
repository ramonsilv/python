# EXERCÍCIO 4
# Ler 5 notas informadas pelo usuário e calcular a média aritmética entre elas.

for i in range(1,6):
    nota = float(input(f"Informe a {i}° nota: "))
    media = (nota + nota + nota + nota + nota) / 5
    print(media)