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
            a.write(f'{nome};{idade};{email}\n')
        except:
            print('ERRO!')
        else:
            print(f'Novo registo de {nome}.')
            a.close()