from pydoc import cli
import socket, json
import threading 

#array dos clientes conectados
clients = []
NomeClients = []
def mensagemThread(cliente):
    while True:
        try:
            data = cliente.recv(4096)
            data_json = json.loads(data)
            if data_json.get("flag") == "NN":
                NomeClients.append(data_json.get("user"))
                print(NomeClients)
            
            broadCast(data, cliente)
        except:
            print(data_json.get("user"))
            NomeClients.remove(data_json.get("user"))
            delCliente(cliente)
            break

#Verifica o cliente (pra não repetir msg)
def broadCast(data, cliente):
    for cadaClient in clients:
        if cadaClient != cliente:
            try: 
                cadaClient.send(data)
            except:
                delCliente(cadaClient)
                

#se o cliente ñ esta mais conectado exclui...
def delCliente (cliente):
    clients.remove(cliente)
    #NomeClients.remove(userName)

def Main():
    #host = "127.0.0.1"
    #port = 10000
    #configura o IP e a porta que o servidor vai ficar executando
    #socketTCP.bind((host, port))    
    #print('Servidor Python TCP: {}:{}'.format(host, port))

    # cria o socket TCP do servidor (Internet,Transporte)
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # configura o IP e a porta que o servidor vai ficar executando
        socketTCP.bind(('127.0.0.1', 10000))
        print('Servidor Python TCP: {}:{}'.format('127.0.0.1', 10000)) #Mostra o servidor conectado    
        socketTCP.listen() #Para infifnitos clientes deixar vazio o listen
    except:
        return print('\nNão conectado!') 

    #fica em looping aguardadnod novas conexões 
    while True:              
        # fica aguardando até que chegue uma mensagem do cliente
        cliente, addr = socketTCP.accept()
        #add cliente conectado no Array        
        clients.append(cliente) 
        print("Conexão realizada por: " + str(addr))              
        thread = threading.Thread(target=mensagemThread, args=[cliente])
        thread.start()
    #socket.close()



if __name__ == '__main__':
    Main()
