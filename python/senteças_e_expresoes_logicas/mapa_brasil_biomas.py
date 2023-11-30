bioma = input("Informe o bioma desejado: ").upper

match bioma:
    case "AMAZÔNIA": print(f"Os Estados pertencente ao Bioma {bioma} é: Acre \n Amapá \n Amazonas \n Maranhão \n Mato Grosso \n ")
    case "CERRADO":print(f"")
    case "MATA ATLÂNTICA":print(f"")
    case "CAATINGA":print(f"")
    case "PAMPA":print(f"")
    case "PANTANAL":print(f"")
    case _:print("Bioma não encontrado, \n verifique forma digitada")