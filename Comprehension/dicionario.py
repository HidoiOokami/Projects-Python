
# Dicionario com list comprehension

# Chave i: valor i * 2
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

# usando for
for numero, dobro in dicionario.items():
    print(f"{numero} x 2 = {dobro}")