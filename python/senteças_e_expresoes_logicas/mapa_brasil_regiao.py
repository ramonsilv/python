regiao = input("Digite a Região que deseja consultar:")

match regiao :
    case "norte":
        print(f"Os estados pertencentes a Região {regiao} são: Acre \n Amapá \n Amazonas \n Pará \n Rondônia \n Roraima \n Tocantins")
    case"nordeste":
        print(f"Os estados pertencentes a Região {regiao} são: Maranhão \n Piauí \n Ceará \n Rio Grande do Norte \n Paraíba \n Pernambuco \n Alagoas \n  Sergipe \n Baiha")
    case "sudeste":
        print(f"Os estados pertencentes a Região {regiao} são: São Paulo \n Minas Gerais \n Rio de Janeiro \n Espírito Santo")
    case "centro-oeste":
        print(f"Os estados pertencentes a Região {regiao} são: Distrito Federal \n Goiás \n Mato Grosso \n Mato Grosso do Sul")
    case "sul":
        print(f"Os estados pertencentes a Região {regiao} são: Rio Grande do Sul \n Santa Catarina \n Paraná ")
    case _: 
        print(f"{regiao} não encorntrada")