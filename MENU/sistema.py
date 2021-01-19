from MENU.lib import *
from MENU.lib.arquivo import *
from time import sleep

arq = 'utilizadores.txt'

if not Util(arq):
    criarUtil(arq)


while True:
    resposta = menu(['Arquivo de utilizadores','Novo utilizador','Editar utilizador','Remover utilizador','Sair do programa'])
    if resposta == 1: #Listagem dos utilizadores
        lerUtil(arq)

    elif resposta == 2: #Adicionar um novo utilizador
        cab('Novo Utilizador:')
        nome = str(input("Nome:"))
        idade = lerint('Idade: ')
        email = lerEmail('Email: ')

        registo(arq,nome,idade,email)
    elif resposta == 3:
        cab('Opc 3')
    elif resposta == 4:
        cab('Opc 4')
    elif resposta == 5:
        cab('A terminar o programa...')
        break
    else:
        print('ERRO! Escolha uma opção correta: ')
    sleep(2)