# -*- coding:utf-8 -*-
import socket
import threading
import queue
import sys
import random 
import os


# Recebimento de dados lado cliente
def ReciveDataChat(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(data.decode('utf-8')) 
        except:
            pass


def RunChat(serverIP):
    host = socket.gethostbyname(socket.gethostname())
    destinion = input('Porta: ') 
    port = random.randint(6000, 10000)
    print(f'Seu IP: {str(host)} Porta: {str(port)} ')
    server = (str(serverIP), int(destinion))
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((host, port))

    name = input('Digite seu nome: ')
    # Gerando nome caso não digite
    if name == '':
        name = 'Usuário' + str(random.randint(1000, 9999))
        print(f'Seu nome: {name}')

    udp.sendto(name.encode('utf-8'), server) 
    threading.Thread(target = ReciveDataChat, args = (udp, )).start()
    # MSG
    while True:
        data = input(': ')
        # para sair
        if data == '#': # ESC chr(27)
            break
        elif data == '':
            continue

        data = '[' + name + ']' + ': ' + data
        udp.sendto(data.encode('utf-8'), server)  
    udp.sendto(data.encode('utf-8'),server)   
    udp.close()
    os._exit(1)
    # Acabo parte do chat cliente