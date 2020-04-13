#-*- coding: utf-8 -*-
#!/usr/local/bin/python3

from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome    = nome
        self.tarefas = []
    #Criando uma nova tarfea só passando a descrição
    def add(self, descricao):
        self.tarefas.append(Tarefas(descricao))

    # Metodo magico a agora a interação com a lista sera feita por ele
    def __iter__(self):
        return self.tarefas.__iter__()


    def pendentes(self):
        # Retornando um ListComprerension
        return [tarefas for tarefas in self.tarefas if not tarefas.feito]

    def procurar(self, descricao):
        return [tarefas for tarefas in self.tarefas 
                if tarefas.descricao == descricao][0] # vai procurar e se achar traga a 1° que achou

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())}) tarefas pendentes' #Ira trazer em numeros a quantidade de pendentes len(self.pendentes()


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
    # Instanciando
    casa = Projeto('Tarefas de Casa')
    # Adicionando tarfeas
    casa.add('Passar roupa')
    casa.add('Passar pano no chao')
    # Mostrando
    print(casa)

    # Procurando tarefa e concluindo ela
    casa.procurar('Passar roupa').concluir()
    for tarefas in casa: # casa.tarefas não a necessidade de usar mais assim por causa do metodo magico iter que agora e responsavel pela interação com esse obj 
        print(f'- {tarefas}')

    # Mostrando
    print(casa)

if __name__ == '__main__':
    main()