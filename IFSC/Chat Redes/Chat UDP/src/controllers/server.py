# -*- coding:utf-8 -*-
import socket
import threading
import queue
import sys
import random 
import os


# Recebimento de dados lado servidor
def ReciveDataServer(sock, recivePackets):
    while True:
        # Bytes suficientes para cobrir a mensagem.
        data, addr = sock.recvfrom(1024)  
        # Coloque um item na fila. Se a fila estiver cheia, aguarde até que um slot livre esteja disponível antes de adicionar o item dentro de um set.
        recivePackets.put((data, addr))


# Start Servidor
def RunServer():
    # gethostbyname() Traduza um nome de host para o formato de endereço IPv4. O endereço IPv4 é retornado como uma string, como '100.50.200.5'. Se o nome do host for um endereço IPv4, ele será retornado inalterado.
    # gethostname() Retorna uma string contendo o nome do host da máquina onde o interpretador Python está executando no momento.
    host = # socket.gethostbyname(socket.gethostname())
    port = 5000
    print(f'\nIP e Porta do Servidor: {str(host)}:{port}')
    # Protocolo UPD sendo definido
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Ligue-se a porta e ao host
    udp.bind((host, port))
    clients = set()
    # módulo implementa filas de vários produtores e vários consumidores. É especialmente útil na programação de threads quando as informações devem ser trocadas com segurança entre vários threads.
    recivePackets = queue.Queue()

    print("Servidor Rodando :)")

    # Iniciando Threading
    threading.Thread(target = ReciveDataServer, args = (udp, recivePackets)).start()

    while True:
        # Se o recivePackets for diferente de vazio
        while not recivePackets.empty():
            # O método get () retorna um valor para a chave dada. Se a chave não estiver disponível, retorna o valor padrão Nenhum.
            data, addr = recivePackets.get()
            # Verificando a existencia de algo no set clients
            if addr not in clients:
                # Adicione a ele
                clients.add(addr)
                continue
            # Adicione a ele mesmo se existir
            clients.add(addr)
            # Codificação utf-8
            data = data.decode('utf-8')
            # o Metodo endswith() verifica se aquilo passado existe dentro do dado
            if data.endswith(chr(27)): # 
                # Remova ele do chat
                clients.remove(addr)
                continue
                
            print(str(addr) + data)

            # Mostrando as mensagens
            for msg in clients:
                if msg != addr:
                    # Envie dados para o soquete. O soquete não deve ser conectado a um soquete remoto, pois o soquete de destino é especificado por endereço .
                    udp.sendto(data.encode('utf-8'), msg)

    udp.close()