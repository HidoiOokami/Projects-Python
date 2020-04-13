
def fibonacci(quantidade, sequencia=(0, 1)): # a Tupla e para novas sequecias da recursividade
    #Condição de parada a sequencia tem que ter o mesmo tamanho da quantidade
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),)) #Acrecentando na sequencia atual a soma dos dois ultimos valores 
    # a , e para definirmos que e uma tupla
    # return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))  isso e uma sobrecarga de operadores

if __name__ == "__main__":
    #Listando 20 primeiros
    for fib in fibonacci(20): #possivel passar segundo parametro (4, 5)
        print(fib)

