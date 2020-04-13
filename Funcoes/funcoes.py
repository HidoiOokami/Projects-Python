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
def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == "__main__":
    # Teste (assertion) se for verdadeira a condição passa se não for gera um erro
    assert tag_bloco('Incluindo com sucesso') == '<div class="success">Incluindo com sucesso</div>'

    assert tag_bloco('Impossivel excluir', 'error') == '<div class="error">Impossivel excluir</div>'

print(tag_bloco('bloco'))
    