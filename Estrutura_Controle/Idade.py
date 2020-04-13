# -*- coding: utf-8 -*-


#Códigos que representam as cores das menssagens de help

ERROR  = '\033[91m'
NORMAL = '\033[0m'


def age_range(age):

    if 0 <= age < 18:
        return "Menor de Idade!"
    elif age in range(19, 35):
        return "Adulto!"
    elif age in range(35, 56):
        return "Melhor Idade!"
    elif age >= 56:
        return "Terceira idade"
    else:
        return "Idade invalida!"


if __name__ == "__main__":

    for age in (17, 35, 27, 100, -2, 55):
        print(f"{age}: {age_range(age)} ")
           
    