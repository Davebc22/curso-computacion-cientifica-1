# engine/batalla.py

from models.entrenador import Entrenador
from models.movimiento import Movimiento
from models.pokemon import Pokemon

class Batalla:
    def __init__(self, jugador1: Entrenador, jugador2: Entrenador):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = 1

    def iniciar_combate(self) -> None:
        """Anuncia el inicio de la batalla 1 vs 1."""
        print(f"¡Comienza la batalla entre {self.jugador1.nombre} y {self.jugador2.nombre}!")
        print(f"({self.jugador1.pokemon_activo} VS {self.jugador2.pokemon_activo})\n")

    def procesar_turno(
        self,
        movimiento_jugador1: Movimiento,
        movimiento_jugador2: Movimiento
    ) -> None:
        """Procesa las acciones elegidas por ambos jugadores durante un turno."""
        raise NotImplementedError("El procesamiento del turno se implementará en la fase 3.")

    def resolver_prioridad(self) -> tuple[Entrenador, Entrenador]:
        """Retorna los entrenadores en el orden en que deben actuar."""
        raise NotImplementedError("La prioridad de turno se implementará en la fase 3.")

    def calcular_daño(
        self,
        atacante: Pokemon,
        defensor: Pokemon,
        movimiento: Movimiento
    ) -> int:
        """Calcula el daño que un movimiento causa al Pokémon defensor."""
        raise NotImplementedError("El cálculo de daño se implementará en la fase 3.")

    def verificar_ganador(self) -> str | None:
        """Evalúa si alguno de los entrenadores se ha quedado sin Pokémon disponible."""
        p1_vivo = self.jugador1.tiene_pokemon_disponible()
        p2_vivo = self.jugador2.tiene_pokemon_disponible()

        if not p1_vivo and not p2_vivo:
            return "Empate"
        elif not p1_vivo:
            return self.jugador2.nombre
        elif not p2_vivo:
            return self.jugador1.nombre
        
        return None   # continúa el combate

    def __str__(self) -> str:
        return f"Turno: {self.turno_actual} | {self.jugador1} vs {self.jugador2}"