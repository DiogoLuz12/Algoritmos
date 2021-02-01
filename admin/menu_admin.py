from MENU.lib.arquivo import *
from time import sleep
from MENU.mensagens import Login

arq = 'utilizadores.txt'




def menu_admin(admin):
    while True:
        resposta = menu(
            ['Arquivo de utilizadores','Novo utilizador','Editar utilizador','Remover utilizador','Programa normal','Sair do programa'])
        if resposta == 1:  # Listagem dos utilizadores
            lerUtil(arq)

        elif resposta == 2:  # Adicionar um novo utilizador
            cab('Novo Utilizador:')
            nome = str(input("Nome: "))
            password = input("pass: ")
            idade = leridade()
            email = lerEmail('Email: ')

            registo(arq, nome, password, idade, email)
        elif resposta == 3:
            edit()
        elif resposta == 4:
            remover()
        elif resposta == 5:
            print('Programa normal')
            Login(admin)
        elif resposta == 6:
            cab('A terminar o programa...')
            break
        else:
            print('ERRO! Escolha uma opção correta: ')
        sleep(2)
