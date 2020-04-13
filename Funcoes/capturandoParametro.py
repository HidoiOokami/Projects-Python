
# Capturando todos os parametros passados

def todos_params(*args, **kwargs): #Parametros variaveis
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')


if __name__ == "__main__":
    todos_params('a', 'b', 'c') # todos os parametros aqui estão dentro da tupla que representão or args posicionais


    todos_params(1, 2, 3, legal=True, valor=12.99)
    """
    Aqui tenho 3 parametros posicionais e 2 nomeados 
    """


    todos_params('Nada', False, [1,2,3], tamanho='M', fragil=True)
    '''
    'Nada', False, [1,2,3], parametro posicionais de tipos diferentes
    tamanho=M, fragil=True Parametros nomeados
    Sempre posicionais vem antes de nomeados se não da problema ou passa todos nomeados
    '''