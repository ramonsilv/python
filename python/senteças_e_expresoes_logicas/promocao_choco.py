n= int(input("informe a quantidade a ser comprada de barras de chocolate: "))
if n % 3 == 0:
    valor = n *10/3
    print("O valor a ser pago é", format(valor,".2f"),"reais")

else:
    valor = (n - n%3) * 10/3 + 4 * (n%3)
    print("O valor a ser pago é", format(valor, ".2f"), "reais")

# ou
# valor = 0
# barra = int(input("informe a quantidade de barra: ")) #EX: 17
# valor += barra // 3 * 10 # valor = 0 +50 -> VALOR = 50
# valor += barra % 3 * 4 # VALOR = 50 + 8 -> VALOR = 58
# print(valor) #58