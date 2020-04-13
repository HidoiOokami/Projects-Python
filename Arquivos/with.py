
#leitura com bloco with


#strip tira os espaços em branco nas bordas da string posso tirar um elemento em expecifico
#strip('elemento)
# fazendo  stream para não carregar o  arquivo todo

#tratando erro
 
#with == com open('pessoas.csv') as arquivo: referenciando o csv com a variavel arquivo
with open('pessoas.csv') as arquivo: #as e uma mensão estou dizendo que o open esta em arquivo
 
    for registros in arquivo: # para dividir as linhas certinho
        print("Nome: {} Idade: {}" .format(*registros.strip().split(','))) #separando a string pela ,
        # o * extrai as informações do arquivo no caso para os dois dados la de dentro

# nesse caso garante que o arquivo será fechado com with
if arquivo.closed:
    print('Arquivo fechado')
