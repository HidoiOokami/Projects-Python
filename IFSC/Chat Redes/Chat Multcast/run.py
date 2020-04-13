# Importando modulos
import sys
import os

from src.controllers.chat import RunChat
from src.controllers.server import RunServer

if __name__ == '__main__':
    if len(sys.argv) == 1:
        RunServer()(sys.argv[1]) 
    elif len(sys.argv) == 2: 
        RunChat(sys.argv[1])
    else:
        print('Rodar o Serevr:-> python run.py')
        print('Rodar como Usuário:-> python run.py <IP do Server>')