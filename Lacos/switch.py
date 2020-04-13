
#Simulando switch
def days(day):
    #Usando dicionario para simular
    days = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    # retornando dia selecionado
    return days.get(day, 'Dia invalido') #Segundo parametro seria o default

def typeDays(day):
    days = {
        1: 'Inicio de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Meio de Semana',
        5: 'Dia de Semana',
        6: 'Final de Semana',
        7: 'Final de Semana'
    }
    # retornando dia selecionado
    return days.get(day, 'Dia invalido') #Segundo parametro seria o default


if __name__ == "__main__":
    for day in range(8):  
        print(f"{day}: {days(day)}")
        print(f"{day}: {typeDays(day)}")





