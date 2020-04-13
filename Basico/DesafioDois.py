'''
Desafio Dois
'''

terca = False
quinta = False

tv_50  = terca and quinta
tv_32  = terca != quinta
sorvete = terca or quinta
saude  = not sorvete

print("TV 50' {}  TV 32' {} Sorvete {} Saude {}" .format(tv_50, tv_32, sorvete, saude))