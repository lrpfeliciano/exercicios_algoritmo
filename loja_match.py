codigo = int(input("Informe o código: "))
match codigo:
    case 1:
        print ("Alimento não perecível")
    case 2 | 3 | 4:
        print ("Alimento perecível")
    case 5 | 6:
        print ("Vestuário")
    case 7:
        print ("Higiene pessoal")
    case 8 | 9 | 10:
        print ("Utensílios domésticos")
    case _:
        print ("Inválido")
