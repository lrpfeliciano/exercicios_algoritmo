numero = int(input("Informe o número: "))

fatorial = 1
saida = ''
for i in range(numero, 0, -1):
    fatorial = fatorial * i
    saida = saida + str(i) 
    if i != 1: 
        saida = saida + '.'
print(f'{numero}! = {saida} = {fatorial}')