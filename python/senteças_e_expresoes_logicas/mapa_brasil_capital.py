uf = input("informe a UF do estado desejado: ").upper

match uf:
    case "AC":
        print('Capital:Rio Branco')
    case "AL":
        print('Capital: Maceió')
    case "AP":
        print('Capital: Macapá')
    case "AM":
        print('Capital: Manaus')
    case "BA":
        print('Capital: Salvador')
    case "CE":
        print('Capital: Fortaleza')
    case"DF":
        print('Capital: Brasília')
    case "ES":
        print('Capital: Vitória')
    case"GO":
        print('Capital: Goiânia')
    case"MA":
        print('Capital: São Luís')
    case"MT":
        print('Capital: Cuiabá')
    case"MS":
        print('Capital: Campo Grande')
    case"MG":
        print('Capital:s Belo Horizonte')
    case"PA":
        print('Capital: Belém')
    case"PB":
        print('Capital: João Pessoa')
    case"PR":
        print('Capital: Curitiba')
    case"PE":
        print('Capital: Recife')
    case"PI":
        print('Capital: Teresina')
    case"RJ":
        print('Capital: Rio de Janeiro')
    case"RN":
        print('Capital: Natal')
    case"RS":
        print('Capital: Porto Alegre')
    case"RO":
        print('Capital: Porto Velho')
    case"RR":
        print('Capital: Boa Vista')
    case"SC":
        print('Capital: Florianópolis')
    case"SP":
        print('Capital: São Paulo')
    case"SE":
        print('Capital: Aracaju')
    case"TO":
        print('Capital: Palmas')
    case _:
        print('UF não encontrada')