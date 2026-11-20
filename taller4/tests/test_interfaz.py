import copy
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from cli.interfaz import (
    jugar_batalla,
    mostrar_hud,
    seleccionar_pokemon,
    solicitar_movimiento,
)
from data.pokemon_pool import POOL_POKEMON
from engine.batalla import Batalla
from models.entrenador import Entrenador


class TestInterfaz(unittest.TestCase):
    def test_seleccion_de_pokemon_rechaza_entrada_no_numerica(self):
        entradas = iter(("abc", "0", "1"))
        mensajes = []
        pokemon = seleccionar_pokemon(
            {"Jolteon": POOL_POKEMON["Jolteon"]},
            input_fn=lambda _prompt: next(entradas),
            output_fn=mensajes.append,
        )

        self.assertEqual(pokemon.nombre, "Jolteon")
        self.assertEqual(mensajes.count("Ingresa un número válido."), 1)
        self.assertEqual(len(mensajes), 8)

    def test_seleccion_de_movimiento_reintenta_entradas_invalidas(self):
        pokemon = copy.deepcopy(POOL_POKEMON["Jolteon"])
        pokemon.movimientos[0].pp_actual = 0
        entrenador = Entrenador("Jugador", pokemon)
        entradas = iter(("texto", "0", "1", "2"))
        mensajes = []

        movimiento = solicitar_movimiento(
            entrenador,
            input_fn=lambda _prompt: next(entradas),
            output_fn=mensajes.append,
        )

        self.assertIs(movimiento, pokemon.movimientos[1])
        self.assertEqual(len(mensajes), 3)

    def test_seleccion_de_pokemon_devuelve_instancia_independiente(self):
        pool = {"Jolteon": POOL_POKEMON["Jolteon"]}
        pokemon = seleccionar_pokemon(
            pool,
            input_fn=lambda _prompt: "1",
            output_fn=lambda _mensaje: None,
        )

        self.assertIsNot(pokemon, pool["Jolteon"])
        self.assertIsNot(pokemon.movimientos[0], pool["Jolteon"].movimientos[0])

    def test_hud_muestra_hp_y_pp(self):
        entrenador1 = Entrenador(
            "Jugador 1", copy.deepcopy(POOL_POKEMON["Jolteon"])
        )
        entrenador2 = Entrenador(
            "Jugador 2", copy.deepcopy(POOL_POKEMON["Gyarados"])
        )
        mensajes = []
        mostrar_hud(
            Batalla(entrenador1, entrenador2),
            output_fn=mensajes.append,
        )

        texto_hud = "\n".join(mensajes)
        self.assertIn("HP 270/270", texto_hud)
        self.assertIn("PP 15/15", texto_hud)

    def test_juego_solicita_movimientos_en_orden_y_anuncia_ganador(self):
        entrenador1 = Entrenador(
            "Jugador 1", copy.deepcopy(POOL_POKEMON["Jolteon"])
        )
        entrenador2 = Entrenador(
            "Jugador 2", copy.deepcopy(POOL_POKEMON["Gyarados"])
        )
        batalla = Batalla(entrenador1, entrenador2)
        prompts = []
        mensajes = []

        def responder(prompt):
            prompts.append(prompt)
            return "1"

        def terminar_batalla(instancia, _movimiento1, _movimiento2):
            instancia.jugador2.pokemon_activo.recibir_daño(
                instancia.jugador2.pokemon_activo.hp_actual
            )

        with patch.object(Batalla, "procesar_turno", terminar_batalla):
            ganador = jugar_batalla(
                batalla,
                input_fn=responder,
                output_fn=mensajes.append,
            )

        self.assertEqual(ganador, "Jugador 1")
        self.assertIn("Jugador 1, elige", prompts[0])
        self.assertIn("Jugador 2, elige", prompts[1])
        self.assertIn("¡Jugador 1 gana la batalla!", mensajes[-1])

    def test_batalla_jolteon_contra_gyarados_hasta_ganador(self):
        jolteon = copy.deepcopy(POOL_POKEMON["Jolteon"])
        gyarados = copy.deepcopy(POOL_POKEMON["Gyarados"])
        batalla = Batalla(
            Entrenador("Jugador 1", jolteon),
            Entrenador("Jugador 2", gyarados),
        )
        mensajes = []
        consola = io.StringIO()

        with (
            patch("engine.batalla.random.randint", return_value=1),
            patch("engine.batalla.random.random", return_value=0.5),
            patch("engine.batalla.random.uniform", return_value=1.0),
            redirect_stdout(consola),
        ):
            ganador = jugar_batalla(
                batalla,
                input_fn=lambda _prompt: "1",
                output_fn=mensajes.append,
            )

        self.assertEqual(ganador, "Jugador 1")
        self.assertEqual(gyarados.hp_actual, 0)
        self.assertEqual(jolteon.movimientos[0].pp_actual, 13)
        self.assertEqual(gyarados.movimientos[0].pp_actual, 4)
        self.assertIn("Gyarados recibe 270 de daño", consola.getvalue())
        self.assertIn("Jolteon recibe 60 de daño", consola.getvalue())

    def test_batalla_snorlax_contra_charizard_hasta_ganador(self):
        snorlax = copy.deepcopy(POOL_POKEMON["Snorlax"])
        charizard = copy.deepcopy(POOL_POKEMON["Charizard"])
        batalla = Batalla(
            Entrenador("Jugador 1", snorlax),
            Entrenador("Jugador 2", charizard),
        )

        respuestas = iter(("4", "1", "4", "1"))
        consola = io.StringIO()
        with (
            patch("engine.batalla.random.randint", return_value=1),
            patch("engine.batalla.random.random", return_value=0.5),
            patch("engine.batalla.random.uniform", return_value=1.0),
            redirect_stdout(consola),
        ):
            ganador = jugar_batalla(
                batalla,
                input_fn=lambda _prompt: next(respuestas),
                output_fn=lambda _mensaje: None,
            )

        self.assertEqual(ganador, "Jugador 1")
        self.assertEqual(charizard.hp_actual, 0)
        self.assertGreater(snorlax.hp_actual, 0)
        self.assertEqual(snorlax.movimientos[3].pp_actual, 3)
        self.assertEqual(charizard.movimientos[0].pp_actual, 13)
        self.assertIn("Charizard recibe 256 de daño", consola.getvalue())
        self.assertIn("Snorlax recibe 61 de daño", consola.getvalue())


if __name__ == "__main__":
    unittest.main()
