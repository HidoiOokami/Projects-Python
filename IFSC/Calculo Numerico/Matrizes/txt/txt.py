arq = open('matriz.txt', 'r')  # abre o arquivo
texto = []
matriz = []
texto = arq.readlines()  # quebra as linhas do arquivo em vetores
print('')


for i in range(len(texto)):  # esse for percorre a posições dp vetor texto
    matriz.append(texto[i].split())  # aqui eu quebro nos espasos das palavras

# mostra o vertor com um conjunto de vetores
print("vetor matriz -> ", str(matriz).replace("'", ''))
print("")

'''
for i in range(len(texto)):  # mostra quedrando em linhas
    print(matriz[i])
'''
