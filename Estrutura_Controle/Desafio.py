# -*- coding: utf-8 -*-

import sys

'''
Conceito Notas

A     De 10,0 à 9,1
A -   De 9,0 à 8,1
B     De 8,0 à 7,1
B -   De 7,0 à 6,1
C     De 6,0 à 5,1
C -   De 5,0 à 4,1
D     De 4,0 à 3,1
D -   De 3,0 à 2,1
E     De 2,0 à 1,1
E -   De 1,0 à 0,0

Notas maiores que 10 ou menores que 0 Serão anuladas
'''
ERROR  = '\033[91m'
NORMAL = '\033[0m'

# o in range(num, ate num) #serve somente para inteiros
def grades(note):
    if note <= 10.0 and note >= 9.1:
        return print(f"A sua nota é: {note} classe A")
    elif note <= 9.0 and note >= 8.1:
        return print(f"A sua nota é: {note} classe A-")
    elif note <= 8.0 and note >= 7.1:
        return print(f"A sua nota é: {note} classe B")
    elif note <= 7.0 and note >= 6.1:
        return print(f"A sua nota é: {note} classe B-")
    elif note <= 6.0 and note >= 5.1:
        return print(f"A sua nota é: {note} classe C")
    elif note <= 5.0 and note >= 4.1:
        return print(f"A sua nota é: {note} classe C-")
    elif note <= 4.0 and note >= 3.1:
        return print(f"A sua nota é: {note} classe D")
    elif note <= 3.0 and note >= 2.1:
        return print(f"A sua nota é: {note} classe D-")
    elif note <= 2.0 and note >= 1.1:
        return print(f"A sua nota é: {note} classe E")
    elif note <= 1.0 and note >= 0.0:
        return print(f"A sua nota é: {note} classe E-")
    else:
        invalid()


def invalid():
    print(ERROR + "A nota e invalida!", NORMAL)
    sys.exit(1)

if __name__ == "__main__":
   
    grades(float(input("Digite a nota: ")))
