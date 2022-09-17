agenda = {}


def save_agenda():
    with open('agenda.csv', 'w') as arquivo:
        for i in agenda:
            arquivo.write(f"{i}, {agenda[i][0]}, {agenda[i][1]}\n")



def input_agenda():
    with open('agenda.csv', 'r' ) as f:
        for linha in f:
            lista = linha.split(', ')
            agenda[lista[0]] = [lista[1], lista[2][:-1]]



def adicionar_contato():
    nome = input("Qual o  nome do contato: ")
    email = input("Qual o email do contato: ")
    telefone = input("Qual o telefone do contato: ")
    agenda[nome] = [email,telefone]
    print(f'contato "{nome}" adicionado com sucesso')


def deletar_contato():
    nome = input('Quem vai rodar? ')
    del agenda[nome]
    print(f'contato "{nome}" deletado com sucesso')

def buscar_contato():
    nome = input("Quem quieres buscar? ")
    print(agenda.get(nome, 'Contato não encontrado'))
    pass

input_agenda()

while (True):

    resposta = input('Voce quer (i)nserir (b)uscar ou (d)eletrar um contato ou (s)air? ')
    if(resposta == 'i'):
        adicionar_contato()

    elif(resposta == 'b'):
        buscar_contato()

    elif(resposta == 'd'):
        deletar_contato()
    
    elif(resposta == 's'):
        save_agenda()
        break

    else:
        print("Escreve direito caramba")



