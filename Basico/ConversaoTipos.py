'''
Conversão de Tipos
'''
a = 3
b = '2'

print(int(b) + a)
print(b + str(a))
print(2 + float(2.2))

'''
Coerção Automática
'''

print(10 / 2) #3 ele gera a converção automatica para float para a gente 
print(2 + True)  # Nesse caso ele assume que o True e 1 então retorna 3
print(2 + False) # Retorna 2 porque False e 0

# verificando tipo variavel
b = 10.0
print(b.is_integer()) 

#abs() e potrncia

#acessando posição de uma String
nome = 'Bed' # String e imultavel não muda só o valor da variavel
nome[0] # Tras B