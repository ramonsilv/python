sexo = str(input("Informe o seu sexo biologico. Masculino(M) ou Feminino(F): ").upper())
altura = float(input("informe a sua altura:"))

peso_ideal_m = 72.7 * altura - 58
peso_ideal_f = 62.1 * altura - 44.77

if sexo == "M":
    print("O seu peso ideal será: ", round(peso_ideal_m))
    #peso_ideal_m = 72.7 * altura - 58
    #print("O seu peso ideal será: ", round(peso_ideal_m)) UMA MANEIRA SER FEITO

    #print(round(72.7 * altura - 58)) OUTRA MANEIRA A SER FEITA
elif (sexo == "F"):
    print("O seu peso ideal será: ", round(peso_ideal_f))
    #peso_ideal_f = 62.1 * altura - 44.77
    #print("O seu peso ideal será: ", round(peso_ideal_f))

    #print(round(62.1 * altura - 44.77))OUTRA MANEIRA A SER FEITA
else :
    print("sexo invalido")