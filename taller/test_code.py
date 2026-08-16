"""
Realizar un algoritmo que transforme números binarios a números decimales

Algoritmo:

1. Solicitar al usuario un número n expresado en forma binaria
2. Convertir en una lista 1 el número n dado 
3. Leer el número k de dígitos del número n dado
4. Guardar en una lista 2 las potencias de 2 que van desde la potencia 0 hasta la potencia k-1
4.1 Invertir orden de la lista
5. Comparar los elementos de la lista 1 y lista 2:
5.1 Si lista 1 (i) == 1 entonces guardar en lista 3 el elemento lista 2 (i)
5.2 Si lista 1 (i) == 0 entonces descartar
6. Sumar los elementos de lista 3

"""


n='10010110000'
# Comprensión de lista para convertir un string a una lista de enteros
lista_n = [int(caracter) for caracter in n]
k=len(lista_n)
lista_p2 = [2**numero for numero in range(k)]
lista_p2 = lista_p2[::-1]
lista_final = []

for i,numero in enumerate(lista_n):
    if numero == 1:
        lista_final.append(lista_p2[i])

print(lista_n)
print(lista_p2)
print(lista_final)
lista_final = sum(lista_final)
print(lista_final)


