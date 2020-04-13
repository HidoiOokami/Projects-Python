"""Servidor multithread assincrono."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Lida com entrada dos clientes."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se conectou." % client_address)
        client.send(bytes("Digite seu Nome por favor:", "utf8"))
        addresses[client] = client_address
        Thread(target = handle_client, args = (client,)).start()


def handle_client(client):  # Toma socket do cliente como parametro.
    """Lida com uma unica conexão."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = '\n\nBem vindo %s! Se quiser sair digite {sair} para sair.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s Entrou no chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{sair}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{sair}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s Deixou o chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix indentifica o nome.
    """Mandando mensagesn para todos os clientes."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

        
clients = {}
addresses = {}

HOST = "10.151.55.40" #socket.gethostbyname(socket.gethostname())
PORT = 55000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print(f"Esperando conexões... \nIP: {HOST}:{PORT}")
    ACCEPT_THREAD = Thread(target = accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()