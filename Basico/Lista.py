'''
Listas
'''

lista = []

#vendo funções que alista suporta informações
dir(lista)
help(lista)

# tamanho da lista
len(lista)

#adicionadondo valores
lista.append(1)

nova_lista = [1, 2, 'Bed', 'kill'] # heterogenia qualquer tipo de valor
nova_lista.remove(2) #ira remover o valor 2

nova_lista.reverse() # Aqui e mutavel pode alterar a lista de tras para frente 

# index tras a posição do elemnto
nova_lista.index('Bed') # tras 2 posição 2 podemos usar o in Bed in nova_lista = True
# ultimo elemento da lisra nova_lista[-1]


#Intervalo da lista
nova_lista[1:3] #comeca no indice um e vai ate o 2 o tres nesse caso não conta
nova_lista[1:-1] # vai ate o pnultimo
nova_lista[1:] # ate o final
nova_lista[::2] # de dois em dois
nova_lista[::-1] # Tras para frente
del nova_lista[1] # deleta elemento de indice 1
del nova_lista[1:] # deleta todos elementos de indice 1 em diante