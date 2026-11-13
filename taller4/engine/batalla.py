# engine/batalla.py

import random
from models.entrenador import Entrenador
from models.movimiento import Movimiento
from models.pokemon import Pokemon, calcular_daño as calcular_daño_pokemon


class Batalla:
    def __init__(self, jugador1: Entrenador, jugador2: Entrenador):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = 1

    def iniciar_combate(self) -> None:
        """Anuncia el inicio de la batalla 1 vs 1."""
        print(f"¡Comienza la batalla entre {self.jugador1.nombre} y {self.jugador2.nombre}!")
        print(f"({self.jugador1.pokemon_activo} VS {self.jugador2.pokemon_activo})\n")

    def resolver_prioridad(self) -> tuple[Entrenador, Entrenador]:
        """Retorna los entrenadores en el orden en que deben actuar según la velocidad de su Pokémon activo."""
        vel1 = self.jugador1.pokemon_activo.velocidad
        vel2 = self.jugador2.pokemon_activo.velocidad

        if vel1 > vel2:
            return self.jugador1, self.jugador2
        elif vel2 > vel1:
            return self.jugador2, self.jugador1
        else:
            # Desempate estocástico p = 0.5 en caso de empate de velocidad
            if random.random() < 0.5:
                return self.jugador1, self.jugador2
            else:
                return self.jugador2, self.jugador1

    def calcular_daño(
        self,
        atacante: Pokemon,
        defensor: Pokemon,
        movimiento: Movimiento
    ) -> int:
        """Calcula el daño aplicando las reglas estocásticas, de tipo y estadísticas."""
        return calcular_daño_pokemon(atacante, defensor, movimiento)

    def procesar_turno(
        self,
        movimiento_jugador1: Movimiento,
        movimiento_jugador2: Movimiento
    ) -> None:
        """Ejecuta el flujo completo de un turno resolviendo prioridades, consumiendo PP y aplicando el daño."""
        movimientos = {
            self.jugador1: movimiento_jugador1,
            self.jugador2: movimiento_jugador2
        }

        for entrenador, movimiento in movimientos.items():
            if not movimiento.es_valido():
                raise ValueError(
                    f"{entrenador.nombre} no puede usar {movimiento.nombre}: no tiene PP."
                )

        print(f"--- Turno {self.turno_actual} ---")

        # 1. Determinar quién ataca primero
        primero, segundo = self.resolver_prioridad()

        # 2. Acción del primer atacante
        atk1 = primero.pokemon_activo
        def1 = segundo.pokemon_activo
        mov1 = movimientos[primero]

        print(f"¡{atk1.nombre} usa {mov1.nombre}!")
        dano1 = atk1.atacar(mov1, def1)
        if dano1 > 0:
            print(f"{def1.nombre} recibe {dano1} de daño. (HP: {def1.hp_actual}/{def1.hp_max})")

        # 3. Acción del segundo atacante (solo si no se ha debilitado)
        if not def1.esta_debilitado():
            atk2 = segundo.pokemon_activo
            def2 = primero.pokemon_activo
            mov2 = movimientos[segundo]

            print(f"¡{atk2.nombre} usa {mov2.nombre}!")
            dano2 = atk2.atacar(mov2, def2)
            if dano2 > 0:
                print(f"{def2.nombre} recibe {dano2} de daño. (HP: {def2.hp_actual}/{def2.hp_max})")
        else:
            print(f"¡{def1.nombre} ha sido debilitado!")

        self.turno_actual += 1

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
        
        return None   # Continúa el combate

    def __str__(self) -> str:
        return f"Turno: {self.turno_actual} | {self.jugador1} vs {self.jugador2}"