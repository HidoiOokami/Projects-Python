'''
Interpolação de dados
'''
from string import Template

nome, idade = 'Bed', 21

print('Nome: %s \nIdade: %d' % (nome, idade))
#print('Nome: %s \nIdade: %.2f' % (nome, idade)) # para arrendondar com duas casa ponto flutuante

print('Nome: {} \nIdade: {}' .format(nome, idade)) # pode ter indice dentro {}

print(f'Nome: {nome} \nIdade: {idade}')

s = Template('Nome: $n \nIdade: $i')
print(s.substitute(n=nome, i=idade))