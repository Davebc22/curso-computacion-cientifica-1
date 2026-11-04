# Matriz de efectividad de ataque según el tipo de Pokémon 
MATRIZ_EFECTIVIDAD = {
    "Normal": {"Roca": 0.5, "Fantasma": 0.0, "Acero": 0.5},
    "Fuego": {"Fuego": 0.5, "Agua": 0.5, "Planta": 2.0, "Hielo": 2.0, "Bicho": 2.0, "Roca": 0.5, "Dragón": 0.5, "Acero": 2.0},
    "Agua": {"Fuego": 2.0, "Agua": 0.5, "Planta": 0.5, "Tierra": 2.0, "Roca": 2.0, "Dragón": 0.5},
    "Planta": {"Fuego": 0.5, "Agua": 2.0, "Planta": 0.5, "Veneno": 0.5, "Tierra": 2.0, "Volador": 0.5, "Bicho": 0.5, "Roca": 2.0, "Dragón": 0.5, "Acero": 0.5},
    "Eléctrico": {"Agua": 2.0, "Planta": 0.5, "Eléctrico": 0.5, "Tierra": 0.0, "Volador": 2.0, "Dragón": 0.5},
    "Hielo": {"Fuego": 0.5, "Agua": 0.5, "Planta": 2.0, "Hielo": 0.5, "Tierra": 2.0, "Volador": 2.0, "Dragón": 2.0, "Acero": 0.5},
    "Lucha": {"Normal": 2.0, "Hielo": 2.0, "Veneno": 0.5, "Volador": 0.5, "Psíquico": 0.5, "Bicho": 0.5, "Roca": 2.0, "Fantasma": 0.0, "Siniestro": 2.0, "Acero": 2.0, "Hada": 0.5},
    "Veneno": {"Planta": 2.0, "Veneno": 0.5, "Tierra": 0.5, "Roca": 0.5, "Fantasma": 0.5, "Acero": 0.0, "Hada": 2.0},
    "Tierra": {"Fuego": 2.0, "Planta": 0.5, "Eléctrico": 2.0, "Veneno": 2.0, "Volador": 0.0, "Bicho": 0.5, "Roca": 2.0, "Acero": 2.0},
    "Volador": {"Planta": 2.0, "Eléctrico": 0.5, "Lucha": 2.0, "Bicho": 2.0, "Roca": 0.5, "Acero": 0.5},
    "Psíquico": {"Lucha": 2.0, "Veneno": 2.0, "Psíquico": 0.5, "Siniestro": 0.0, "Acero": 0.5},
    "Bicho": {"Fuego": 0.5, "Planta": 2.0, "Lucha": 0.5, "Veneno": 0.5, "Volador": 0.5, "Psíquico": 2.0, "Fantasma": 0.5, "Siniestro": 2.0, "Acero": 0.5, "Hada": 0.5},
    "Roca": {"Fuego": 2.0, "Hielo": 2.0, "Lucha": 0.5, "Tierra": 0.5, "Volador": 2.0, "Bicho": 2.0, "Acero": 0.5},
    "Fantasma": {"Normal": 0.0, "Psíquico": 2.0, "Fantasma": 2.0, "Siniestro": 0.5},
    "Dragón": {"Dragón": 2.0, "Acero": 0.5, "Hada": 0.0},
    "Siniestro": {"Lucha": 0.5, "Psíquico": 2.0, "Fantasma": 2.0, "Siniestro": 0.5, "Hada": 0.5},
    "Acero": {"Fuego": 0.5, "Agua": 0.5, "Eléctrico": 0.5, "Hielo": 2.0, "Roca": 2.0, "Acero": 0.5, "Hada": 2.0},
    "Hada": {"Fuego": 0.5, "Lucha": 2.0, "Veneno": 0.5, "Dragón": 2.0, "Siniestro": 2.0, "Acero": 0.5}
}


def calcular_efectividad(tipo_ataque: str, tipo_defensor_1: str, tipo_defensor_2: str = None) -> float:
    """
    Calcula el multiplicador de efectividad considerando defensores de uno o dos tipos.
    Retorna 1.0 como valor por defecto para interacciones neutras.
    """
    efectividad_1 = MATRIZ_EFECTIVIDAD.get(tipo_ataque, {}).get(tipo_defensor_1, 1.0)
    
    if tipo_defensor_2:
        efectividad_2 = MATRIZ_EFECTIVIDAD.get(tipo_ataque, {}).get(tipo_defensor_2, 1.0)
        return efectividad_1 * efectividad_2
        
    return efectividad_1

"""
Prueba:
pokemon = calcular_efectividad("Tierra", 'Fuego', "Volador")

print(pokemon)

"""
