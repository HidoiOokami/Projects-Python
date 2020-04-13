'''
Operadores Aritmeticos
'''
print('Soma: ',           2 + 3)
print('Subtração: ',      4 - 7)
print('Divisão: ',        9.4 / 3)
print('Div n° inteiro: ', 9.4 // 3) # Obrigando a dar n° inteiro
print('Expoente: ',       2 ** 8)   # exponenciação elevando 2 a 8 potencia
print('Resto: ',          10 % 3)   # resto da divisão 

print('\n')
''' 
Operadores Relacionais

'''
print(3 > 4)    #False
print(4 >= 3)   #False
print(1 < 2)    #True
print(3 <= 1)   #False
print(3 != 2)   #True
print(3 == 3)   #True
print(2 == '2') #False

print('\n')

'''
Operadores de Atribuição
'''
a = 0 # o a ira assumir o valor de cada uma das execuções anterios

a -= 3
print(a)

a *= 2
print(a)

a /= 2
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

print('\n')

'''
Operadores de Logicos

and == && or == ||

'''

# verdadeiro ou falso
print(True or False)  #Retorna True
print(7 != 3 and 2 > 3)

# Negação de um operador
not 0 #False
not 1 #True

not not -1 #true
not not True #True

#Operadores bit a bit
True & False # False
False | True # True
True ^ False # True 

#Exemplo Binario
# 3 = 11 AND
# 2 = 10
# _ = 10 se
3 & 2

# 3 = 11 OR
# 2 = 10
# _ = 11 se
3 | 2

# 3 = 11 XOR
# 2 = 10
# _ = 01 se
3 ^ 2


'''
Operadores Ternarios
'''

esta_chovendo = True
# Nesse caso True assume porque e o que esta mais proximo da variavel e False seria o contrario
print('Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chovendo])

#if ternario Hoje estou com as roupas molhadas se estiver chovendo caso contrario estou com as roupas secas 
print('Hoje estou com as roupas ' + ('molhadas') if esta_chovendo else 'secas')

'''
Operador de Membro
'''

lista = [1, 2, 3, 'Ana', 'Liza']

print(2 in lista) # True
print('Ana' not in lista) #False

#Operador de identidade
print('\n Operador de identidade \n')
x = 3
y = x
z = 3

print(x is y) # como o valor de ambas e o mesmo ira dar True Listas nesse caso são diferentes
print(y is z)