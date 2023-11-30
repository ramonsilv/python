from msilib.schema import Media


lista=[]
for i in range(10):
    notas = float(input("Digite as notas dos alunos: "))
    lista.append(notas)
print(lista)

#2
for item in lista:
    if ( item >= 6):
        print(item)

#3
for item in lista:
    item = item + 1
    print(item)     #percorrer somente para mostrar as notas

# for i in range(len(lista)):
#     lista[i] += 1.0     #percorrer para alterar as notas

#4
soma = 0
for notas in lista:
    soma += notas
    media = soma / len(lista)   # len -> ele pega o tamanho da lista (quantidade da lista)
print (media)

# OU EM HARD CODE

# media = 0
# for nota in lista :
#     media += nota
#     media = media / len(lista)
#     print(media)

# OU
# media = sum(lista)
# print(media)