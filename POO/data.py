
class Data:

    # Contrutor nome magico __init__
    def __init__(self, dia = 3, mes = 7, ano = 1997):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    #Metodo especial que converte para str
    #self objeto que esta sendo usado nesse momento e um this
    def __str__(self): # metodo magico
        return f'{self.dia}\{self.mes}\{self.ano}'

#Instancia
data = Data(5, 12, 2019) # posso ou não passar os dias
dataUm = Data() 
dataDois = Data(mes=12) #modificando só o mes
# Não a necessidade de definir atributos 
# na classe o python deixa eu manipular dados 
# que não foram indexados como atributos da classe
#data.dia = 5
#data.mes = 12
#data.ano = 2019

# Chamando de forma implicita ele ira procurar o __str__
print(data) # por ser um metodo suportado por todos os obj do py não preciso chamalo
print(dataUm)
print(dataDois)

