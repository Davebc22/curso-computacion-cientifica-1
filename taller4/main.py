from cli.interfaz import jugar_batalla, seleccionar_pokemon, solicitar_nombre
from engine.batalla import Batalla
from models.entrenador import Entrenador


def main() -> None:
    print("=== Simulador de Batallas Pokémon ===")
    nombre1 = solicitar_nombre("Nombre del Jugador 1: ")
    pokemon1 = seleccionar_pokemon()
    nombre2 = solicitar_nombre("Nombre del Jugador 2: ")
    pokemon2 = seleccionar_pokemon()

    jugador1 = Entrenador(nombre1, pokemon1)
    jugador2 = Entrenador(nombre2, pokemon2)
    jugar_batalla(Batalla(jugador1, jugador2))


if __name__ == "__main__":
    main()
