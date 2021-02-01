from MENU.lib.arquivo import registo, leridade, lerEmail, cab
from admin.menu_admin import menu_admin
from MENU.mensagens import Login


arq = 'utilizadores.txt'


granted = False
def grant():
    global granted
    granted = True


def login(name,password):
    success = False
    admin = False
    file = open("utilizadores.txt","r")
    if name == "Gustavo" and password == "couves" or name == "Diogo" and password == "couves" or name == "Ricardo" and password == "couves":
        success = True
        admin = True

    else:
        for i in file:
            a = i.split(";")
            if(a[0]==name and a[1]==password):
                success=True
                break
    file.close()
    if (success) and admin:
        print("Login aceite! (admin)")
        grant()
        menu_admin(name)
    elif (success) and not admin:
        print("Login aceite! (utilizador)")
        Login(name)
    else:
        print("Password ou nome de utilizador errado! ")

def access(option):
    if(option == "login"):

        name = input("Escreva o nome de utilizador: ")
        password = input("Escreva a sua password: ")
        login(name,password)
        if (granted):
            print("---Bem-Vindo---")
            print("Detalhes do user")
            print("Username: ", name)
    else:
        cab('Novo Utilizador:')
        nome = str(input("Nome: "))
        password = input("pass: ")
        idade = leridade()
        email = lerEmail('Email: ')

        registo(arq,nome,password,idade,email)




