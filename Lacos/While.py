# -*- coding: utf-8 -*-
# da para usar o if True:
# while True:
 

from random import randint

numero_informado = -1
numero_secreto   = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input("Digite um número: "))
   

print(f'Número secreto é: {numero_secreto}')