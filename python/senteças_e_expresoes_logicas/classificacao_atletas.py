idade = int(input("qual idade o atleta: "))

if idade >= 6 and idade <= 11:
    print("Sua categoria é infantil")
elif idade >=12 and idade <= 17:
    print("Sua categoria é Juvenil")
elif idade >= 18 and idade <=45 :
    print("Sua categoria é aduta")
else:
    print("idade não corresponde á uma categoria")