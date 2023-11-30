uf = input("informe a UF do estado desejado: ").upper

match uf:
    case "AC":
        print('Estado: Acre')
    case "AL":
        print('Estado: Algoas')
    case "AP":
        print('Estado: Ampá')
    case "AM":
        print('Estado: Amzonas')
    case "BA":
        print('Estado: Baia')
    case "CE":
        print('Estado: Cerá')
    case"DF":
        print('Estado: Distrito Federal')
    case "ES":
        print('Estado: Esririto Santo')
    case"GO":
        print('Estado: Goás')
    case"MA":
        print('Estado: Maranhão')
    case"MT":
        print('Estado: Mato Grosso')
    case"MS":
        print('Estado: Mato Grosso do Sul')
    case"MG":
        print('Estado: Minas Gerais')
    case"PA":
        print('Estado: Pará')
    case"PB":
        print('Estado: Paraíba')
    case"PR":
        print('Estado: Paraná')
    case"PE":
        print('Estado: Pernambuco')
    case"PI":
        print('Estado: Piauí')
    case"RJ":
        print('Estado: Rio De Janeiro')
    case"RN":
        print('Estado: Rio Grande Do Norte')
    case"RS":
        print('Estado: Rio Grande Do Sul')
    case"RO":
        print('Estado: Rondonia')
    case"RR":
        print('Estado: Roraima')
    case"SC":
        print('Estado: Santa Catarina')
    case"SP":
        print('Estado: São Paulo')
    case"SE":
        print('Estado: Sergipe')
    case"TO":
        print('Estado: Tocantins')
    case _:
        print('UF não encontrada')