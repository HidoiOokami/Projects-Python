# Parametros opcionais classe e opicional se não passar  tomara coomo padrao
# args são os argumentos ou propriedades do conteudo
def tag_bloco(conteudo, *args, classe='success', inline=False): #para alternar entre span e div
    tag = 'span' if inline else 'div' # if ternario
    html = conteudo if not callable(conteudo) else conteudo(*args) # html recebe conteudo se ele não for uma função
    # Caso ele seja chamo ele como um metodo função e passo os parametros que uma tupla
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens) #começa vazia e cada vez que for inserida alguma coisa comcatena coma lista
    # dentro do join o que eu quero que gere ali em cima (f'<li>{item}</li>' for itrm in itens) é um generetor
    # Como ele está dentro de () da função ele ja se comportara como um generetor
    return f'<ul>{lista}</ul>' # Dentro do retorno tera a lista que possui os li que ira dentro de um ul


if __name__ == "__main__":
    
    print(tag_bloco('bloco'))
    print(tag_bloco('1° Texto', classe='info', inline=False))
    print(tag_bloco('texto', inline=True))
    print(tag_bloco('Error', classe='error'))
    # Passando á tag_bloco como parametro uma função que fara o packing de mais de um dado para passar
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='Table', inline=False))

    # testando passagem de função com parametro função se tivermos parametros com * temos que passar os demais 
    # sempre referenciando classe='info' ou seja parametro nomeado
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info', inline=True))
    