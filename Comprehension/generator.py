
# generetors troca [] por () gera os dados sob demanda e menor que o comprehension que gera completo

generator = (i ** 2 for i in range(10) if i % 2 == 0) #i ** 2 == i² se for verdadeiro elevo ao ² valor de i
#print(next(generator)) #Saida 0
#print(next(generator)) #Saida 4 
#print(next(generator)) #Saida 16
#print(next(generator)) #Saida 32
#print(next(generator)) #Saida 64 proximo da erro

# Com for
for num in generator:
    print(num)