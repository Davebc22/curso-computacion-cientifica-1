import random

class Carta:

    palo = {
        "Treboles" : 1,
        "Diamantes" : 2,
        "Picas" : 3, 
        "Corazones" : 4    
    }

    identificador ={ 
        "A": 1, 
        "2": 2,
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "J": 11, 
        "Q": 12, 
        "K": 13
    }

    def __init__(self, palo, identificador):
        self.palo = palo
        self.identificador = identificador

    def __str__(self):
        return f'{self.identificador} de {self.palo}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, otra):
        return self.palo == otra.palo and self.identificador == otra.identificador

    def __lt__(self, otra):
        #C1
        palo_self = Carta.palo[self.palo]
        id_self = Carta.identificador[str(self.identificador)]
        #C2
        palo_otra = Carta.palo[otra.palo]
        id_otra = Carta.identificador[str(otra.identificador)]
        
        if palo_self < palo_otra:
            return True
        elif palo_self > palo_otra:
            return False
        else: 
            return id_self < id_otra

        def __gt__(self, otra):
            return otra < self

class Baraja:
    def __init__(self):
        self.baraja = []
        for palo in Carta.palo:
            for identificador in Carta.identificador:
                carta = Carta(palo,identificador)
                self.baraja.append(carta)

    def __str__(self):
        return f'Baraja con {len(self.baraja)} cartas: \n\n{self.baraja}'

    def barajar(self):
        random.shuffle(self.baraja)

    def ordenar(self):
        self.baraja.sort()


# Pruebas 


baraja = Baraja()
print("### NUEVA BARAJA ###")
print(f'{baraja}\n')

baraja.barajar()
print("### BARAJANDO ###")
print(f'\n{baraja}\n')

baraja.ordenar()
print("### ORGANIZANDO ###")
print(f'\n{baraja}\n')


print("\n### PRUEBAS DE COMPARACIÓN DE CARTAS ###")
c1 = Carta("Treboles", "A")
c2 = Carta("Corazones", "K")
c3 = Carta("Treboles", "8")
c4 = Carta("Treboles", "A")
print(f"{c1} == {c4} :", c1 == c4)  
print(f"{c1} < {c2}  :", c1 < c2)   
print(f"{c1} > {c2}  :", c1 > c2)   