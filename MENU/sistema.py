from MENU.lib.arquivo import *
from MENU.lib.LOGIN import login


arq = 'utilizadores.txt'

if not Util(arq):
    criarUtil(arq)


while True:

        print("---Bem-Vindo---")
        option = input("Login or register or EXIT (1,2,3): ")
        while(option !="1" and option!="2" and option!="3"):
            option = input("Login or register (1,2): ")

        if (option =="1"):
            name = input("Username: ")
            password = input("Password: ")
            login(name,password)
        if (option =="2"):
            cab('Novo Utilizador:')
            nome = str(input("Nome: "))
            password = input("pass: ")
            idade = leridade()
            email = lerEmail('Email: ')

            registo(arq,nome,password,idade,email)

        if (option =="3"):
            break
