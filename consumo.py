# 1) Ler tempo gasto
tempo = float(input("Informe o tempo gasto: "))
# 2) Ler a velocidade média
velocidade = float(input("Informe a velocidade média: "))
# 3) Calcular a distância
distancia = tempo * velocidade
# 4) Calcular os litros usados
litros = distancia / 12
# 5) A exibição das informações
print(f'O tempo gasto: {tempo}')
print(f'A velocidade média: {velocidade}')
print(f'A distância: {distancia}')
print(f'A quantidade de litros: {litros:.3f}')