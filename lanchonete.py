
preco = 0.0
total = 0.0
CACHORRO_QUENTE = 12
HAMBURGUER = 12
CHEESEBURGUER = 13
REFRIGERANTE = 8
while True:
    codigo = input("Informe o código: ")
    quantidade = int(input("Informe a quantidade: "))
    if codigo == '100':
        preco = CACHORRO_QUENTE
    elif codigo == '103':
        preco = HAMBURGUER
    elif codigo == '104':
        preco = CHEESEBURGUER
    elif codigo == '105':
        preco = REFRIGERANTE
    else:
        print("Código inválido.'")
        continue
    total = total + (preco * quantidade)
    resp = input("Deseja continuar? (s/n) ")
    if resp == 'n' or resp == 'N':
        break

print(f"O valor total é {total:.2f}")

    