

class Humano:

    #Atributo da classe
    especie = 'Homo Sapiens'

    #Construtor
    def __init__(self, nome):
        self.nome = nome

    # metodos de instancia recebe Instancia self
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        #retornando o proprio objeto
        return self

    # metodo estatico não recebe parametros usa um decoretor
    @staticmethod
    def especies():
        especiesHumanos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        # para ser uma tupla passar ,
        return ('Australopiteco',) + tuple(f'Homo {especie}' for especie in especiesHumanos) # concatenando para começar com Homo

    # metodo de classe recebem uma classe como parametro tambem tem um decoretor cls e convencao de class
    @classmethod
    def evolucao(cls):
        # Verificando se e a ultima especie retornada 
        return cls.especie == cls.especies()[-1] # O retorno do metodo e uma tuple por isso [-1] pega o ultimo elemento

class Neanderthal(Humano):
    # Pegando do metodo especies o Neanderthal que e o penultimo
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    # Pegando do metodo especies o HomoSapiens que e o ultimo
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = Humano('José')
    bed  = Humano('Bed').das_cavernas() #self.especie = 'Homo Neanderthalensis' foi setado tomando a especie global
    # Poderia passar assim para dizer que ele e das cavernas
    # Humano.das_cavernas(jose)

    print(f'Evolucao (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolucao (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.evolucao()}') # True
    print(f'Neanderthal evoluido? {Neanderthal.evolucao()}') # False