"""
# 12. Implemente un algoritmo que como entrada reciba una lista de numeros, y un numero T objetivo. Como salida el algoritmo debe encontrar grupos de 3 numeros que sumen el numero T objetivo

"""
lista_entrada = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
t = 20

print(f'Elementos de la lista que al formarse en grupos de 3 y al sumarlos dan {t}: ')
for i in range(len(lista_entrada)):
    for j in range(i+1, len(lista_entrada)):
        for k in range(j+1, len(lista_entrada)):
            if lista_entrada[i]+lista_entrada[j]+lista_entrada[k] == t:
                print(f'({lista_entrada[i]} + {lista_entrada[j]} + {lista_entrada[k]}) = {t}')


