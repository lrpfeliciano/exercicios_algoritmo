total = float(input("Informe o valor total: ") )
numero = int(input("Informe número de clientes: "))

valorPorCliente = total / numero

print(f"O valor é R$ {valorPorCliente} por cliente")

print("O valor {0} por cliente".format(valorPorCliente ))  
#print("O valor é R$ " + valorPorCliente + " por cliente")