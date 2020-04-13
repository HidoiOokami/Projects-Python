#-*- coding: utf-8 -*-

def fibonacci(limite):
        # lista
    resultado = [0, 1]
   
    while resultado[-1] < limite: #enquanto ultimo elemento for menor que o limite continue
        resultado.append(resultado[-2] + resultado[-1]) # resultado[-2] penultimo + resultado[-1] ultimo
    return resultado

if __name__ == "__main__":
    for fib in fibonacci(1000):
        print(fib)