"""
Este ejecutable de python fue realizado con Claude code como corrección al archivo original maquina_expendedora_mio.py,
ejecutable que está en esta misma raíz.

Este archivo conserva la lógica original propuesta de dividir responsabilidades entre clases, sin embargo, es una corrección al trabajo realizado
el cual no se culminó a tiempo.

En general las anotaciones # de Claude son correcciones o adiciones consideradas como buenas prácticas.

"""

import copy
import math


# [FIX] Helper compartido: rechaza strings, None, bool, NaN e infinito.
# Sin esto, un NaN pasa todas las comparaciones "< 0" sin ser detectado.
def _es_numero(valor):
    return (
        isinstance(valor, (int, float))
        and not isinstance(valor, bool)
        and math.isfinite(valor)
    )


# Formato de pesos colombianos: 2000 -> $2.000
def formato_pesos(valor):
    return "$" + f"{valor:,.0f}".replace(",", ".")


class Producto:
    def __init__(self, nombre:str, precio:float, codigo:str):
        # [FIX] Validaciones 
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        if not _es_numero(precio) or precio < 0:
            raise ValueError("El precio debe ser un número no negativo")
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código del producto no puede estar vacío")

        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo

    def __str__(self):
        return f' Producto: {self.nombre}\n Precio: {formato_pesos(self.precio)}\n Código: {self.codigo}'

class RanuraItem:
    def __init__(self, producto, cantidad: float):
        # [FIX] Validaciones adicionales
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser una instancia de Producto")
        if not _es_numero(cantidad) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número no negativo")

        self.producto = producto
        self.cantidad = cantidad

    def esta_disponible(self):
        return self.cantidad > 0

    def reducir_inventario(self,cantidad):
        try:
            # [FIX] Antes, un str/None lanzaba TypeError, que el except no atrapaba
            if not _es_numero(cantidad):
                raise ValueError("La cantidad debe ser un número")

            if cantidad < 0:
                raise ValueError("La cantidad no puede ser un número negativo")

            if self.cantidad < cantidad:
                raise ValueError("La cantidad no puede ser mayor a lo que hay en inventario")

            # [FIX] Se eliminó el "if self.esta_disponible()": era redundante
            # (si no había stock, la validación anterior ya había fallado).
            self.cantidad -= cantidad
            return True  # [FIX] Ahora informa si la operación tuvo éxito

        except ValueError as error:
            print( f'Error : {error}')
            return False

    def agregar_inventario(self,cantidad):
        try:
            if not _es_numero(cantidad):  # [FIX] mismo caso que arriba
                raise ValueError("La cantidad debe ser un número")

            if cantidad < 0:
                raise ValueError("La cantidad no puede ser un número negativo")

            self.cantidad +=cantidad
            return True

        except ValueError as error:
            print( f'Error : {error}')
            return False

# ---------------------------------------------------------------------------
# NUEVA CLASE
# ---------------------------------------------------------------------------
class DenominacionInvalidaError(ValueError):
    """Se lanza cuando se ingresa un billete o moneda no aceptado."""
    pass


class Monedero:
    """Saldo temporal de la transacción en curso + validación de denominaciones."""

    def __init__(self, denominaciones_aceptadas: list = None):
        if denominaciones_aceptadas is None:
            denominaciones_aceptadas = [1000, 2000, 5000, 10000]

        if not denominaciones_aceptadas:
            raise ValueError("Debe haber al menos una denominación aceptada")
        if any(not _es_numero(d) or d <= 0 for d in denominaciones_aceptadas):
            raise ValueError("Las denominaciones deben ser números mayores a cero")

        self.saldo_actual: float = 0.0
        # Copia defensiva: modificar la lista original no altera el monedero
        self.denominaciones_aceptadas: list = sorted(set(denominaciones_aceptadas))

    def ingresar(self, monto):
        """Valida la denominación y la suma al saldo. Lanza excepción si no es válida."""
        if isinstance(monto, bool) or monto not in self.denominaciones_aceptadas:
            raise DenominacionInvalidaError(
                f"Denominación no válida: {monto}. "
                f"Aceptadas: {self.denominaciones_aceptadas}"
            )
        self.saldo_actual += monto

    def tiene_suficiente(self, costo) -> bool:
        return self.saldo_actual >= costo

    def descontar(self, costo):
        """Resta el costo del saldo. Lanza excepción si el costo es inválido o el saldo no alcanza."""
        if not _es_numero(costo) or costo < 0:
            raise ValueError("El costo debe ser un número no negativo")
        if not self.tiene_suficiente(costo):
            raise ValueError("Saldo insuficiente")
        self.saldo_actual -= costo

    def devolver_cambio(self) -> float:
        """Retorna el saldo restante y reinicia la transacción a 0."""
        cambio = self.saldo_actual
        self.saldo_actual = 0.0
        return cambio

    def __str__(self):
        return f' Saldo actual: {self.saldo_actual}\n Denominaciones aceptadas: {self.denominaciones_aceptadas}'
# ---------------------------------------------------------------------------


class Maquina:

    # Se conserva como plantilla de inventario inicial.
    # [FIX] Ya no se comparte entre instancias: __init__ trabaja sobre una copia.
    ranuras = {
        "A1" : RanuraItem(Producto('cereal', 2000, 'A1'), 10),
        "A2" : RanuraItem(Producto('yogurt', 3000, 'A2'), 10),
        "A3" : RanuraItem(Producto('chocorramo', 2000, 'A3'), 10),
        "A4" : RanuraItem(Producto('cocacola', 4000, 'A4'), 10),
        "A5" : RanuraItem(Producto('jamon', 4000, 'A5'), 10),
        "A6" : RanuraItem(Producto('avena', 5000, 'A6'), 10),
        "A7" : RanuraItem(Producto('galletas', 2000, 'A7'), 10),
        "A8" : RanuraItem(Producto('chocolatina', 2000, 'A8'), 10),
        "A9" : RanuraItem(Producto('gomitas', 3000, 'A9'), 10),
        "A10" : RanuraItem(Producto('sanduche', 5000, 'A10'), 10)
    }

    # [FIX] ranuras ahora es opcional (usa la plantilla) y dinero tiene valor por defecto.
    # Maquina(Maquina.ranuras, 0) sigue funcionando igual que antes.
    def __init__(self, ranuras=None, dinero: float = 0):
        if ranuras is None:
            ranuras = Maquina.ranuras
        if not isinstance(ranuras, dict):
            raise ValueError("Las ranuras deben ser un diccionario")
        if not _es_numero(dinero) or dinero < 0:
            raise ValueError("El dinero de la máquina debe ser un número no negativo")

        # [FIX] Copia profunda: dos máquinas ya no se pisan el inventario
        # y la plantilla de clase no se corrompe.
        self.ranuras = copy.deepcopy(ranuras)
        self.dinero = dinero
        self.monedero = Monedero()  # [NUEVO] reemplaza al antiguo self.saldo

    @property
    def saldo(self):
        # [NUEVO] Compatibilidad: maquina.saldo sigue existiendo, ahora viene del monedero
        return self.monedero.saldo_actual

    # [NUEVO] Los códigos se comparan sin espacios y en mayúsculas ("a1 " -> "A1")
    @staticmethod
    def _normalizar_codigo(codigo):
        return str(codigo).strip().upper()

    def actualizar_ranura(self, codigo, nuevo_nombre = None, nuevo_precio = None, nuevo_codigo = None, nueva_cantidad = None):

        codigo = self._normalizar_codigo(codigo)

        if codigo not in self.ranuras:
            return 'El código no existe'
        item = self.ranuras[codigo]

        # [FIX] TODAS las validaciones ocurren antes de modificar nada.
        # Antes, si nuevo_codigo ya existía, el nombre/precio/cantidad
        # ya habían cambiado cuando se retornaba el error.
        if nuevo_nombre is not None and (not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip()):
            return "El nuevo nombre no puede estar vacío"

        if nuevo_precio is not None:
            if not _es_numero(nuevo_precio):
                return "El nuevo precio debe ser un número"
            if nuevo_precio < 0:
                return "El nuevo precio no puede ser un número negativo"

        if nueva_cantidad is not None:
            if not _es_numero(nueva_cantidad):
                return "La nueva cantidad debe ser un número"
            if nueva_cantidad < 0:
                return "La nueva cantidad no puede ser negativa"

        if nuevo_codigo is not None:
            nuevo_codigo = self._normalizar_codigo(nuevo_codigo)
            if nuevo_codigo == "":
                return "El nuevo código no puede estar vacío"
            if nuevo_codigo != codigo and nuevo_codigo in self.ranuras:
                return "El código ya existe"

        # Aplicación de cambios (ya validado todo)
        if nuevo_nombre is not None:
            item.producto.nombre = nuevo_nombre.strip()

        if nuevo_precio is not None:
            item.producto.precio = nuevo_precio

        if nueva_cantidad is not None:
            item.cantidad = nueva_cantidad

        if nuevo_codigo is not None and nuevo_codigo != codigo:
            del self.ranuras[codigo]
            self.ranuras[nuevo_codigo] = item
            item.producto.codigo = nuevo_codigo

        return "Ranura actualizada"

    def agregar_ranura(self, codigo_ranura = None, nombre = None, precio = None, cantidad = None):

        if codigo_ranura is None or nombre is None or precio is None or cantidad is None:
            return "Todos los datos son obligatorios"

        codigo_ranura = self._normalizar_codigo(codigo_ranura)  # [NUEVO]

        # [FIX] Validaciones de vacío y de tipo (antes "abc" < 0 lanzaba TypeError)
        if codigo_ranura == "":
            return "El código no puede estar vacío"
        if not isinstance(nombre, str) or not nombre.strip():
            return "El nombre no puede estar vacío"
        if not _es_numero(precio) or not _es_numero(cantidad):
            return "El precio y la cantidad deben ser números"

        if codigo_ranura in self.ranuras:
            return "El código ya existe"

        if precio < 0 or cantidad < 0:
            return "El precio o la cantidad no pueden ser negativos"

        self.ranuras[codigo_ranura] = RanuraItem(Producto(nombre.strip(), precio, codigo_ranura), cantidad)

        return "Ranura agregada"

    def mostrar_inventario(self):
        # [FIX] Antes, con el diccionario vacío no se imprimía nada
        if not self.ranuras:
            print('No hay ranuras registradas')
            return

        for codigo, item in self.ranuras.items():
            print(f'Ranura {codigo}:')
            print(item.producto)
            print(f'Cantidad disponible: {item.cantidad}')

    def ingresar_dinero(self, monto):
        # [CAMBIO] Delegado al Monedero, que valida las denominaciones aceptadas.
        # Ahora retorna el mensaje (como el resto de métodos) en vez de imprimirlo,
        # para que el menú decida cómo mostrarlo.
        try:
            self.monedero.ingresar(monto)
            return f'Saldo actual: {formato_pesos(self.saldo)}'
        except ValueError as error:
            return f'Error : {error}'

    def seleccionar_producto(self,codigo):
        codigo = self._normalizar_codigo(codigo)  # [NUEVO]

        if codigo not in self.ranuras:
            return "El código no existe"

        item = self.ranuras[codigo]
        precio = item.producto.precio

        # [FIX] cantidad < 1 cubre stock fraccionario (ej. 0.5), que antes
        # pasaba esta_disponible() y dejaba el inventario en negativo.
        if not item.esta_disponible() or item.cantidad < 1:
            return "Producto agotado"

        if not self.monedero.tiene_suficiente(precio):
            return "Saldo insuficiente"

        # [FIX] Se usa reducir_inventario en vez de modificar item.cantidad directamente
        item.reducir_inventario(1)
        self.monedero.descontar(precio)
        self.dinero += precio
        cambio = self.monedero.devolver_cambio()

        return f"Entrega de {item.producto.nombre}. Su cambio es: {formato_pesos(cambio)}"

    def devolver_cambio(self):
        cambio = self.monedero.devolver_cambio()

        if cambio <= 0:
            return 'No hay dinero para devolver'

        return f'Se devuelve : {formato_pesos(cambio)}'


# ---------------------------------------------------------------------------
# INTERFAZ DE LÍNEA DE COMANDOS
# ---------------------------------------------------------------------------
def _a_entero(texto):
    """Convierte '$1.000', '1,000' o '1000' en 1000. Lanza ValueError si no se puede."""
    limpio = texto.strip().replace("$", "").replace(".", "").replace(",", "").replace(" ", "")
    return int(limpio)


def leer_entero(mensaje):
    """Pide un entero. Retorna None (y avisa) si la entrada no es válida."""
    try:
        return _a_entero(input(mensaje))
    except ValueError:
        print("Error : Debe ingresar un número entero válido")
        return None


def leer_entero_opcional(mensaje):
    """Retorna (ok, valor). Si el usuario deja vacío: (True, None)."""
    texto = input(mensaje).strip()
    if texto == "":
        return True, None
    try:
        return True, _a_entero(texto)
    except ValueError:
        print("Error : Debe ingresar un número entero válido")
        return False, None


def mostrar_menu(maquina):
    print("\n" + "=" * 40)
    print("        MÁQUINA EXPENDEDORA")
    print("=" * 40)
    print(f"Saldo actual: {formato_pesos(maquina.saldo)}")
    print("-" * 40)
    print("1. Ver catálogo de productos")
    print("2. Ingresar dinero")
    print("3. Comprar producto")
    print("4. Cancelar y retirar dinero")
    print("5. Modo Administrador")
    print("6. Salir")


def opcion_ingresar_dinero(maquina):
    aceptadas = ", ".join(formato_pesos(d) for d in maquina.monedero.denominaciones_aceptadas)
    print(f"Denominaciones aceptadas: {aceptadas}")
    monto = leer_entero("Monto a ingresar: $")
    if monto is not None:
        print(maquina.ingresar_dinero(monto))


def opcion_comprar(maquina):
    print(f"Saldo disponible: {formato_pesos(maquina.saldo)}")
    codigo = input("Código del producto (ej. A1): ")
    print(maquina.seleccionar_producto(codigo))


def admin_reabastecer(maquina):
    codigo = maquina._normalizar_codigo(input("Código de la ranura a reabastecer: "))
    item = maquina.ranuras.get(codigo)
    if item is None:
        print("El código no existe")
        return

    cantidad = leer_entero(f"Unidades a agregar a {item.producto.nombre} (actual: {item.cantidad}): ")
    if cantidad is None:
        return

    if item.agregar_inventario(cantidad):
        print(f"Stock actualizado. {item.producto.nombre}: {item.cantidad} unidades")


def admin_agregar_ranura(maquina):
    codigo = input("Código de la nueva ranura (ej. B1): ")
    nombre = input("Nombre del producto: ")
    precio = leer_entero("Precio: $")
    if precio is None:
        return
    cantidad = leer_entero("Cantidad inicial: ")
    if cantidad is None:
        return
    print(maquina.agregar_ranura(codigo, nombre, precio, cantidad))


def admin_actualizar_ranura(maquina):
    codigo = input("Código de la ranura a modificar: ")
    print("(Deje vacío cualquier campo que no quiera cambiar)")

    nuevo_nombre = input("Nuevo nombre: ").strip() or None

    ok, nuevo_precio = leer_entero_opcional("Nuevo precio: $")
    if not ok:
        return

    nuevo_codigo = input("Nuevo código: ").strip() or None

    ok, nueva_cantidad = leer_entero_opcional("Nueva cantidad: ")
    if not ok:
        return

    print(maquina.actualizar_ranura(codigo, nuevo_nombre, nuevo_precio, nuevo_codigo, nueva_cantidad))


def menu_administrador(maquina):
    while True:
        print("\n--- MODO ADMINISTRADOR ---")
        print("1. Reabastecer stock")
        print("2. Agregar nueva ranura")
        print("3. Modificar ranura")
        print("4. Ver inventario")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            admin_reabastecer(maquina)
        elif opcion == "2":
            admin_agregar_ranura(maquina)
        elif opcion == "3":
            admin_actualizar_ranura(maquina)
        elif opcion == "4":
            maquina.mostrar_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    maquina = Maquina()

    try:
        while True:
            mostrar_menu(maquina)
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                maquina.mostrar_inventario()
            elif opcion == "2":
                opcion_ingresar_dinero(maquina)
            elif opcion == "3":
                opcion_comprar(maquina)
            elif opcion == "4":
                print(maquina.devolver_cambio())
            elif opcion == "5":
                menu_administrador(maquina)
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrumpido.")

    # Si queda saldo sin usar, se devuelve antes de apagar la máquina
    if maquina.saldo > 0:
        print(maquina.devolver_cambio())
    print("Gracias por usar la máquina expendedora. ¡Hasta pronto!")


if __name__ == "__main__":
    main()