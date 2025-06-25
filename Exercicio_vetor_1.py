vetorA = []
vetorB = []
for i in range(10):
    entrada = int(input("Informe um número: "))
    vetorA.append(entrada)

    resultado = 0
    if vetorA[i] % 2 == 0:
        resultado = vetorA[i] * 5
    else:
        resultado = vetorA[i] + 5
    vetorB.append(resultado)

print(vetorB)    
