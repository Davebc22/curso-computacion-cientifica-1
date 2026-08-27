"""
# 6. Realiza un algoritmo que cuente la cantidad de ocurrencias de cada caracter en una frase


"""

palabra = input('Escriba una frase o palabra: ')
palabra = palabra.lower()
lista1 = list(palabra.replace(" ", ""))

for caracter in set(lista1):
    cantidad = lista1.count(caracter)
    print(f'{caracter} : {cantidad}')