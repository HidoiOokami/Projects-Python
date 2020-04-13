'''
String
'''

nome = "Ana Paula"

nome[0] # Tras A
nome[6] # Tras u
nome[-3] # Tras Au começa de tras para frente
nome[4:] # Começando apartir do 4 Paula 
nome[-5:] # Começa de tras para frente tras Paula também
nome[:3] # Começa do 3 mas ele mesmo não conta tras Ana indice 0 1 e 2 
nome[2:5] #tras a P porque o 5 não entra

nome[::] #tras todos
nome[::2] #Pulando dois em dois 
nome[1::2] #começando 1 e saltando de 2 em 2
nome[::-1] #inverte a String passo nesse caso e negativo 
'''
Consigo usar operador membro em str
'''
frase = 'Python'

'py' not in  frase # True
len(frase) # tamanho da frase
frase.lower() # tudo minusculo
frase.upper() # tudo maiusculo
frase.split() #quebra a frase nos espaços
frase.split('y') #quebra no y