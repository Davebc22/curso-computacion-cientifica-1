"""
# 5. Realiza un algoritmo que valide si una frase es un palindromo
ejp: luz azul
Algoritmo
1. Pedir al usuario una palabra p
2. Volver la palabra p una lista l1
3. invertir lista l2
4. Evaluar si l1 = l2
4.1 Si sí: l1 es palíndromo
4.2 si no: l1 no es palíndromo
"""
palabra = input('Inserte una palabra ')
palabra.lower()
lista1 = list(palabra.replace(" ", ""))
lista2 = lista1[::-1]

if lista1 == lista2:
    print(f'La frase/palabra "{palabra}" SÍ es un palíndromo')
else: 
    print(f'La frase/palabra "{palabra}" NO es un palíndromo')