#!usr/local/bin/python3
'''
    --Função

    - Parametro nomeado
    - Parametro posicional
    - Parametros opcionais


    tipos especiais de argumento, são dois 
    sendo que os nomes podem ser derivados mas o importante são os *

    *args    -> retorna uma tupla
    **kwargs -> retorna um dicionario

    muito loko!

'''

# Parametros opcionais classe e opicional se não passar  tomara coomo padrao
def tag_bloco(texto, classe='success', inline=False): #para alternar entre span e div
    tag = 'span' if inline else 'div' # if ternario
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == "__main__":
    
    print(tag_bloco('bloco'))
    print(tag_bloco('1° Texto', '2° Classe', False))
    print(tag_bloco('texto', inline=True))
    print(tag_bloco('Error', classe='error'))
    