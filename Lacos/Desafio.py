# -*- coding: utf-8 -*-
from random import randint

def given_away():
    return randint(1, 6) # o 6 entra

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if i == given_away():
        print(f"Acertou!!! seu n° = {i}")
        break
else:
    print(f"Opss não foi desta vez! seu n° = {i}")