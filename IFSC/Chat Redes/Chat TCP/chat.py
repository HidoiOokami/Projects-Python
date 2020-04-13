from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


def receive():
    """Recebimento de mensagens."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibilidade de o cliente abandonar o chat.
            break


def send(event = None):  
    """Lida com o envio de mensagens."""
    msg = my_msg.get()
    my_msg.set("")  # limpa os campos.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """Função para fechamento da app."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chat TCP")
top.geometry("330x290")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # Para as mensagens serem enviadas.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # Para navegar pelas mensagens anteriores.
# Mensagens.
msg_list = tkinter.Listbox(messages_frame, height = 15, width = 50, yscrollcommand = scrollbar.set, borderwidth = 0)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()  #place(x = 5, y = 5, width = 440, height = 400)
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable = my_msg, borderwidth = 0)
entry_field.bind("<Return>", send)
entry_field.place(x = 5, y = 250, width = 255, height = 25)
send_button = tkinter.Button(top, text = "Enviar", command = send, bg = "gray", fg = "white", borderwidth = 0)
send_button.place(x = 265, y = 250, width = 60, height = 25)

top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Digite a IP que deseja se conectar: ') 
PORT = input('Digite a Porta que deseja se conectar: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

tkinter.mainloop() 