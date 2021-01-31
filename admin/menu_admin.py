from MENU.lib.arquivo import *
from time import sleep

arq = 'utilizadores.txt'




def menu_admin():
    while True:
        resposta = menu(
            ['Arquivo de utilizadores', 'Novo utilizador', 'Editar utilizador', 'Remover utilizador', 'Sair do programa'])
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
            cab('A terminar o programa...')
            break
        else:
            print('ERRO! Escolha uma opção correta: ')
        sleep(2)