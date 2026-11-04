from models.pokemon import Pokemon
from data.movimiento import CATALOGO_MOVIMIENTOS

POOL_POKEMON = {
    # 1. Caso de prueba: Jolteon (Eléctrico)
    "Jolteon": Pokemon(
        id_pokemon=135, nombre="Jolteon", tipo_1="Eléctrico",
        hp_max=270, ataque=120, defensa=110, at_especial=110, def_especial=100, velocidad=130,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Rayo"].copiar(),
            CATALOGO_MOVIMIENTOS["Bomba Lodo"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar(),
            CATALOGO_MOVIMIENTOS["Tijera X"].copiar()
        ]
    ),

    # 2. Caso de prueba: Gyarados (Agua / Volador)
    "Gyarados": Pokemon(
        id_pokemon=130, nombre="Gyarados", tipo_1="Agua", tipo_2="Volador",
        hp_max=330, ataque=155, defensa=109, at_especial=80, def_especial=100, velocidad=81,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Hidrobomba"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Pájaro Osado"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar()
        ]
    ),

    # 3. Caso de prueba: Snorlax (Normal)
    "Snorlax": Pokemon(
        id_pokemon=143, nombre="Snorlax", tipo_1="Normal",
        hp_max=430, ataque=110, defensa=115, at_especial=85, def_especial=130, velocidad=30,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar(),
            CATALOGO_MOVIMIENTOS["Puño Dinámico"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar()
        ]
    ),

    # 4. Caso de prueba: Charizard (Fuego / Volador)
    "Charizard": Pokemon(
        id_pokemon=6, nombre="Charizard", tipo_1="Fuego", tipo_2="Volador",
        hp_max=297, ataque=104, defensa=78, at_especial=129, def_especial=105, velocidad=100,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Lanzallamas"].copiar(),
            CATALOGO_MOVIMIENTOS["Pájaro Osado"].copiar(),
            CATALOGO_MOVIMIENTOS["Garra Dragón"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar()
        ]
    ),

    # 5. Caso de prueba: Blastoise (Agua)
    "Blastoise": Pokemon(
        id_pokemon=9, nombre="Blastoise", tipo_1="Agua",
        hp_max=299, ataque=103, defensa=120, at_especial=105, def_especial=105, velocidad=78,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Hidrobomba"].copiar(),
            CATALOGO_MOVIMIENTOS["Rayo de Hielo"].copiar(),
            CATALOGO_MOVIMIENTOS["Foco Resplandor"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar()
        ]
    ),

    # 6. Caso de prueba: Machamp (Lucha)
    "Machamp": Pokemon(
        id_pokemon=68, nombre="Machamp", tipo_1="Lucha",
        hp_max=321, ataque=150, defensa=100, at_especial=85, def_especial=105, velocidad=55,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Puño Dinámico"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar()
        ]
    ),

    # 7. Caso de prueba: Gengar (Fantasma / Veneno)
    "Gengar": Pokemon(
        id_pokemon=94, nombre="Gengar", tipo_1="Fantasma", tipo_2="Veneno",
        hp_max=261, ataque=85, defensa=80, at_especial=150, def_especial=95, velocidad=110,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Bola Sombra"].copiar(),
            CATALOGO_MOVIMIENTOS["Bomba Lodo"].copiar(),
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar(),
            CATALOGO_MOVIMIENTOS["Pulso Umbrío"].copiar()
        ]
    ),

    # 8. Venusaur (Planta / Veneno)
    "Venusaur": Pokemon(
        id_pokemon=3, nombre="Venusaur", tipo_1="Planta", tipo_2="Veneno",
        hp_max=301, ataque=100, defensa=103, at_especial=120, def_especial=120, velocidad=80,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Hoja Aguda"].copiar(),
            CATALOGO_MOVIMIENTOS["Bomba Lodo"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar()
        ]
    ),

    # 9. Dragonite (Dragón / Volador)
    "Dragonite": Pokemon(
        id_pokemon=149, nombre="Dragonite", tipo_1="Dragón", tipo_2="Volador",
        hp_max=323, ataque=154, defensa=115, at_especial=120, def_especial=120, velocidad=80,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Garra Dragón"].copiar(),
            CATALOGO_MOVIMIENTOS["Pájaro Osado"].copiar(),
            CATALOGO_MOVIMIENTOS["Lanzallamas"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar()
        ]
    ),

    # 10. Tyranitar (Roca / Siniestro)
    "Tyranitar": Pokemon(
        id_pokemon=248, nombre="Tyranitar", tipo_1="Roca", tipo_2="Siniestro",
        hp_max=341, ataque=154, defensa=130, at_especial=115, def_especial=120, velocidad=61,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar(),
            CATALOGO_MOVIMIENTOS["Pulso Umbrío"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Puño Dinámico"].copiar()
        ]
    ),

    # 11. Lucario (Lucha / Acero)
    "Lucario": Pokemon(
        id_pokemon=448, nombre="Lucario", tipo_1="Lucha", tipo_2="Acero",
        hp_max=281, ataque=130, defensa=90, at_especial=135, def_especial=90, velocidad=90,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Puño Dinámico"].copiar(),
            CATALOGO_MOVIMIENTOS["Foco Resplandor"].copiar(),
            CATALOGO_MOVIMIENTOS["Bola Sombra"].copiar(),
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar()
        ]
    ),

    # 12. Gardevoir (Psíquico / Hada)
    "Gardevoir": Pokemon(
        id_pokemon=282, nombre="Gardevoir", tipo_1="Psíquico", tipo_2="Hada",
        hp_max=277, ataque=85, defensa=85, at_especial=145, def_especial=135, velocidad=80,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar(),
            CATALOGO_MOVIMIENTOS["Fuerza Lunar"].copiar(),
            CATALOGO_MOVIMIENTOS["Bola Sombra"].copiar(),
            CATALOGO_MOVIMIENTOS["Rayo de Hielo"].copiar()
        ]
    ),

    # 13. Scizor (Bicho / Acero)
    "Scizor": Pokemon(
        id_pokemon=212, nombre="Scizor", tipo_1="Bicho", tipo_2="Acero",
        hp_max=281, ataque=150, defensa=120, at_especial=75, def_especial=100, velocidad=65,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Tijera X"].copiar(),
            CATALOGO_MOVIMIENTOS["Foco Resplandor"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar()
        ]
    ),

    # 14. Mamoswine (Hielo / Tierra)
    "Mamoswine": Pokemon(
        id_pokemon=473, nombre="Mamoswine", tipo_1="Hielo", tipo_2="Tierra",
        hp_max=361, ataque=150, defensa=100, at_especial=90, def_especial=80, velocidad=80,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Rayo de Hielo"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar()
        ]
    ),

    # 15. Garchomp (Dragón / Tierra)
    "Garchomp": Pokemon(
        id_pokemon=445, nombre="Garchomp", tipo_1="Dragón", tipo_2="Tierra",
        hp_max=357, ataque=150, defensa=115, at_especial=100, def_especial=105, velocidad=102,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Garra Dragón"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Lanzallamas"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar()
        ]
    ),

    # 16. Togekiss (Hada / Volador)
    "Togekiss": Pokemon(
        id_pokemon=468, nombre="Togekiss", tipo_1="Hada", tipo_2="Volador",
        hp_max=311, ataque=70, defensa=115, at_especial=140, def_especial=135, velocidad=80,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Fuerza Lunar"].copiar(),
            CATALOGO_MOVIMIENTOS["Pájaro Osado"].copiar(),
            CATALOGO_MOVIMIENTOS["Lanzallamas"].copiar(),
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar()
        ]
    ),

    # 17. Umbreon (Siniestro)
    "Umbreon": Pokemon(
        id_pokemon=197, nombre="Umbreon", tipo_1="Siniestro",
        hp_max=331, ataque=85, defensa=130, at_especial=80, def_especial=150, velocidad=65,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Pulso Umbrío"].copiar(),
            CATALOGO_MOVIMIENTOS["Bola Sombra"].copiar(),
            CATALOGO_MOVIMIENTOS["Golpe Cuerpo"].copiar(),
            CATALOGO_MOVIMIENTOS["Bomba Lodo"].copiar()
        ]
    ),

    # 18. Steelix (Acero / Tierra)
    "Steelix": Pokemon(
        id_pokemon=208, nombre="Steelix", tipo_1="Acero", tipo_2="Tierra",
        hp_max=291, ataque=105, defensa=200, at_especial=75, def_especial=85, velocidad=30,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Foco Resplandor"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar(),
            CATALOGO_MOVIMIENTOS["Puño Dinámico"].copiar()
        ]
    ),

    # 19. Aerodactyl (Roca / Volador)
    "Aerodactyl": Pokemon(
        id_pokemon=142, nombre="Aerodactyl", tipo_1="Roca", tipo_2="Volador",
        hp_max=301, ataque=125, defensa=85, at_especial=80, def_especial=95, velocidad=130,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Roca Afilada"].copiar(),
            CATALOGO_MOVIMIENTOS["Pájaro Osado"].copiar(),
            CATALOGO_MOVIMIENTOS["Terremoto"].copiar(),
            CATALOGO_MOVIMIENTOS["Lanzallamas"].copiar()
        ]
    ),

    # 20. Alakazam (Psíquico)
    "Alakazam": Pokemon(
        id_pokemon=65, nombre="Alakazam", tipo_1="Psíquico",
        hp_max=251, ataque=70, defensa=65, at_especial=155, def_especial=115, velocidad=120,
        movimientos=[
            CATALOGO_MOVIMIENTOS["Psíquico"].copiar(),
            CATALOGO_MOVIMIENTOS["Bola Sombra"].copiar(),
            CATALOGO_MOVIMIENTOS["Foco Resplandor"].copiar(),
            CATALOGO_MOVIMIENTOS["Rayo"].copiar()
        ]
    )
}

print(POOL_POKEMON["Gengar"])