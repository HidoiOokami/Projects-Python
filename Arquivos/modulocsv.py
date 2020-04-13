import csv

# tras pronto para leitura já
with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada): #reader leitor 
        print("Nome: {}, Idade: {}" .format(*pessoa))
