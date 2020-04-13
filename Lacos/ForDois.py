#-*- coding: utf-8 -*-

palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end = ", ") # imprimir na mesma linha


print('\n')
aluno = ["Gabriel", 'José', 'Rodrigo', 'Rubens']

for nome in aluno:
    print(nome)


print('\n')
# percondo nome e indice
for indice, nome in enumerate(aluno):
    print(indice + 1, nome)

# tupla
print('\n')
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

for dias in dias_semana:
    print(dias)

#set embaralhado
print('\n')
for letra in set('Hello World!'):
    print(letra) 


#for percorendo dicionario
print('\n')
dicionario = {
    'nome': 'Caneta',
    'preco': 14.99,
    'importada': True,
    'estoque': 793 
}

for index, nome in enumerate(dicionario):
    print(f"{index + 1} = {nome}")

#for percorendo dicionario trazer chave .keys() não a necessidade
print('\n')

for chave in dicionario:
    print(chave)

#for percorendo dicionario trazer valor
print('\n')

for valor in dicionario.values():
    print(valor)

#for percorendo dicionario trazer chave e valor
print('\n')

for chave, valor in dicionario.items():
    print(chave, '=', valor)
# os valores chave e valor estão disponiveis fora do bloco do for insano
print('\n')
print(chave, valor)