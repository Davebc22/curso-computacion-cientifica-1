"""
Parcial - Punto 3
"""
import random
import matplotlib.pyplot as plt

simulaciones = 10000
asientos_finales_100 = []

for simulacion in range(simulaciones):
    #Condción Inicial
    asientos_libres = list(range(1, 101))
    asientos_ocupados = []

    #Pasajero 1
    distraido = random.randint(1,100)
    asientos_ocupados = [distraido]
    asientos_libres.remove(distraido)

    # Segundo Escenario: Pasajeros del 2 al 100
    for pasajero in range(2,101) :
        if pasajero in asientos_libres:
            asientos_ocupados.append(pasajero)
            asientos_libres.remove(pasajero)
        else:
            asiento_azar = random.choice(asientos_libres)
            asientos_ocupados.append(asiento_azar)
            asientos_libres.remove(asiento_azar)

    #Registro de posiciones dle pasajero 100
    pasajero_100 = asientos_ocupados[-1]
    asientos_finales_100.append(pasajero_100)

# PUNTO 1:
exitos = asientos_finales_100.count(100)
probabilidad = exitos / simulaciones
print(f"Probabilidad estimada de que el pasajero 100 se siente en su sitio: {probabilidad*100}%")

# PUNTO 2:
plt.hist(asientos_finales_100,bins=range(1,102), edgecolor ="black", align="left", color="purple",)
plt.title("Distribución de Frecuencia del asiento del pasajero 100")
plt.xlabel("Número de Asiento en el que se sentó")
plt.ylabel("Frecuencia - Número de Simulaciones")
plt.show()