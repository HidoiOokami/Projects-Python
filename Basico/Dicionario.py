'''
Chaves e Valores Dicionario
'''

pessoa = {
    'nome'   : 'Prof Ana',
    'idade'  : 38,
    'cursos' : ['Ingles', 'Frances']
}

print(pessoa)

len(pessoa) #tamanho

print(pessoa['nome']) #assim acesso a item

print(pessoa['cursos'][0]) #assim acesso a item

print(pessoa.keys()) # tras os identificadores de cada valor nome-idade-cursos
print(pessoa.values()) # só os valores
print(pessoa.items()) #cada item
print(pessoa.get('idade'))

# caso não encontre retorne um arrey vazio
print(pessoa.get('tags', [])) # tags não existe

'''
Manipulando dicionarios
'''

pessoa = {
    'nome'   : 'Gabriel',
    'idade'  : 27,
    'cursos' : ['React', 'Python']
}


#alterando valor de idade
pessoa['idade'] = 21
pessoa['cursos'].append('JavaScript')


#lendo e tirando valor de dentro doo dicionario
pessoa.pop('idade')
#Adicionando pessoa
pessoa.update({'idade' : 27, 'Sexo' : 'M'})
#Deletando Pessoa
del pessoa['cursos']
#Limpando dicionario
pessoa.clear()
print(pessoa)