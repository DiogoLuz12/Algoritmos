granted = False
def grant():
    global granted
    granted = True


def login(name,password):
    success = False
    file = open("detalhes.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Login aceite!")
        grant()
    else:
        print("Password ou nome de utilizador errado! ")


def register(name,password):
    file = open("utilizadores.txt","a")
    file.write("\n"+name+","+password)
    file.close()
    grant()

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
        print("Escreva o seu username e a sua password para se registar: ")
        name = input("Escreva o nome de utilizador: ")
        password = input("Escreva a sua password:")
        register(name,password)


def begin():
    print("---Bem-Vindo---")
    option = input("Login or register (login,reg): ")
    if(option !="login" and option!="reg"):

        begin()
    else:
        if (option =="login"):
            login()
        if (option =="reg"):
          name = input("Username: ")
          password = input("Password: ")
          register(name,password)


begin()
