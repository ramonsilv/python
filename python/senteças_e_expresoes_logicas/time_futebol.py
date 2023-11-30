time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input(f"Quantos gols o {time1} marcou? "))# o f serve basicamente para trazer a variavel para o contexto da string ou do texto entre aspas("")

time2 = input("Digite o nome do segundo time: ")
gols2 = int(input(f"Quantos gols o {time2} marco? "))#o f serve basicamente para trazer a variavel para o contexto da string ou do texto entre aspas("")

if gols1 > gols2:
    vencedor = time1

elif gols2 > gols1:
    vencedor = time2

else:
    vencedor = "EMPATE"

if vencedor == "EMPATE":
    print("A partida terminou em empate! ")
else:
    print(f"o time vencedor é o {vencedor}!")