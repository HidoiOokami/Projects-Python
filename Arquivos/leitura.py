

arquivo = open('pessoas.csv')

dados = arquivo.read()

arquivo.close()

for registros in dados.splitlines(): # para dividir as linhas certinho
    print("Nome: {} Idade: {}" .format(*registros.split(','))) #separando a string pela ,
    # o * extrai as informações do arquivo no caso para os dois dados la de dentro