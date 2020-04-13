
# Passando função como parametro
# if ternario <expressao1> if <condicao> else <expressao2>
def executar(funcao): # Verificando se e valido
    if callable(funcao):
        funcao()
    else:
        print("Parametro não suportado")

def bom_dia():
    print('Bom dia')

def boa_tarde():
    print('Boa Tarde')


if __name__ == "__main__":
    executar(1)
    executar(boa_tarde)