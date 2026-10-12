# Taller 3: Máquina expendedora de productos

Implementación de una máquina expendedora por consola, desarrollada como continuación del taller de máquina expendedora de productos. El programa maneja un catálogo de productos, inventario por ranura, compras, saldo y operaciones administrativas.

## Archivos del taller

- [`maquina_expendedora_mío.py`](./maquina_expendedora_m%C3%ADo.py): archivo original realizado por mí. En el enunciado también se hace referencia a este archivo como `maquina_expendedora_mio.py`.

- [`maquina_expendedora_claude.py`](./maquina_expendedora_claude.py): versión corregida con ayuda de Claude. Conserva la estructura y la lógica propuesta originalmente, e incorpora validaciones y ajustes para mejorar el funcionamiento.
- [`Taller 2 - Maquina expendedora de productos.pdf`](./Taller%202%20-%20Maquina%20expendedora%20de%20productos.pdf): documento de referencia del taller anterior.

> **Aclaración de autoría:** el archivo original hecho por mí es `maquina_expendedora_mio.py` (guardado en esta carpeta como `maquina_expendedora_mío.py`). El archivo corregido es `maquina_expendedora_claude.py`.

## Requisitos

- Python 3.9 o posterior.
- No se requieren paquetes externos; la versión corregida utiliza únicamente módulos de la biblioteca estándar (`copy` y `math`).

## Ejecución

Desde esta carpeta, ejecutar la versión corregida:

```bash
python maquina_expendedora_claude.py
```

Para ejecutar el archivo original en Windows PowerShell:

```powershell
python .\maquina_expendedora_mío.py
```

El menú principal permite ver el catálogo, ingresar dinero, comprar un producto, cancelar una compra y retirar el saldo, entrar al modo administrador o salir. Al salir, la versión corregida devuelve automáticamente el saldo que todavía esté pendiente.

## Organización del programa

### Clases

- **`Producto`**: contiene el nombre, el precio y el código de un producto.
- **`RanuraItem`**: vincula un `Producto` con la cantidad disponible y permite consultar, reducir o aumentar el inventario.
- **`Maquina`**: administra el inventario, el recaudo, las compras y las ranuras. Su inventario inicial incluye diez productos con códigos `A1` a `A10`.
- **`Monedero`**: en la versión corregida, mantiene el saldo de la transacción y valida las denominaciones aceptadas. En el archivo original la clase está declarada como marcador vacío.
- **`DenominacionInvalidaError`**: excepción de la versión corregida para indicar que se intentó ingresar una denominación no aceptada.

### Funcionalidades principales

- **Compras:** se selecciona una ranura por su código. Si hay existencias y saldo suficiente, se descuenta una unidad, se contabiliza el precio en el recaudo y se entrega el cambio restante.
- **Ingreso de dinero:** la versión corregida acepta por defecto denominaciones de `$1.000`, `$2.000`, `$5.000` y `$10.000`.
- **Administración:** permite reabastecer productos, agregar nuevas ranuras, modificar datos y consultar el inventario.
- **Validaciones en la versión corregida:** valida datos de productos, precios, cantidades, denominaciones y códigos; normaliza códigos quitando espacios y convirtiéndolos a mayúsculas; además, copia el inventario inicial para que distintas instancias no compartan modificaciones.
- **Devolución de saldo:** permite cancelar una operación y recuperar el saldo sin utilizar.

## Documentación del código

Las clases y los métodos principales incluyen docstrings con el propósito, los parámetros y los valores de retorno. La versión corregida también documenta las funciones de la interfaz de consola y las funciones auxiliares.

## Diferencias entre las versiones

La versión original contiene la implementación inicial de las clases y operaciones de inventario, ingreso de dinero, compra y devolución de cambio. La versión corregida conserva ese planteamiento y agrega, entre otros ajustes, validaciones de tipos y valores, control de denominaciones, normalización de códigos, aislamiento del inventario entre máquinas y manejo del saldo mediante `Monedero`.
