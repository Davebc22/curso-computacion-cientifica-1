"""
# 10. Conjetura de Collatz

### Implementa un algoritmo que genere y grafique la siguiente secuencia, iniciando desde un numero entero positivo cualquiera

- Si el ultimo numero n es par, el siguiente es: n/2
- Si el ultimo numero n es impar, el siguiente es: 3*n+1


"""
import matplotlib.pyplot as plt
# Función de Collatz
def collatz(n):
    if n<=0:
        return []
        
    contenedor = [n]
    while n !=1:
        if n % 2 == 0:
            n = n//2
            contenedor.append(n)
        else:
            n = 3*n+1
            contenedor.append(n)
    return contenedor

#Pedir Datos 
numero = int(input('Inserte un entero positivo: '))
print(collatz(numero))


# Graficar Función 
datos = collatz(numero)
plt.figure(figsize=(8,4))
plt.plot(datos, color="#602b8f", linewidth=2, marker='o', markersize=4)
plt.title('Conjetura de Collatz', fontsize=12, fontweight='semibold')
plt.xlabel('Iteraciones')
plt.ylabel('Valor ($n$)')
plt.show()