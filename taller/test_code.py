"""
Realizar un algoritmo que transforme numeros romanos a numeros decimales

Consideraciones:
1. Los símbolos se escriben de izquierda a derecha de MAYOR a MENOR valor
2. Los números romanos representan solo enteros positivos
3. De Mayor a menor: M=1000, D=500, C=100, L=50, X=10, V=5, I=1
4. Si una letra está seguida por otra de igual o menor valor ENTONCES sus valores se suman. EJP: CX -> 100 + 10
5. Si una letra está seguida por otra de mayor valor ENTONCES sus valores se restan. EJP: XC -> 100 - 10

Algoritmo:
1. Solicitar al usuario un número romano r
2. Convertir r en una lista_romanos
2.1 Convertir todos los elementos de lista_romanos en mayúsuclas
3 Declarar un diccionario valores_romanos asociando cada letra al valor entero correspondiente
4. Añadir a una lista_enteros los valores del diccionario asociados a cada letra en lista_romanos en orden 
5.0 Si lista_enteros[i] > lista_enteros[i+1] 
5.0.1 Entonces sumar lista_enteros[i] + lista_enteros[i+1]
5.0.2 añadir el valor de la suma  5.0.1 a total
5.1 Si lista_enteros[i] <= lista_enteros[i+1]
5.1.1 Entonces restar lista_enteros[i+1] - lista_enteros[i]
5.1.2 Entonces añadir el valor de la resta 5.1.1 a total 
6.0 Imprimir valor total una vez terminado el ciclo


"""


r = 'LXIV'
lista_romanos = list(r)
lista_romanos = [letra.upper() for letra in lista_romanos]
lista_enteros = []
#Utilización de diccionari0 para hacer el recorrido más rápido
valores = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
total = 0

#Recuperar valores del diccionario con comprensión de listas
lista_enteros= [valores[letra] for letra in lista_romanos]
#Detenerse en el penúltimo debido al uso del sucesor i+1
for i,numero in enumerate(lista_enteros):
    if i+1 < len(lista_enteros) and lista_enteros[i] < lista_enteros[i+1]:
        total -= lista_enteros[i]
    else:
        total+= lista_enteros[i]
print(total)


