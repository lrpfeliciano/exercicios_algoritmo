nome = "Luis"

print(nome)

nome = "Renato"

print(nome)

agenda = []
agenda.append("Pedro")
agenda.append(nome)

telefones = []
telefones.append('2222')
telefones.append('3333')

contatos = []
contatos.append(['Pedro', '2222'])
contatos.append([nome, '3333'])

print(contatos[0][1])

contatos2 = []
pessoa = {'nome': 'Pedro', 'telefone': '2222'}
contatos2.append(pessoa)
print(contatos2[0]['telefone'])
print("Fim")
