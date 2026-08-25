"""
Realizar un algoritmo que transforme numeros decimales a numeros romanos
Consideraciones:
Sean A,B elementos del conjunto de Números Romanos
a) Aumento de valor: Cuando una cifra A <= B se ubica a la derecha de B se suma: B+A
b) Disminución de valor: Cuando una cira A <= B se ubica a la izquierda de B se resta: B-A
c) Repetición: una cifra A puede repetirse hasta 3 veces de manera consecutiva
d) contar hasta el 4000 abierto, por una cuestión de notación


Ejemplo Guía: 2943
a) Ubicar el valor posicional del primer dígito (ie Millares, Centenas, Decenas,..) -> Millares
b) Asignar valor correspondiente -> MM
c) Ubicar el valor posicional del segundo dígito -> Centenas
d) Asignar valor correspondiente -> CM
e) Ubicar el valor posicional del tercer dígito -> Decenas
f) Asignar el valor correspondiente -> XL
...
g) Ubicar el valor posicional del último dígito -> Unidades
h) Asignar el valor correspondiente -> III
i) Unir asignaciones 
Romano: MMCMXLIII

Notar:
k = 1 -> Unidades
k = 2 -> Decenas
K = 3 -> Centenas
k = 4 -> Millares 

"""

def decimal_a_romano(numero):
	"""Convierte un entero positivo menor que 4000 a numeracion romana."""
	if numero <= 0 or numero >= 4000:
		print("El numero debe estar entre 1 y 3999")

	valores = (
		(1000, "M"),
		(900, "CM"),
		(500, "D"),
		(400, "CD"),
		(100, "C"),
		(90, "XC"),
		(50, "L"),
		(40, "XL"),
		(10, "X"),
		(9, "IX"),
		(5, "V"),
		(4, "IV"),
		(1, "I"),
	)

	romano = ""
	for valor, simbolo in valores:
		cantidad, numero = divmod(numero, valor)
		romano += simbolo * cantidad
	return romano


n = 2943
print(decimal_a_romano(n))

