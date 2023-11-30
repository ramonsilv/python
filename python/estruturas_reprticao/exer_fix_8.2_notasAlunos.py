#3
notas = []

while True:
    nota = float(input("Digite a nota do aluno [Digite -1 para sair]: "))

    if nota == -1:
        break
    
    notas.append(notas)

if len(notas) > 0:
    media = sum(nota) /len(notas)
    print("A média das notas dos alunos é: ", media)
else:
    print("Nenhuma nota foi inserida.")

print("lista de notas dos alunos: ", notas)