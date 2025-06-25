vetor = []

for i in range(10):
    entrada = int(input("Informe o número: "))
    vetor.append(entrada)

somaImpares = 0
for i in vetor:
    if i % 2 != 0:
        somaImpares += i
        #somaImpares = somaImpares + i    
print(f'A soma dos números ímpares é: {somaImpares}')