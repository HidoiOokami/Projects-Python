#-*- coding: utf-8 -*-
#!/usr/local/bin/python3

'''
Python trata encapsulamento da mesma forma que JS com uma convenção usando o _ para dizer a visibilidade de tal obj
'''

from datetime import datetime, timedelta

# tratando excessão de erros
class Error(Exception):
    pass

class Projeto:
    def __init__(self, nome):
        self.nome    = nome
        self.tarefas = []
    
    #metodo privado **kwargs e para manter os mesmos parametros nos metodos privados
    def _add_tarefa(self, tarefa, **kwargs): 
        self.tarefas.append(tarefa)
        

    def _add_nova_tafera(self, descricao, **kwargs):
        self.tarefas.append(Tarefas(descricao, kwargs.get('vencimento', None))) # kwargs.get('vencimento', None) verificando se tem o met nos vencimentos se ñ traga Nada none

    # Metodo magico sobrecarrega de operador +=
    # projeto += tarefa
    def __iadd__(self, tarefa):
        tarefa.dono = self # Setamos o dono da tarefa/
        self._add_tarefa(tarefa)
        return self # retornando proprio projeto

    #Criando uma nova tarfea só passando a descrição
    def add(self, tarefa, vencimento = None, **kwargs):
        # aqui vai depender da função escolhida na hora do chamado do metodo
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefas) else self._add_nova_tafera# só chamo essa se o parametro tarefa for do tipo da Classe Tarefas
        # isinstance(tarefa, Tarefas) aqui o primeiro e o tipo e o segundo e a que eu quero comparar
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)


    # Metodo magico a agora a interação com a lista sera feita por ele
    def __iter__(self):
        return self.tarefas.__iter__()


    def pendentes(self):
        # Retornando um ListComprerension
        return [tarefas for tarefas in self.tarefas if not tarefas.feito]

    def procurar(self, descricao):
        # Lançando excessão
        try:
            return [tarefas for tarefas in self.tarefas 
                    if tarefas.descricao == descricao][0] # vai procurar e se achar traga a 1° que achou
        except IndexError as e: # e e um apelido
            raise Error(str(e))

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
        self.dono = None

    # modificando metodo já existente com super para se referenciar aos obj da classe pai
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorente(self.descricao, novo_vencimento, self.dias)
        # Verifica se esta setado
        if self.dono:
            # Adicionando ao dono nova tarefa criada
            self.dono += nova_tarefa
        return nova_tarefa



def main():
    # Instanciando
    casa = Projeto('Tarefas de Casa')
    # Adicionando tarfeas
    casa.add('Passar roupa', datetime.now()) # passando data de vencimento
    casa.add('Passar pano no chao', datetime.now() + timedelta(days = 3, minutes = 12))
    # essa tarefa ja tem como dono projeto casa
    casa += TarefaRecorente('Tirar leite', datetime.now(), 7)
    casa.procurar('Tirar leite').concluir()
    # Mostrando
    print(casa)

    try:
        casa.procurar('Lavar pratos').concluir()
    except Error as e:
        print(f'A cauda foi: {str(e)}')

    # Procurando tarefa e concluindo ela
    #casa.procurar('Passar roupa').concluir()
    for tarefas in casa: # casa.tarefas não a necessidade de usar mais assim por causa do metodo magico iter que agora e responsavel pela interação com esse obj 
        print(f'- {tarefas}')

    # Mostrando
    print(casa)

if __name__ == '__main__':
    main()