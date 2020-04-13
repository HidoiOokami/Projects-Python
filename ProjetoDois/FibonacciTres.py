#-*- coding: utf-8 -*-

def fibonacci(quantidade): #gerando qtd de numeros
        # lista
    resultado = [0, 1]
    # _ boas praticas variavel que não esta sendo usada
    for _ in range(2, quantidade): # do 2 porque já temos os dois primeiros
        resultado.append(sum(resultado[-2:])) # resultado[-2:] penultimo + resultado[-1:] ultimo nesse caso o-2: pega os dois ultimos
        #condição de saida 
    return resultado

if __name__ == "__main__":
    #Listar os 20 primeiros
    for fib in fibonacci(20):
        print(fib)