
from EscolaFuncoes import cadastrar, listagem, mensagem, mensagem_personalizada


vetor = []

while True:
    mensagem()
    op = int(input("1 - Cadastro\n2 - Listagem\n9 - Sair\nInforme a opção: "))
    match op:
        case 1:
            cadastrar(vetor)
        case 2:
            listagem(vetor)
        case 9:
            mensagem_personalizada("Obrigado acessar o nosso programa.")
            break
        case _:
            mensagem_personalizada("Opção inválida.")


