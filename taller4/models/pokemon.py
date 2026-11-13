import random
from typing import List, Optional
from data.matriz_efectividad import calcular_efectividad
from models.movimiento import Movimiento


def calcular_daño(atacante: "Pokemon", defensor: "Pokemon", movimiento: Movimiento) -> int:
    if random.randint(1, 100) > movimiento.precision:
        print(f"¡El ataque {movimiento.nombre} de {atacante.nombre} ha fallado!")
        return 0

    if movimiento.categoria == "Físico":
        ataque = atacante.ataque
        defensa = defensor.defensa
    else:
        ataque = atacante.at_especial
        defensa = defensor.def_especial

    stab = 1.5 if movimiento.tipo in (atacante.tipo_1, atacante.tipo_2) else 1.0
    efectividad = calcular_efectividad(
        movimiento.tipo,
        defensor.tipo_1,
        defensor.tipo_2,
    )
    if efectividad == 0.0:
        print(f"No afecta a {defensor.nombre}...")
        return 0

    critico = random.random() <= 0.0625
    if critico:
        print("¡Un golpe crítico!")

    aleatorio = random.uniform(0.85, 1.00)
    nivel = 50
    # Los casos numéricos del PDF truncan el daño base antes de aplicar modificadores.
    daño_base = int(
        (((2 * nivel / 5) + 2) * movimiento.potencia * (ataque / defensa) / 50) + 2
    )
    modificador = stab * efectividad * (1.5 if critico else 1.0) * aleatorio
    return int(daño_base * modificador)


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
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")
        self.hp_actual = max(0, self.hp_actual - cantidad)

    def atacar(self, movimiento: Movimiento, objetivo: "Pokemon") -> int:
        """Consume PP, calcula el daño del movimiento y lo aplica al objetivo."""
        if not movimiento.es_valido():
            raise ValueError(f"{movimiento.nombre} no tiene PP.")
        movimiento.consumir_pp()
        daño = calcular_daño(self, objetivo, movimiento)
        if daño > 0:
            objetivo.recibir_daño(daño)
        return daño

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