# EXERCÍCIO 3
# Leia as notas de vários alunos e calcule a média entre elas. Pare de ler notas quando o usuário digitar -1. Em seguida, mostre o valor final da média.

quantidade = 0
soma = 0
n = float(input())

while(n != -1):
    soma += n
    quantidade += 1
    n = float(input())
media = soma / quantidade
print(media)