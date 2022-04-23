import socket, json
import threading

Clientes = []

class cliente(object):
    def __init__(self):
        self.nome = ""
        self.con = ""

def rodaThread(conn):
    while True:
        print('Aguardando mensagens...')
        data = conn.recv(4096)
        if not data:
            break
        mensagem = json.loads(data)
        if mensagem.get("flag") == "NN": #Novo usuario
            print("Usuario " + mensagem.get("user") + " - Entrou")
            user = cliente()
            user.nome = mensagem.get("user")
            user.con = conn
            #Clientes.append()
            print(json.loads(user))
        # devolve a mensagem para o cliente
        conn.send(data.upper())
    conn.close()
    return

def Main():
    host = "0.0.0.0"
    port = 10000
    # cria o socket TCP do servidor (Internet,Transporte)
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Configura o IP e a porta que o servidor vai ficar executando
    socketTCP.bind((host,port))
    print('Servidor Python TCP: {}:{}'.format(host,port))

    # habilita o servidor para aceitar conexões
	# o parâmetro indica a quantidade máxima de solicitações de conexão que podem ser enfileiradas, antes de serem recusadas. Ex: 5 (congestionamento)
    socketTCP.listen(1)

    # fica em loop aguardando novas conexões de clientes
    while True:
        # fica bloqueado aguardando a conexão de um cliente
        conn, addr = socketTCP.accept()
        print("Conexão realizada por: " + str(addr))

        # cria e dispara a execução da thread do cliente
        t = threading.Thread(target=rodaThread, args=(conn,))
        t.start()

    socket.close()

if __name__ == '__main__':
    Main()