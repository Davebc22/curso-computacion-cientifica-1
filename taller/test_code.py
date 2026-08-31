"""
# 7. Realiza un algoritmo que tome como entrada 3 puntos x,y del plano cartesiano, formando un triangulo, como salida el programa calcule al area y perimetro

Algoritmo
Tomar 3 coordenadas
Calcular pitágoras
Usar forma vectorial del área
"""
import numpy as np

x1 = np.array((2,0))
x2 = np.array((1,5))
x3 = np.array((2,1))

perimetro = np.linalg.norm(x2-x1) + np.linalg.norm(x3-x2) + np.linalg.norm(x3-x1)

v1 = x2 - x1 
v2 = x3 - x1 

#Multiplicación cruzada
area = 0.5 * np.abs(v1[0]*v2[1] - v1[1] * v2[0])

print(f'El perímetro es {perimetro} y el área es: {area}')
