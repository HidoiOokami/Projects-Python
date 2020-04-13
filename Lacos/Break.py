

for x in range(1, 11):
    if x % 2 == 0:
        # interrompendo a iteração para ir para proxima
        continue
    print(x) # ira imprimir todos os impares porque o continue toda vez que e para manda interropen

print("\n\n")
for x in range(1, 11):
    if x == 5:
        break
    print(x)


# For com else
print("\n\n")
for i in range(1, 11):
    if i == 6: break
    print(i)

else:
    print("Fim!")

