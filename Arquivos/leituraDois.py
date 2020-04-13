#strip tira os espaços em branco nas bordas da string posso tirar um elemento em expecifico
#strip('elemento)
# fazendo  stream para não carregar o  arquivo todo
arquivo = open('pessoas.csv')


for registros in arquivo.splitlines(): # para dividir as linhas certinho
    print("Nome: {} Idade: {}" .format(*registros.strip().split(','))) #separando a string pela ,
    # o * extrai as informações do arquivo no caso para os dois dados la de dentro


arquivo.close()