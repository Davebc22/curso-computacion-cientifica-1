"""
Realizar un algoritmo que transforme números decimales a números binarios
Comprensión del problema:
Un número decimal es un número representado a través de 10 símbolos: 0,1,2,3,4,5,6,7,8,9
Un número binario es represtando a través de 2 símbolos: 0,1

Algoritmo:
1. Pedir al usuario el valor de n
2. Guardar k = n//2 
3. Guardar residuo = n%2
4. asignar n = k 
5. si n = 1 entonces terminar 
6. si n != 1 Volver a 1.
"""

n = int(input('inserte un número entero '))
binario = []
k=0

while(n>0):
    k = n//2
    residuo = n%2
    n=k
    binario.append(residuo)
# * para desempaquetar la lista & ::-1 para recorrer de último a primero
print(*binario[::-1])
