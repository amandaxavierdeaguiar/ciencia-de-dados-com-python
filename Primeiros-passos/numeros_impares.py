#Exiba apenas os numeros ímpares.

for numero in range(100):
    if (numero % 2 == 0):
        continue

    print(numero, end = ' ')
