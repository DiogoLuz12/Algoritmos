def lerEmail(email):
    import re
    email = input("Digite o seu email: ")
    regex = '^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while not re.search(regex, email):
        print("Email invalido")
        email = input("Digite o seu email novamente: ")
    return email


def lerint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: digite um número válido!!')
            continue
        else:
            return n


def linha(tam=10):
    return ' ----- ' * tam

def cab (txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu (lista):
    cab('MENU')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = lerint('Opção: ')
    return opc

