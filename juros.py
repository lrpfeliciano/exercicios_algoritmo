valor = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a taxa: "))
tempo = int(input("Informe o tempo: "))

prestacao = valor + (valor * taxa /100) * tempo

print(f'O valor atualizado é {prestacao:.2F}')