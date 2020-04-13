# Passando funcao com parametro para outra funcao com *

def calc(precoBruto, calcImposto, *parms): # não e obrigatorio passar
    return precoBruto + precoBruto * calcImposto(*parms) # Sera feito um Peking de *parms para passar como parametro virara uma tupla
    

def impostX(importado):
    # se for retorne if ternario
    return 0.22 if importado else 0.13

def imposto_y(explosivo, fatorMult = 1): # parametro  fatorMult = 1 e opcional se não for passado ira assumir valor 1
    # 0.11 * fatorMult se for explosivo se não for não tem imposto
    return 0.11 * fatorMult if explosivo else 0


if __name__ == '__main__':
    precoBruto = 134.98
    # se passar ** Dicionario tem que passar parametros nomeados e variaveis ou seja pode passar ou não mas se passar tem que ser nomeado
    # segundo parametro e função que eu desejo para calcular esse devido pedido
    # True e do parametro de impostoX
    precoFinal = calc(precoBruto, impostX, True)

    # em cima de impostoY True, 1.5 explosivo e o val de mult e 1.5
    precoFinal = calc(precoFinal, imposto_y, True, 1.5)

    print(f'Preço final R$ {precoFinal}')