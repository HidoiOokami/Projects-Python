
#Comprehension e uma forma de criar listas de forma concisa ou seja melhor

# [ ] comessa assim

dobros = [i * 2 for i in range(10)] #Começa com a expressão i * 2 ai vem o laço e uma condicional
print(dobros)

#jeito normal 
normal = []

for i in range(10):
    normal.append(i * 2)
print(normal)

dobro = [i * 2 for i in range(10) if i % 2 == 0] #Começa com a expressão i * 2 ai vem o laço e uma condicional
print(dobro)

