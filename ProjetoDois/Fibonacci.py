#-*- coding: utf-8 -*-

def fibonacci(limite):
    ultimo, penultimo = 1, 0
    print(f"{penultimo}, {ultimo}", end=", ")

    while ultimo < limite:
        #usando uma tupla para fazer o swap de valores não precisa do ()
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=(", "))
        
        
if __name__ == "__main__":
    fibonacci(1000)