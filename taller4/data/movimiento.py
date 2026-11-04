from models.movimiento import Movimiento

CATALOGO_MOVIMIENTOS = {
    # Movimientos obligatorios para los casos de prueba
    "Terremoto": Movimiento("Terremoto", "Tierra", "Físico", 100, 100, 10),
    "Rayo": Movimiento("Rayo", "Eléctrico", "Especial", 90, 100, 15),
    "Lanzallamas": Movimiento("Lanzallamas", "Fuego", "Especial", 90, 100, 15),
    "Puño Dinámico": Movimiento("Puño Dinámico", "Lucha", "Físico", 100, 50, 5),
    
    # Movimientos adicionales variados
    "Rayo de Hielo": Movimiento("Rayo de Hielo", "Hielo", "Especial", 90, 100, 10),
    "Garra Dragón": Movimiento("Garra Dragón", "Dragón", "Físico", 80, 100, 15),
    "Hidrobomba": Movimiento("Hidrobomba", "Agua", "Especial", 110, 80, 5),
    "Golpe Cuerpo": Movimiento("Golpe Cuerpo", "Normal", "Físico", 85, 100, 15),
    "Psíquico": Movimiento("Psíquico", "Psíquico", "Especial", 90, 100, 10),
    "Bola Sombra": Movimiento("Bola Sombra", "Fantasma", "Especial", 80, 100, 15),
    "Bomba Lodo": Movimiento("Bomba Lodo", "Veneno", "Especial", 90, 100, 10),
    "Tijera X": Movimiento("Tijera X", "Bicho", "Físico", 80, 100, 15),
    "Roca Afilada": Movimiento("Roca Afilada", "Roca", "Físico", 100, 80, 5),
    "Fuerza Lunar": Movimiento("Fuerza Lunar", "Hada", "Especial", 95, 100, 15),
    "Foco Resplandor": Movimiento("Foco Resplandor", "Acero", "Especial", 80, 100, 10),
    "Pulso Umbrío": Movimiento("Pulso Umbrío", "Siniestro", "Especial", 80, 100, 15),
    "Hoja Aguda": Movimiento("Hoja Aguda", "Planta", "Físico", 90, 100, 15),
    "Pájaro Osado": Movimiento("Pájaro Osado", "Volador", "Físico", 120, 100, 15)
}

"""
whatever = CATALOGO_MOVIMIENTOS.get("Rayo de Hielo")
print(whatever)
"""