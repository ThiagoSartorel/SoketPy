import json
import socket

NomeUsuario = ""

class Mensagem(object):
    def __init__(self):
        self.user = ""
        self.msg = ""
        self.flag = ""

def enviaMensagem(cliente, usuario, mensagem, flag):
    msg = Mensagem()
    msg.user = usuario
    msg.flag = flag
    msg.msg = mensagem
    msg_string = json.dumps(msg.__dict__, indent=0)
    cliente.send(bytes(msg_string, encoding="utf-8"))
    return

def Main():
    # cria o socket TCP do cliente, abrindo uma porta alta
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print('Cliente Python UDP: {}'.format( mySocket.getsockname )  )

    # define o endereço e porta do servidor de destino
    servidorDestino = ('127.0.0.1', 10000)

    #realiza a conexao com o servidor
    mySocket.connect(servidorDestino)

    username = input("Nome:")
    NomeUsuario = username
    enviaMensagem(mySocket, NomeUsuario, "", "NN")

    while True:
        # aguarda o usuário digitar uma mensagem
        message = input(" -> (q sair) ")

        if message == 'q':

            break

        # envia a mensagem do usuário para o servidorDestino
        mySocket.send(message.encode())

        # fica em wait ate que uma mensagem chegue
        # recebe e mostra a mensagem devolvida pelo servidor
        data = mySocket.recv(4096)
        print('Recebido do servidor {}: {}'.format( mySocket.getpeername(),data.decode()))
    
    mySocket.close()

if __name__ == '__main__':
    Main()