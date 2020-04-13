
#leitura com bloco with


#strip tira os espaços em branco nas bordas da string posso tirar um elemento em expecifico
#strip('elemento)
# fazendo  stream para não carregar o  arquivo todo

#tratando erro
 
#with == com open('pessoas.csv') as arquivo: referenciando o csv com a variavel arquivo
with open('pessoas.csv') as arquivo: #as e uma mensão estou dizendo que o open esta em arquivo
    # abrindo em mode de escrita
    with open('pessoas.txt', 'w') as saida: # segundo parametro e passado dizendo omodo que o arquivo sera aberto leitura escrita == w...
        for registros in arquivo: # para dividir as linhas certinho
            pessoa = registros.strip().split(',')
            print("Nome: {} Idade: {}" .format(*pessoa), file=saida) #separando a string pela ,
            # o * extrai as informações do arquivo no caso para os dois dados la de dentro
            # file=saida da função print quer dizer que ao invez de eu imprimir no console vou imprimir 
            # no arquivo txt nesse caso
# nesse caso garante que o arquivo será fechado com with
if arquivo.closed:
    print('Arquivo fechado')


if saida.closed:
    print('Arquivo de saida fechado')