# 🗺️ Hoja de Ruta: Proyecto Final - Simulador de Batallas Pokémon (1 vs 1)
## Realizado con IA: Evaluación personalizada item a item - **No se da por marcada la sección si no se asegura comprensión** 


Esta hoja de ruta está diseñada para cumplir al 100% con los criterios de evaluación del proyecto, adaptando estrictamente la lógica para combates individuales (1 vs 1).

---

## Fase 1: Base de Datos y Sistema de Tipos (Mecánica y Pool)
**Objetivo:** Construir la base de conocimiento estática del juego.
*Correspondencia en PDF: Sección 2 (Mecánica de Tipos) y Sección 3 (Pool de Pokémon).*

- [ ] **1.1. Matriz de Efectividad:** Crear la estructura (diccionario o matriz) que calcule los multiplicadores (0.0, 0.5, 1.0, 2.0, 4.0) cruzando tipos de ataque vs. tipos del defensor.
- [ ] **1.2. Catálogo de Movimientos:** Definir un pool de movimientos con sus atributos (`nombre`, `tipo`, `categoria` [Físico/Especial], `potencia`, `precision`, `pp_max`).
- [ ] **1.3. Pool de 20 Pokémon:** Crear un archivo de datos (JSON o diccionarios de Python) con 20 Pokémon asegurando que se cubran los 18 tipos elementales oficiales.
- [ ] **1.4. Atributos Completos:** Asegurar que cada Pokémon tenga `id`, `nombre`, `tipo_1`, `tipo_2`, estadísticas base completas ($HP, Atk, Def, Sp.Atk, Sp.Def, Speed$) y una lista de 4 movimientos.

---

## Fase 2: Construcción del Modelo Orientado a Objetos (POO)
**Objetivo:** Implementar la abstracción, encapsulamiento y estructura de clases.
*Correspondencia en PDF: Sección 4 (Clases propuestas) y Evaluación (Diseño POO 35%).*

- [ ] **2.1. Clase `Movimiento`:** Implementar atributos y métodos `consumir_pp()` y `es_valido()`.
- [ ] **2.2. Clase `Pokemon`:** Implementar atributos (calculando $HP$ máximo) y métodos `recibir_daño(cantidad)`, `esta_debilitado()` y `obtener_estadistica()`.
- [ ] **2.3. Clase `Entrenador` (Adaptada 1v1):** Implementar con un solo `pokemon_activo` (eliminando la lista de equipo y el método de cambio de Pokémon).
- [ ] **2.4. Clase `Batalla` (Esqueleto):** Crear la estructura principal con `jugador1`, `jugador2` y los métodos `iniciar_combate()`, `procesar_turno()`, `resolver_prioridad()`, `calcular_daño()`, y `verificar_ganador()`.

---

## Fase 3: Motor Matemático y Computación Estocástica
**Objetivo:** Desarrollar el corazón de la simulación y las reglas físicas.
*Correspondencia en PDF: Sección 5 (Mecánica de Combate y Simulación Estocástica).*

- [ ] **3.1. Prioridad de Turno:** Implementar lógica donde ataca primero el de mayor `velocidad`. Si hay empate, resolver con probabilidad $p = 0.5$.
- [ ] **3.2. Simulación Estocástica (Precisión):** Implementar $r \sim U(1, 100) \le \text{Precisión}$. Si falla, restar PP pero no calcular daño.
- [ ] **3.3. Simulación Estocástica (Crítico):** Implementar la probabilidad de $6.25\%$ ($1/16$) para asestar un golpe crítico (multiplicador 1.5).
- [ ] **3.4. Fórmula de Daño Oficial:** Integrar todo asumiendo Nivel = 50:
  - Validar Ataque Físico vs. Defensa Física O Ataque Especial vs. Defensa Especial.
  - Calcular STAB (1.5 si tipo de ataque coincide con tipo del atacante).
  - Calcular Efectividad (incluyendo el producto de dos tipos si el defensor es dual).
  - Generar el factor aleatorio continuo $U(0.85, 1.00)$.
  - Completar la ecuación: $Daño = (((2 \times 50 / 5) + 2) \times Potencia \times (A/D) / 50) + 2) \times Modificador$.

---

## Fase 4: Interfaz de Consola (CLI) y Ciclo de Juego
**Objetivo:** Unir todas las piezas en un flujo jugable y robusto.
*Correspondencia en PDF: Sección 5 (Interfaz CLI) y Evaluación (Interfaz CLI 10%).*

- [ ] **4.1. HUD de Batalla:** Imprimir al inicio del turno los nombres, $HP$ actual/máximo y los Puntos de Poder (PP) de los movimientos.
- [ ] **4.2. Fase de Comandos:** Solicitar al Jugador 1 y luego al Jugador 2 que elijan un ataque (del 1 al 4). *Nota: No se solicitará opción de cambio.*
- [ ] **4.3. Higienización de Inputs:** Manejar errores (ej. si el usuario ingresa letras en lugar de números) para que el programa no colapse.
- [ ] **4.4. Casos de Prueba (Validación):** Correr los combates de prueba (ej. Jolteon vs Gyarados, Snorlax vs Charizard) para confirmar que las matemáticas coinciden con los casos del PDF.


# Arbol del Proyecto

![alt text](image.png)