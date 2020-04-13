#-*- coding: utf-8 -*-
#!/usr/local/bin/python3

from datetime import datetime

class Tarefas:

    def __init__(self, descricao):
        self.descricao = descricao
        #Inicializando outros attr dentro do construtor
        self.feito = False # Verifica se a tarefa foi concluida
        self.criacao = datetime.now() #Pegando data atual

    #Metodos
    def concluir(self):
        self.feito = True

    def __str__(self):
        #Saida bonita se a tarefa for True
        return self.descricao + (' - (Concluída)' if self.feito else ' - (A fazer)')

def main():
    casa = []   
    casa.append(Tarefas('Passar roupa'))
    casa.append(Tarefas('Lavar louça'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar louça']

    for tarefa in casa:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()