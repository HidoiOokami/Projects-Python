
# assemelha a ideia de sobre escrita do Java


def log(function):
    def decorator(*args, **kwargs): # argumentos posicionais variaveis e argumentos nomeados vareaveis
        print(f'inicio da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y

if __name__ == '__main__':
    print(soma(5, 7))
    #argumento nomeado vareavel
    print(sub(5, y=7)) # o y fixo ao nome do argumento passado