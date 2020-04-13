#-*- coding: utf-8 -*-

from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome    = nome
        self.tarefas = []
    #Criando uma nova tarfea só passando a descrição
    def add(self, descricao, vencimento = None):
        self.tarefas.append(Tarefas(descricao, vencimento))

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

    def __init__(self, descricao, vencimento = None):
        self.descricao = descricao
        #Inicializando outros attr dentro do construtor
        self.feito = False # Verifica se a tarefa foi concluida
        self.criacao = datetime.now() #Pegando data atual
        self.vencimento = vencimento


    #Metodos
    def concluir(self):
        self.feito = True

    def __str__(self):
        #Saida atendendo as condições
        status = []
        if self.feito: # Se for verdadeiro
            status.append(' - (Concluída)')
        elif self.vencimento: # se for passado o vencimento 
            if datetime.now() > self.vencimento:
                status.append(' - (Vencida)')
            else:
                # Pegando quantos dias faltam para vencer
                dias = (self.vencimento - datetime.now()).days
                status.append(f' - (Vence em: {dias} dias)')
        # retorna a descricao e retorma com status
        return f'{self.descricao}' + ' '.join(status)


# Classe que ira herdar de tarefas por padrã oe o Object
# Ira definir os vencimentos das tarefas
class TarefaRecorente(Tarefas):
    def __init__(self, descricao, vencimento = None, dias = 7):
        # referenciando a classe pai
        super().__init__(descricao, vencimento=vencimento)
        self.dias = dias

    # modificando metodo já existente com super para se referenciar aos obj da classe pai
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorente(self.descricao, novo_vencimento, self.dias)






def main():
    # Instanciando
    casa = Projeto('Tarefas de Casa')
    # Adicionando tarfeas
    casa.add('Passar roupa', datetime.now()) # passando data de vencimento
    casa.add('Passar pano no chao', datetime.now() + timedelta(days = 3, minutes = 12))
    # Mostrando
    print(casa)

    # Procurando tarefa e concluindo ela
    #casa.procurar('Passar roupa').concluir()
    for tarefas in casa: # casa.tarefas não a necessidade de usar mais assim por causa do metodo magico iter que agora e responsavel pela interação com esse obj 
        print(f'- {tarefas}')

    # Mostrando
    print(casa)

if __name__ == '__main__':
    main()