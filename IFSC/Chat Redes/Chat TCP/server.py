"""Server  multithreaded (asyncrono)."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Entrada dos clientes."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se conectou." % client_address)
        client.send(bytes("Digite seu Nome por favor:", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, )).start()


def handle_client(client):  # Tomando socket do cliente como parametro
    """Lida com uma única conexão do cliente."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Bem vindo %s! Se quiser sair digite {sair} para sair.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s Entrou no Chat" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name


def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s Se conectou." % client_address)
        client.send(bytes("Digite seu Nome por favor", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Bem vindo %s! Se quiser sair digite {quit} para sair.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s Deixou o chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = "192.168.0.172"  # socket.gethostbyname(socket.gethostname())
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Esperando conexões...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
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


def broadcast(msg, prefix=""):
    """Transmitindomsg para toda a galera."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
addresses = {}

if __name__ == "__main__":
    SERVER.listen(5)
    print(f"Esperando conexões... \nNo IP: {HOST}:{PORT}")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
