"""
### Implementar la codificación Run-Length Encoding (RLE) expandida
Convierte la cadena "AAABBCDDDD" en "A3B2C1D4"

"""

cadena = 'AAABBCDDDD'
contador = 1
acumulador = []

for i in range(len(cadena)):
    if i+1 < len(cadena) and cadena[i] == cadena[i+1]:
        contador+=1
    else:
        acumulador.append(f'{cadena[i]}{contador}')
        contador = 1

print("".join(acumulador))
