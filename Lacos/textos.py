#Constanstes maiusculas

#PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política') # tupla
PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'} #set
textos = [
    'João gosta de futebol e política',
    'A praia foi legal'
]

#Verificando se a palavras proibidas dentro da lista
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split())) #Se houver palavras iguais saia
    
    if intersecao:
        print("Possui palavras proibidas:", intersecao)
    else:
        print('Nenhuma palavra', texto)

    '''
    for palavra in texto.lower().split(): # deixando tudo minusculo separando por padrão pelos espaços
        # verificando dentro da tupla
        if palavra in PALAVRAS_PROIBIDAS:
            print("possui", palavra)
            
            break

    else:
        print('Nenhuma palavra', texto)'''
