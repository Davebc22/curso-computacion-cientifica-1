import copy
from collections.abc import Callable, Mapping

from data.pokemon_pool import POOL_POKEMON
from engine.batalla import Batalla
from models.entrenador import Entrenador
from models.movimiento import Movimiento
from models.pokemon import Pokemon


InputFn = Callable[[str], str]
OutputFn = Callable[[str], None]


def solicitar_nombre(
    prompt: str,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
) -> str:
    while True:
        nombre = input_fn(prompt).strip()
        if nombre:
            return nombre
        output_fn("El nombre no puede estar vacío.")


def seleccionar_pokemon(
    pool: Mapping[str, Pokemon] = POOL_POKEMON,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
) -> Pokemon:
    pokemones = list(pool.values())
    if not pokemones:
        raise ValueError("No hay Pokémon disponibles en el pool.")

    while True:
        output_fn("Selecciona tu Pokémon:")
        for indice, pokemon in enumerate(pokemones, start=1):
            output_fn(f"{indice}. {pokemon}")

        respuesta = input_fn(f"Opción (1-{len(pokemones)}): ").strip()
        try:
            indice = int(respuesta)
        except ValueError:
            output_fn("Ingresa un número válido.")
            continue

        if 1 <= indice <= len(pokemones):
            return copy.deepcopy(pokemones[indice - 1])

        output_fn(f"Elige un número entre 1 y {len(pokemones)}.")


def mostrar_hud(batalla: Batalla, output_fn: OutputFn = print) -> None:
    output_fn(f"\n--- Turno {batalla.turno_actual} ---")
    for entrenador in (batalla.jugador1, batalla.jugador2):
        pokemon = entrenador.pokemon_activo
        output_fn(
            f"{entrenador.nombre} - {pokemon.nombre}: "
            f"HP {pokemon.hp_actual}/{pokemon.hp_max}"
        )
        for indice, movimiento in enumerate(pokemon.movimientos, start=1):
            output_fn(
                f"  {indice}. {movimiento.nombre} "
                f"({movimiento.tipo}, PP {movimiento.pp_actual}/{movimiento.pp_max})"
            )


def solicitar_movimiento(
    entrenador: Entrenador,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
) -> Movimiento:
    movimientos = entrenador.pokemon_activo.movimientos
    while True:
        respuesta = input_fn(
            f"{entrenador.nombre}, elige un movimiento (1-{len(movimientos)}): "
        ).strip()
        try:
            indice = int(respuesta)
        except ValueError:
            output_fn("Ingresa un número válido.")
            continue

        if not 1 <= indice <= len(movimientos):
            output_fn(f"Elige un número entre 1 y {len(movimientos)}.")
            continue

        movimiento = movimientos[indice - 1]
        if not movimiento.es_valido():
            output_fn(f"{movimiento.nombre} no tiene PP. Elige otro movimiento.")
            continue
        return movimiento


def jugar_batalla(
    batalla: Batalla,
    input_fn: InputFn = input,
    output_fn: OutputFn = print,
) -> str | None:
    batalla.iniciar_combate()

    while True:
        ganador = batalla.verificar_ganador()
        if ganador is not None:
            output_fn(f"¡{ganador} gana la batalla!")
            return ganador

        sin_movimientos = [
            entrenador
            for entrenador in (batalla.jugador1, batalla.jugador2)
            if not any(
                movimiento.es_valido()
                for movimiento in entrenador.pokemon_activo.movimientos
            )
        ]
        if sin_movimientos:
            nombres = ", ".join(entrenador.nombre for entrenador in sin_movimientos)
            output_fn(
                f"La batalla termina sin ganador: {nombres} "
                "no tiene movimientos con PP."
            )
            return None

        mostrar_hud(batalla, output_fn)
        movimiento1 = solicitar_movimiento(batalla.jugador1, input_fn, output_fn)
        movimiento2 = solicitar_movimiento(batalla.jugador2, input_fn, output_fn)
        batalla.procesar_turno(movimiento1, movimiento2)
