import socket, json
import threading

from TcpServidorPythonThready import mensagemThread

user = ''

class Mensagem(object):
    def __init__(self):
        self.user = ""
        self.msg = ""
        self.flag = ""

#Recebe as msg do cliente
def recebeMsgThread(cliente):
        while True:
            try:
                data = cliente.recv(4096).decode('utf-8') 
                data_final = json.loads(data)
                emitente = data_final.get("user")
                mensagem = data_final.get("msg")
                print(emitente +">>>"+ mensagem)                
            except:
                # Valida conexão com o servidor, se der erro 
                print('Falha ao conectar com o servidor! Digite x para continuar')
                cliente.close()
                break

#Envia msg para algum cliente 
def enviaMsgThread(cliente, user):
    while True:
        try:   
            #envia msg formatada  
            data = Mensagem()       
            data.msg = input('')#input mensagem
            #data.msg = user + ">>>" + data.msg
            data.user = user
            data.flag = "mensagem"
            data_string = json.dumps(data.__dict__, indent = 0)
            
            #print(data_string)

            #cliente.send(f'{user}>>> {data_string}'.encode('utf-8'))
            cliente.send(bytes(data_string,encoding="utf-8"))
        except:
            return

#inicializa a conexao
def inicializaConexao(cliente):
    
    try:
        # define o endereço e porta do servidor Cliente que é do serv de destino
        cliente.connect(('127.0.0.1', 10000))
        username = input ('Digite o nome do usuário: ')
        print('\nAgora você está online, '+ username + '!\n') 
        user = username
        mensagem = Mensagem()
        mensagem.user = user
        mensagem.flag = "NN"
        mensagem.msg = "entrou"
        mensagem_string = json.dumps(mensagem.__dict__, indent=0)
        cliente.send(bytes(mensagem_string, encoding="utf-8"))
        return user       
    except:
        return print('\nSem conexão com o servidor!\n') 

def Main():
    # cria o socket TCP do cliente, abrindo uma porta alta (cliente objeto socket)
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clienteN = inicializaConexao(cliente)

    #Threads
    t1 = threading.Thread(target=recebeMsgThread, args=[cliente])
    t2 = threading.Thread(target=enviaMsgThread, args=[cliente, clienteN])
    #Inicia a thread
    t1.start()
    t2.start()

    #fica em wait ate que uma mensagem chegue
    #recebe e mostra a mensagem devolvida pelo servidor
    #data, server = mySocket.recvfrom(4096)
    #print('Recebido do servidor {}: {}'.format(server, data.decode()))
    #print( str(s.recv(4096), 'utf-8') )   
    #mySocket.close()


if __name__ == '__main__':
        Main()