"""
# 11. Genere el histograma que resulta de simular la suma del lanzamiento de 2 dados de 6 caras, genere esto para un N numero de repeticiones del experimento



"""

import matplotlib.pyplot as plt
import random

# Tupla aleatoria simulando los dados
n = 1000
conteo = 0
lista_lanzamiento = []
lista_suma = []

while conteo < n:

    numero_aleatorio = (random.randint(1,6), random.randint(1,6))
    suma = sum(numero_aleatorio)
    lista_lanzamiento.append(numero_aleatorio)
    lista_suma.append(suma)
    conteo +=1

print(lista_lanzamiento)
print(lista_suma)

# Histograma
bins = [i - 0.5 for i in range(2, 14)]
plt.hist(
    lista_suma, bins=bins, rwidth=0.8, edgecolor="black"
)
plt.title(f"Distribución de la suma de dos dados lanzados {n} veces")
plt.xlabel("Sumas de los dados")
plt.ylabel("Frecuencia ")
plt.xticks(range(2, 13))
max_y = max([lista_suma.count(x) for x in lista_suma])
plt.yticks(range(0, max_y + 20, 20))
plt.show()