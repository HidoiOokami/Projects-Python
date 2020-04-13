
#Retornando lista e Dicionarios de uma função
# poderia passar da seguinte forma
"""
nums = (1,2,3) # poderia ser uma lista
print(soma(*nums)) #Nesse caso iria desempacotar e somar a tupla para passar os dados
"""

def soma(*numeros): #Como aqui espera uma tupla empacotamento
    soma = 0
    for n in numeros:
        soma += n
    return soma

'''
Dicionario ou seja passando com **kwargs
'''
def resultado(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')

if __name__ == '__main__':
    #print(soma(1))
    #print(soma(1, 3)) # Posso passar quantos valores quiser
    # chave valor dicionario
    resultado(primeiro='Bed',
              segundo='Kirudinha',
              terceiro='Nagui')







