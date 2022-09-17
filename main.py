agenda = {}


def adicionar_contato():
    nome = input("Qual o  nome do contato: ")
    email = input("Qual o email do contato: ")
    telefone = input("Qual o telefone do contato: ")
    agenda[nome] = [email,telefone]
    print(agenda)
    pass

def deletar_contato():
    nome = input('Quem vai rodar? ')
    del agenda(nome)
    pass

def buscar_contato():
    pass

while (True):

    resposta = input('Voce quer (i)nserir (b)uscar ou (d)eletrar um contato ou (s)air? ')
    if(resposta == 'i'):
        adicionar_contato()

    elif(resposta == 'b'):
        buscar_contato()

    elif(resposta == 'd'):
        deletar_contato()
    
    elif(resposta == 's'):
        break

    else:
        print("Escreve direito caramba")



