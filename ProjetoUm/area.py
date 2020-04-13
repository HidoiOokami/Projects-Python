# -*- coding: utf-8 -*-
#!/usr/local/bin/python3

from math import pi # nesse caso não posso usar math.pi
import sys
import errno

#Códigos que representam as cores das menssagens de help
ERROR  = '\033[91m'
NORMAL = '\033[0m'

def circle(lightning):
    return pi * float(lightning) ** 2 # a procedencia aqui **2 e a potencia coemaça por ele


def help():
    return print(f"É necessario informar o raio do círculo \nSintax: {sys.argv[0]} <raio> ")


#executando codigo só se for o main
if __name__ == "__main__":

    if len(sys.argv) < 2:
        help()
        sys.exit(1) #qualquer numero diferente de 0 e que terminou com erro
    if not sys.argv[1].isnumeric():  # se nãp fpr numero faça
        help()
        print(ERROR + "O valor do raio deve ser númerico!", NORMAL)
        sys.exit(errno.EINVAL)
  
    #passando via terminal o valor do raio
    lightning = sys.argv[1] # o 0 e o nome do arquivo, lightninge raio
    area = circle(lightning)
    print('Area do circulo e:', area)
