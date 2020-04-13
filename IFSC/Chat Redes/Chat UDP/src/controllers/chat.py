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
            print('\n' + data.decode('utf-8')) 
        except:
            pass


def RunChat(serverIP):
    host = socket.gethostbyname(socket.gethostname())
    port = int(input('Qual a porta que você deseja usar: ')) #random.randint(6000, 10000)
    destinion = input('Digite a Porta que deseja se conectar: ')
    if destinion == '':
        destinion = 6000
    print(f'Seu IP: {str(host)} Porta: {str(port)} ')
    server = (str(serverIP), int(destinion)) 
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Liga
    udp.bind((host, port))

    name = input('Digite seu nome: ')
    # Gerando nome caso não digite
    if name == '':
        name = 'Usuário' + str(random.randint(1000, 9999))
        print(f'Seu nome: {name}')
    # enviar para
    udp.sendto(name.encode('utf-8'), server)

    threading.Thread(target = ReciveDataChat, args = (udp, )).start()

    print('O chat está aberto pode começar a conversar :)')
    # MSG
    while True:
        data = input('\n-> ')
        # para sair
        if data == '#': 
            break
        elif data == '':
            continue
        data = str(' ' + name + ': ' + data + '\n')
        udp.sendto(data.encode('utf-8'), server)  

    udp.sendto(data.encode('utf-8'),server)   
    udp.close()
    os._exit(1)
    # Acabo parte do chat cliente