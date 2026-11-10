from data.pokemon_pool import POOL_POKEMON
from models.entrenador import Entrenador
from engine.batalla import Batalla

jugador1 = Entrenador("Jugador 1", POOL_POKEMON["Jolteon"])
jugador2 = Entrenador("Jugador 2", POOL_POKEMON["Gyarados"])
batalla = Batalla(jugador1, jugador2)

assert batalla.jugador1 is jugador1
assert batalla.jugador2 is jugador2
assert batalla.turno_actual == 1
assert batalla.verificar_ganador() is None

batalla.iniciar_combate()
print(batalla)

# Comprueba también que detecta un ganador cuando un Pokémon cae debilitado.
pokemon1 = jugador1.pokemon_activo
pokemon1.recibir_daño(pokemon1.hp_actual)
assert batalla.verificar_ganador() == "Jugador 2"

print("Prueba básica superada.")