# Parametros opcionais classe e opicional se não passar  tomara coomo padrao
def tag_bloco(conteudo, classe='success', inline=False): #para alternar entre span e div
    tag = 'span' if inline else 'div' # if ternario
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens) #começa vazia e cada vez que for inserida alguma coisa comcatena coma lista
    # dentro do join o que eu quero que gere ali em cima (f'<li>{item}</li>' for itrm in itens) é um generetor
    # Como ele está dentro de () da função ele ja se comportara como um generetor
    return f'<ul>{lista}</ul>' # Dentro do retorno tera a lista que possui os li que ira dentro de um ul


if __name__ == "__main__":
    
    print(tag_bloco('bloco'))
    print(tag_bloco('1° Texto', '2° Classe', False))
    print(tag_bloco('texto', inline=True))
    print(tag_bloco('Error', classe='error'))
    # Passando á tag_bloco como parametro uma função que fara o packing de mais de um dado para passar
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='Table', inline=False))
    