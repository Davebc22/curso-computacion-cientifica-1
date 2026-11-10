# models/entrenador.py
from models.pokemon import Pokemon
from data.pokemon_pool import POOL_POKEMON



class Entrenador:
    def __init__(self, nombre: str, pokemon_activo: Pokemon):
        self.nombre = nombre
        self.pokemon_activo = pokemon_activo

    def tiene_pokemon_disponible(self) -> bool:
        """Evalúa si el Pokémon activo del entrenador no está debilitado."""
        return not self.pokemon_activo.esta_debilitado()

    def __str__(self) -> str:
        return f"Entrenador: {self.nombre} | Pokémon Activo: {self.pokemon_activo.nombre}"

"""
entrenador1 = Entrenador("Cabezón", POOL_POKEMON["Gengar"])
print(entrenador1)
"""