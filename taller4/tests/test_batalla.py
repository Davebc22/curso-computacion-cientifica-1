import copy
import unittest
from unittest.mock import patch

from data.pokemon_pool import POOL_POKEMON
from engine.batalla import Batalla
from models.entrenador import Entrenador


TIPOS_OFICIALES = {
    "Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psíquico", "Bicho",
    "Roca", "Fantasma", "Dragón", "Siniestro", "Acero", "Hada",
}


class TestDatosIniciales(unittest.TestCase):
    def test_pool_cubre_los_18_tipos_y_tiene_cuatro_movimientos(self):
        self.assertEqual(len(POOL_POKEMON), 20)
        tipos = {
            tipo
            for pokemon in POOL_POKEMON.values()
            for tipo in (pokemon.tipo_1, pokemon.tipo_2)
            if tipo
        }
        self.assertSetEqual(tipos, TIPOS_OFICIALES)
        self.assertEqual(
            len({pokemon.id for pokemon in POOL_POKEMON.values()}),
            len(POOL_POKEMON),
        )
        for nombre, pokemon in POOL_POKEMON.items():
            self.assertEqual(pokemon.nombre, nombre)
            self.assertIn(pokemon.tipo_1, TIPOS_OFICIALES)
            self.assertTrue(
                pokemon.tipo_2 is None or pokemon.tipo_2 in TIPOS_OFICIALES
            )
            self.assertEqual(len(pokemon.movimientos), 4, pokemon.nombre)
            self.assertGreater(pokemon.hp_max, 0, pokemon.nombre)
            self.assertEqual(pokemon.hp_actual, pokemon.hp_max, pokemon.nombre)
            for estadistica in (
                "ataque", "defensa", "at_especial", "def_especial", "velocidad"
            ):
                self.assertGreater(getattr(pokemon, estadistica), 0, pokemon.nombre)
            for movimiento in pokemon.movimientos:
                self.assertIn(movimiento.tipo, TIPOS_OFICIALES)
                self.assertIn(movimiento.categoria, {"Físico", "Especial"})
                self.assertGreater(movimiento.potencia, 0)
                self.assertGreaterEqual(movimiento.precision, 0)
                self.assertLessEqual(movimiento.precision, 100)
                self.assertGreater(movimiento.pp_max, 0)
                self.assertEqual(movimiento.pp_actual, movimiento.pp_max)


class TestModelos(unittest.TestCase):
    def test_pokemon_no_puede_recibir_daño_negativo_y_se_debilita_en_cero(self):
        pokemon = copy.deepcopy(POOL_POKEMON["Jolteon"])

        with self.assertRaisesRegex(ValueError, "no puede ser negativo"):
            pokemon.recibir_daño(-1)
        self.assertEqual(pokemon.hp_actual, pokemon.hp_max)

        pokemon.recibir_daño(pokemon.hp_max + 1)
        self.assertEqual(pokemon.hp_actual, 0)
        self.assertTrue(pokemon.esta_debilitado())

    def test_pokemon_ataca_consumiendo_pp_y_aplicando_el_daño(self):
        atacante = copy.deepcopy(POOL_POKEMON["Jolteon"])
        defensor = copy.deepcopy(POOL_POKEMON["Gyarados"])
        movimiento = atacante.movimientos[0]

        with (
            patch("engine.batalla.random.randint", return_value=100),
            patch("engine.batalla.random.random", return_value=0.5),
            patch("engine.batalla.random.uniform", return_value=1.0),
        ):
            daño = atacante.atacar(movimiento, defensor)

        self.assertEqual(daño, 270)
        self.assertEqual(movimiento.pp_actual, movimiento.pp_max - 1)
        self.assertEqual(defensor.hp_actual, defensor.hp_max - daño)


class TestBatalla(unittest.TestCase):
    def setUp(self):
        jolteon = copy.deepcopy(POOL_POKEMON["Jolteon"])
        gyarados = copy.deepcopy(POOL_POKEMON["Gyarados"])
        self.jugador1 = Entrenador("Jugador 1", jolteon)
        self.jugador2 = Entrenador("Jugador 2", gyarados)
        self.batalla = Batalla(self.jugador1, self.jugador2)

    def test_prioridad_se_define_por_velocidad_y_resuelve_empates(self):
        self.assertEqual(
            self.batalla.resolver_prioridad(),
            (self.jugador1, self.jugador2),
        )

        self.jugador2.pokemon_activo.velocidad = self.jugador1.pokemon_activo.velocidad
        with patch("engine.batalla.random.random", return_value=0.49):
            self.assertEqual(
                self.batalla.resolver_prioridad(),
                (self.jugador1, self.jugador2),
            )
        with patch("engine.batalla.random.random", return_value=0.5):
            self.assertEqual(
                self.batalla.resolver_prioridad(),
                (self.jugador2, self.jugador1),
            )

    def test_calculo_de_daño_usa_precision_critico_stab_y_efectividad(self):
        movimiento = self.jugador1.pokemon_activo.movimientos[0]
        with (
            patch("engine.batalla.random.randint", return_value=90),
            patch("engine.batalla.random.random", return_value=0.5),
            patch("engine.batalla.random.uniform", return_value=0.85),
        ):
            daño = self.batalla.calcular_daño(
                self.jugador1.pokemon_activo,
                self.jugador2.pokemon_activo,
                movimiento,
            )

        self.assertEqual(daño, 229)

    def test_golpe_critico_usa_probabilidad_y_multiplicador_correctos(self):
        movimiento = self.jugador1.pokemon_activo.movimientos[0]
        daños = []
        for resultado_critico in (0.0625, 0.0625001):
            with (
                patch("engine.batalla.random.randint", return_value=100),
                patch("engine.batalla.random.random", return_value=resultado_critico),
                patch("engine.batalla.random.uniform", return_value=1.0),
            ):
                daños.append(
                    self.batalla.calcular_daño(
                        self.jugador1.pokemon_activo,
                        self.jugador2.pokemon_activo,
                        movimiento,
                    )
                )

        self.assertEqual(daños, [405, 270])

    def test_caso_pdf_critico_y_resistencia_de_tipos(self):
        charizard = copy.deepcopy(POOL_POKEMON["Charizard"])
        blastoise = copy.deepcopy(POOL_POKEMON["Blastoise"])
        batalla = Batalla(
            Entrenador("Jugador 1", charizard),
            Entrenador("Jugador 2", blastoise),
        )

        with (
            patch("engine.batalla.random.randint", return_value=100),
            patch("engine.batalla.random.random", return_value=0.0625),
            patch("engine.batalla.random.uniform", return_value=1.0),
        ):
            daño = batalla.calcular_daño(
                charizard,
                blastoise,
                charizard.movimientos[0],
            )

        self.assertEqual(daño, 56)

    def test_caso_pdf_terremoto_no_afecta_a_charizard(self):
        snorlax = copy.deepcopy(POOL_POKEMON["Snorlax"])
        charizard = copy.deepcopy(POOL_POKEMON["Charizard"])
        batalla = Batalla(
            Entrenador("Jugador 1", snorlax),
            Entrenador("Jugador 2", charizard),
        )

        with (
            patch("engine.batalla.random.randint", return_value=100),
            patch("engine.batalla.random.random") as probabilidad_critico,
            patch("engine.batalla.random.uniform") as variacion,
        ):
            daño = batalla.calcular_daño(
                snorlax,
                charizard,
                snorlax.movimientos[0],
            )

        self.assertEqual(daño, 0)
        probabilidad_critico.assert_not_called()
        variacion.assert_not_called()

    def test_movimiento_fallido_consume_pp_sin_causar_daño(self):
        movimiento1 = self.jugador1.pokemon_activo.movimientos[0]
        movimiento2 = self.jugador2.pokemon_activo.movimientos[0]
        movimiento1.precision = 90
        movimiento2.precision = 90
        hp_jolteon = self.jugador1.pokemon_activo.hp_actual
        hp_gyarados = self.jugador2.pokemon_activo.hp_actual

        with patch("engine.batalla.random.randint", return_value=91):
            self.batalla.procesar_turno(movimiento1, movimiento2)

        self.assertEqual(movimiento1.pp_actual, movimiento1.pp_max - 1)
        self.assertEqual(movimiento2.pp_actual, movimiento2.pp_max - 1)
        self.assertEqual(self.jugador1.pokemon_activo.hp_actual, hp_jolteon)
        self.assertEqual(self.jugador2.pokemon_activo.hp_actual, hp_gyarados)
        self.assertEqual(self.batalla.turno_actual, 2)

    def test_movimiento_sin_pp_no_inicia_el_turno(self):
        movimiento1 = self.jugador1.pokemon_activo.movimientos[0]
        movimiento2 = self.jugador2.pokemon_activo.movimientos[0]
        movimiento1.pp_actual = 0
        hp_jolteon = self.jugador1.pokemon_activo.hp_actual
        hp_gyarados = self.jugador2.pokemon_activo.hp_actual

        with self.assertRaisesRegex(ValueError, "no tiene PP"):
            self.batalla.procesar_turno(movimiento1, movimiento2)

        self.assertEqual(movimiento1.pp_actual, 0)
        self.assertEqual(movimiento2.pp_actual, movimiento2.pp_max)
        self.assertEqual(self.jugador1.pokemon_activo.hp_actual, hp_jolteon)
        self.assertEqual(self.jugador2.pokemon_activo.hp_actual, hp_gyarados)
        self.assertEqual(self.batalla.turno_actual, 1)

    def test_verificar_ganador_detecta_pokemon_debilitado(self):
        self.jugador1.pokemon_activo.recibir_daño(
            self.jugador1.pokemon_activo.hp_actual
        )

        self.assertEqual(self.batalla.verificar_ganador(), "Jugador 2")


if __name__ == "__main__":
    unittest.main()
