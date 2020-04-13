
import csv
from urllib import request # Passar o caminho do arquivo baixado 


def read(url):
    #Pegando arquivo remotamente
    with request.urlopen(url) as entrada:
        print('Baixando arquivo CSV...')
        #Decondig
        dados = entrada.read().decode('latin1')
        print('Dowload do arquivo CSV completo"')
        
        for cidade in csv.reader(dados.splitlines()): # separo por linhas
            # Pegando os indices especificos do desafio coluna 9 e 4
            print(f"{cidade[8]}: {cidade[3]}")

if __name__ == "__main__":
    #Passando url o print(r"") isso ignora os caracters especiais
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')           
            

