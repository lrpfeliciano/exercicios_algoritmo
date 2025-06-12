codigo = int(input("Informe o código: "))

if codigo == 1:
    print("Alimento não perecível")
elif codigo == 2 or codigo == 3 or codigo == 4:
    print("Alimento perecível")
elif codigo == 5 or codigo == 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene pessoal")
elif codigo >= 8 and codigo <= 10:
    print("Utensílios domésticos")
else:
    print("Inválido")