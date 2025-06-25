nome = 'Luis'
print(nome)

nome2 = 'Renato'
print(nome2)

# Criando um vetor
#Iniciando vazio
vetor = [] 
#Com valores pré cadastrados
frutas = ['banana', 'maçã', 'pêra'] 

#Adicionando valores
vetor.append("Paulo")
frutas.append("mamão")

print(vetor)
print(frutas)

#Imprimir a segunda posição
print(frutas[1])

frutas[0] = 'Banana da terra'
frutas.append(nome)
frutas.append(45)
frutas.append(4.70)
frutas.insert(1, "açaí")


entrada = input("Informe o nome da fruta: ")
frutas.append(entrada)
print(frutas)


frutas.remove("Luis")
frutas.remove(45)
frutas.remove(4.7)
frutas.pop()
frutas.pop(0)
try:
    frutas.remove("João")
except:
    print("Informação não encontrada")

frutas.append(str(10))
#DEU ERRO PORQUE A POSIÇÃO NÃO EXISTIA 
#NA LISTA
#frutas[10] = 'Kiwi'
frutas.insert(10, 'Kiwi')
#Ordena em ordem crescente
frutas.sort()
#Ordenar em ordem decrescente
frutas.reverse()

for f in frutas:
    print(f)

#Remove todos de uma vez
#frutas.clear()
print("Fim")



