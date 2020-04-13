
#Simulando switch

def get_type_day(day):
    # Cada chave sera uma tupla
    days = {
        # 1, 7 e domingo e sabado ou seja fim de semana
        (1, 7):    'Fim de Semana', 
        # de segunda a sexta
        tuple(range(2, 7)): 'Dia de Semana',
    }

    # criando generetor para fericar dia retorna types que e o dia da semana 
    # number e a tupla e os numeros da semana types e o tipo daquele dia
    # no dicionario days.items() percorre os dois elementos ao mesmo tempo chave e valor
    # if day in number se o parametro do metodo get_type_day e um numero valido da semana
    day_selected = (types for number, types in days.items() if day in number)
    return next(day_selected, "Dia invalido")

if __name__ == "__main__":
    for day in range(0, 9):
        print(f"{day}: {get_type_day(day)}")
