
def Login(login):

    VerMensagensResposder(login)


def listaDeRespostaDeUmMensagem(msgs, id_msg):
    lista_respostas = []
    if id_msg != '0':
        for m in msgs:
            n, id, msg, data, idResposta, nivel = m
            if id_msg == idResposta:
                lista_respostas.append([n, id, msg, data, idResposta, -1])
    return lista_respostas

def listaTopMensagensComResposta(msgs, id_user, top, mostra_user=False):
    c = 0
    vtop = []
    for i in range(len(msgs)-1,-1,-1):
        n, id, msg, data, idResposta, nivel = msgs[i]
        idResposta = int(idResposta)
        if id == id_user: # and idResposta == 0:
            vtop.append([n, id, msg, data, idResposta, 0])
            c = c + 1
        if c == top:
            break
    vtop.reverse()
    # https://www.w3schools.com/python/python_lists_methods.asp
    num_carateres_por_nivel = 2
    print("=" * 80)
    if len(vtop) == 0:
        print ("Sem mensagens!")
    else:
        print("Top: ", top)
        print("{:<30} {:<20} {:^10} {:^10} {:}".format('MSG','DATA','NR/NR_MSG','USER','NÍVEL'))
        print("-" * 80)
    idResposta_ultima_resposta = 0
    while len(vtop) > 0:
        # retira 1 elemento da lista
        n, id, msg, data, idResposta, nivel = vtop.pop(0)
        idResposta_ultima_resposta = n
        # escreve num_carateres_por_nivel espaços / nível,
        # não muda de linha
        print (" " * num_carateres_por_nivel * nivel, end='')
        print("{:<30} {:<20} {:^10} {:^10} {:^10}".format(msg,data,"{:}/{:}".format(n, idResposta),id, nivel))
        # Obter respostas da msg com NR: n
        lista_respostas = listaDeRespostaDeUmMensagem(msgs, n)
        # adiciona respostas no início da lista
        for m in lista_respostas:
            m [5] = nivel + 1
            vtop.insert(0, m)
    print("=" * 80)
    return idResposta_ultima_resposta

def LerMensagens():
    import os
    nome = "mensagens.csv"
    if not os.path.exists(nome): # Or folder
        f = open (nome, "wt", encoding='utf-8')
        print("NR;USER;MSG;ID_RESP_MSG;DATA", file=f)
        f.close()
    f = open (nome, "rt", encoding='utf-8')
    linhas = f.readline()
    linhas = f.readlines()
    f.close()
    msgs = []
    for m in linhas:
        m = m.rstrip('\n')
        n, id, msg, data , idResposta= m.split(";")
        msgs.append([n, id, msg, data, idResposta,  -1])
    return msgs

def AdicionaMensagem(linhas, id, msg, id_ultima_msg):
    import datetime
    f = open ("mensagens.csv", "at", encoding='utf-8')
    data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    s = "%s;%s;%s;%s;%s" % (len(linhas)+1, id, msg, data, id_ultima_msg)
    print(s, file=f)
    f.close()
    linhas.append([len(linhas)+1, id, msg, data, id_ultima_msg, -1])
    print ("*" * 50)
    print("Mensagem inserida:", s)
    print("*" * 50)

def EscreveEstado(estado):
    estados = {'1':'Ver/criar mensagens:', '2': "Ver mensagens de outro user:",
               '3':'Responder a mensagem:'}
    print('Estado:', estados[estado])

def ObtemListaDeUsers(msgs, my_id):
    utilizadores = {} # dicionaro: não permite elementos repetidos
    for n, id, msg, data, idResposta, nivel in msgs:
        if my_id != id:
            utilizadores [id] = id
    return utilizadores

def VerMensagensResposder(my_id):
    # listar Top N mensagens
    top = 3
    print('User: %s' % my_id )
    linhas = LerMensagens()
    estado = '1';
    while True:
        EscreveEstado(estado)
        listaTopMensagensComResposta(linhas, my_id, top)

        print("Opções:\n\tEscreva texto e prima <enter> para criar nova mensagem.\n\t\t0-Logout.\n\t\t1-Ver outros.\n\t\t2-Mudar número de mensagens a ver de cada vez: %s" % top)
        msg = input("\t\t? ")
        if msg == '0':
            break
        elif msg == '2':
            top = input("Número de mensagens a ver de cada vez (%s) ?" % top)
        elif msg == '1':
            estado = '2'
            utilizadores = ObtemListaDeUsers(linhas, my_id)
            print("-" * 30)
            print("Lista de utilizadores")
            print("USER_ID")
            for u in utilizadores:
                print ("{:^6}".format(u))
            print("-" * 30)
            id_outro = input("ID do utilizador (0-logout) ?")
            while id_outro != '0':
                EscreveEstado(estado)
                id_ultima_msg = listaTopMensagensComResposta(linhas, id_outro, top)
                print("ID última mensagem: ", id_ultima_msg)
                msg = input("Escreva msg de resposta:\n\t0-sair ver msg outro utilizador.\n\t1-Responder a outra mensagem.\n\t?")
                if msg == '0':
                    estado = '1'
                    break
                elif msg =='1':
                    estado = '3'
                    id_msg = input("ID mensagem para dar resposta ?")
                    msg = input("Mensagem de resposta à mensagem %s (0-cancelar)" % id_msg)
                    if msg != '0':
                        AdicionaMensagem(linhas, my_id, msg, id_msg)
                else:       # inserir mensagem de resposta da ultima mensagem
                    AdicionaMensagem(linhas, my_id, msg, id_ultima_msg)
        else:
            AdicionaMensagem(linhas, my_id, msg, 0)



def listaTopMensagens(linhas, id_user, top):
    c = 0
    #for m in linhas:
    vtop = []
    for i in range(len(linhas)-1,-1,-1):
        m = linhas[i]
        m = m.rstrip('\n')
        n, id, msg,idResposta, data = m.split(";")
        if id == id_user and idResposta =='0':
            vtop.append("%s;%s;%s;%s" % (n, id, msg,idResposta))
            c = c + 1
        if c == top:
            break
    print("Mensagens:")
    vtop.reverse()
    for m in vtop:
        print(m)

    id_ultima_msg = 0
    if len(vtop)>0:
        id_ultima_msg  = vtop [len(vtop)-1].split(";")[0]   # ultima
    return id_ultima_msg
