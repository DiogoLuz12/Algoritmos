from MENU.lib import *

def Util(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarUtil(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerUtil(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO!')
    else:
        cab('Utilizadores ')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')

            print(f'{dado[0]:<10}{dado[1]:>3} anos     Email: {dado[2]:>3} ')
    finally:
        a.close()

def registo(arq,nome='erro',idade=0,email='erro'):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO!')
    else:
        try:
            a.write(f'{nome};{idade};{email} \n')
        except:
            print('ERRO!')
        else:
            print(f'Novo registo de {nome}.')
            a.close()


def edit():


    with open ("utilizadores.txt","r") as f:

        utilizadores = (f.readlines())

        pesquisa = input("digite o nome de utilizador: ")

        for i in utilizadores:
            aux = i.split(";")

            pos = utilizadores.index(i)

            if pesquisa == aux[0]:
                print("nome-1 \n")
                print("data de nascimento-2 \n")
                print("email-3 \n")

                opc = int (input("digite a sua opção: "))
                if opc == 1:
                    novo_nome = input("digite um novo nome: ")

                    aux[0] = novo_nome
                    utilizadores.pop(pos)
                    utilizadores.insert(pos,aux[0]+";"+aux[1]+";"+aux[2])

                elif opc == 2:
                    nova_data = input("digite uma nova data: ")


                    nova_data = nova_data.split("/")
                    idade = datetime.date.today().year - int(nova_data[2])
                    if datetime.date.today().month >= int(nova_data[1]):
                        if datetime.date.today().day >= int(nova_data[0]):
                            idade = idade

                        else:
                            idade = idade - 1
                    else:
                        idade = idade - 1

                    aux[1] = idade
                    utilizadores.pop(pos)
                    utilizadores.insert(pos,aux[0]+";"+aux[1]+";"+aux[2])

                elif opc == 3:
                    novo_email = input("digite um novo email: ")


                    aux[2] = novo_email
                    utilizadores.pop(pos)
                    utilizadores.insert(pos,aux[0]+";"+aux[1]+";"+aux[2])


    with open ("utilizadores.txt","w") as f:
        for i in utilizadores:
            f.write(i)



def remover():


    with open ("utilizadores.txt","r") as f:

        utilizadores = (f.readlines())

        pesquisa = input("digite o nome de utilizador: ")

        for i in utilizadores:
            aux = i.split(";")

            pos = utilizadores.index(i)

            if pesquisa == aux[0]:

                utilizadores.pop(pos)

    with open ("utilizadores.txt","w") as f:
        for i in utilizadores:
            f.write(i)

