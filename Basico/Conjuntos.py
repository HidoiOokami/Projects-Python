'''
Semelhante a lista não garante ordem não e indexado não acaita elementos repetidos
'''

a = {1, 2, 3} # usando {} e um set

a = set('Bed') # cria uma estrutura com cada uma das letras
print(a) # não garante ordenação

# a str 3 esta presente em a? E 4 não esta presente em a?
print('3' in a, 4 not in a)

{1,2,3} == {1,3,2,2} # São iguais ele ignora os repetidos e não liga para a ordem 

#Operações unindo conjuntos
c1 = {1,2}
c2 = {2,3}

print(c1.union(c2))

#Elementos comuns aos dois
print(c1.intersection(c2))

#atualizando contunto 1 com dados do dois
c1.update(c2)

# Verificando se um conjunto e subconjunto de outro
print(c2 <= c1)
# Superconjunto
print(c1 >= c2)

#Atribuição subtrativa
c1 -= {2}