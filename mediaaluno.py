nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informr a nota 2: "))

media = (nota1 + nota2) / 2

print(f'A média é {media:.2f}')
if media >= 7:
    print("Aprovado")
else:
    #print("Reprovado")
    #Fluxo antigo
    recuperacao = float(input("Nota de recuperacao: "))
    novamedia = (media + recuperacao) / 2
    if novamedia >= 5:
        print("Aprovado")
    else:
        print("Reprovado")
    print(f'A média final é {novamedia:.2f}')