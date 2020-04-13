import numpy as np

# O formulário da matriz já deve estar no formato [A | b]
# Onde 'A' é o sistema e 'b' é a saída
def jordan(matrix):
    np.asarray(matrix) # Garantindo uma matriz, asarray converte a entrada em uma matriz
    matrix = matrix.astype(float) # Garantindo que os dados de dada matriz sejam Flutuantes
    
    print('-=' * 60)
    print('\nA Matriz inicial A: \n')
    print(f'{matrix}\n')
    print('-=' * 60)

    ''' 
        A propriedade shape é geralmente usada para obter a forma atual de uma matriz, 
        mas também pode ser usada para remodelar a matriz no local, atribuindo-lhe uma 
        tupla de dimensões da matriz 
    '''
    n, m = matrix.shape # n = 3 m = 4

    print(f'\n{n} Linhas \n{m - 1} Colunas \n')
    print('-=' * 60)

    for i in range(0, n, 1):
        pivo = matrix[i, i] # Primeiro elemento e o pivo
        next_iten = i + 1 # Proximo
        for k in range(next_iten, n, 1):
            if (np.abs(matrix[k, i]) > 0): # if (np.abs(matrix[k, i]) >= 0):
                coeficiente = pivo / matrix[k, i]
                matrix[k,:] = matrix[k,:] * coeficiente - matrix[i, :]
                #print(F'\nDEBUG{matrix[k,:]}')
                #break
            else:
                ''' Tratando exceção da 1° linha e coluna '''
                coeficiente = 'Divisão por 0'
            
            print(f'\nCoeficiente: {coeficiente}\n')
            print(f'\n{matrix}\n')
            print('-=' * 60)

    print(f'\nEliminando triangular inferios\n')
    
    last_line = n - 1
    last_colunm = m - 1

    for i in range(last_line, 0 - 1, -1):
        # Normaliza o 1° elemento diagonal
        matrix[i, :] = matrix[i, :] / matrix[i, i]
        pivo = matrix[i, i] # 1° elemento da atula matriz
        # Para a linha 'i'
        previous = i - 1 # anterior 
        for k in range(previous, 0 - 1, -1):
            if (np.abs(matrix[k,i]) > 0):
                coeficiente = pivo / matrix[k, i]
                matrix[k, :] = matrix[k, :] * coeficiente - matrix[i, :]
            else:
                ''' Tratando exceção da 1° linha e coluna '''
                coeficiente = 'Divisão por 0'

            print(f'\nCoeficiente: {coeficiente}\n')
            print(f'\n{matrix}\n')
            print('-=' * 60)

    x = matrix[:, last_colunm]
    x = np.transpose([x])
    return x

