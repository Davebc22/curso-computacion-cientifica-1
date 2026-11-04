from typing import List, Optional
from models.movimiento import Movimiento

class Pokemon:
    def __init__(
        self,
        id_pokemon: int,
        nombre: str,
        tipo_1: str,
        hp_max: int,
        ataque: int,
        defensa: int,
        at_especial: int,
        def_especial: int,
        velocidad: int,
        movimientos: List[Movimiento],
        tipo_2: Optional[str] = None
    ):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.hp_max = hp_max
        self.hp_actual = hp_max
        self.ataque = ataque
        self.defensa = defensa
        self.at_especial = at_especial
        self.def_especial = def_especial
        self.velocidad = velocidad
        self.movimientos = movimientos

    def recibir_daño(self, cantidad: int) -> None:
        """Reduce los Puntos de Salud actuales del Pokémon sin bajar de 0."""
        self.hp_actual = max(0, self.hp_actual - cantidad)

    def esta_debilitado(self) -> bool:
        """Evalúa si el Pokémon se ha quedado sin Puntos de Salud."""
        return self.hp_actual <= 0

    def obtener_estadistica(self, nombre_stat: str) -> int:
        """Retorna el valor numérico de la estadística solicitada."""
        stats = {
            "hp_max": self.hp_max,
            "hp_actual": self.hp_actual,
            "ataque": self.ataque,
            "defensa": self.defensa,
            "at_especial": self.at_especial,
            "def_especial": self.def_especial,
            "velocidad": self.velocidad
        }
        return stats.get(nombre_stat.lower(), 0)

    def __str__(self) -> str:
        tipos = f"{self.tipo_1}/{self.tipo_2}" if self.tipo_2 else self.tipo_1
        return f"{self.nombre} ({tipos}) - HP: {self.hp_actual}/{self.hp_max}"