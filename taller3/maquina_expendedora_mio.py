class Producto:
    """Representa un producto disponible en la máquina expendedora."""

    def __init__(self, nombre:str, precio:float, codigo:str):
        """Inicializa un producto.

        Parámetros:
            nombre: Nombre del producto.
            precio: Precio del producto.
            codigo: Código que identifica el producto.

        Retorna:
            None: Inicializa los atributos de la instancia.
        """
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo

    def __str__(self):
        """Genera la descripción legible del producto.

        Retorna:
            str: Nombre, precio y código del producto.
        """
        return f' Producto: {self.nombre}\n Precio: {self.precio}\n Código: {self.codigo}'

class RanuraItem:
    """Asocia un producto con la cantidad disponible en una ranura."""

    def __init__(self, producto, cantidad: float):
        """Inicializa una ranura.

        Parámetros:
            producto: Producto almacenado en la ranura.
            cantidad: Unidades disponibles.

        Retorna:
            None: Inicializa los atributos de la instancia.
        """
        self.producto = producto
        self.cantidad = cantidad

    def esta_disponible(self):
        """Comprueba si hay unidades disponibles.

        Retorna:
            bool: True si la cantidad es mayor que cero; False en otro caso.
        """
        return self.cantidad > 0

    def reducir_inventario(self,cantidad):
        """Reduce el inventario en la cantidad indicada si es válida.

        Parámetros:
            cantidad: Unidades que se desean retirar.

        Retorna:
            None: Actualiza el inventario o imprime el error detectado.
        """
        try:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser un número negativo")

            if self.cantidad < cantidad:
                raise ValueError("La cantidad no puede ser mayor a lo que hay en inventario")
            
            if self.esta_disponible():
                self.cantidad -= cantidad


        except ValueError as error:
            print( f'Error : {error}')

    def agregar_inventario(self,cantidad):
        """Aumenta el inventario en la cantidad indicada si es válida.

        Parámetros:
            cantidad: Unidades que se desean agregar.

        Retorna:
            None: Actualiza el inventario o imprime el error detectado.
        """
        try:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser un número negativo")
            
            self.cantidad +=cantidad 
        
        except ValueError as error:
            print( f'Error : {error}')

class Maquina:
    """Controla el inventario, las ventas y el dinero de la máquina."""

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

    def __init__(self, ranuras, dinero: float):
        """Inicializa la máquina con sus ranuras y dinero recaudado.

        Parámetros:
            ranuras: Diccionario con las ranuras del inventario.
            dinero: Dinero inicial de la máquina.

        Retorna:
            None: Inicializa el inventario, el dinero y el saldo.
        """
        self.ranuras = ranuras
        self.dinero = dinero
        self.saldo = 0

    def actualizar_ranura(self, codigo, nuevo_nombre = None, nuevo_precio = None, nuevo_codigo = None, nueva_cantidad = None):    
        """Actualiza los datos de una ranura existente.

        Parámetros:
            codigo: Código actual de la ranura.
            nuevo_nombre: Nombre nuevo opcional del producto.
            nuevo_precio: Precio nuevo opcional.
            nuevo_codigo: Código nuevo opcional para la ranura.
            nueva_cantidad: Inventario nuevo opcional.

        Retorna:
            str: Mensaje que indica el resultado de la operación.
        """
        
        if codigo not in self.ranuras:
            return 'El código no existe'
        item = self.ranuras[codigo]

        if nuevo_precio is not None and nuevo_precio < 0:
            return "El nuevo precio no puede ser un número negativo"

        if nueva_cantidad is not None and nueva_cantidad < 0:
            return "La nueva cantidad no puede ser negativa"

        if nuevo_nombre is not None:
            item.producto.nombre = nuevo_nombre
        

        if nuevo_precio is not None:
            item.producto.precio = nuevo_precio

        if nueva_cantidad is not None:
            item.cantidad = nueva_cantidad

        if nuevo_codigo is not None and nuevo_codigo != codigo:
            if nuevo_codigo in self.ranuras:
                return "El código ya existe"

            del self.ranuras[codigo]
            self.ranuras[nuevo_codigo] = item
            item.producto.codigo = nuevo_codigo

        return "Ranura actualizada"  
    
    def agregar_ranura(self, codigo_ranura = None, nombre = None, precio = None, cantidad = None):
        """Agrega una ranura nueva al inventario.

        Parámetros:
            codigo_ranura: Código único de la ranura.
            nombre: Nombre del producto.
            precio: Precio del producto.
            cantidad: Cantidad inicial del producto.

        Retorna:
            str: Mensaje que indica si se agregó la ranura o el error.
        """
        
        if codigo_ranura is None or nombre is None or precio is None or cantidad is None:
            return "Todos los datos son obligatorios"
        if codigo_ranura in self.ranuras:
            return "El código ya existe"

        if precio < 0 or cantidad < 0:
            return "El precio o la cantidad no pueden ser negativos"

        self.ranuras[codigo_ranura] = RanuraItem(Producto(nombre, precio, codigo_ranura), cantidad)

        return "Ranura agregada"

    def mostrar_inventario(self):
        """Imprime las ranuras, productos y cantidades disponibles.

        Retorna:
            None: Escribe el inventario en la salida estándar.
        """
        for codigo, item in self.ranuras.items():
            print(f'Ranura {codigo}:')
            print(item.producto)
            print(f'Cantidad disponible: {item.cantidad}')
        
    def ingresar_dinero(self, monto):
        """Añade un monto al saldo de la transacción si es válido.

        Parámetros:
            monto: Monto que se desea ingresar.

        Retorna:
            None: Actualiza el saldo o imprime un error de validación.
        """
        try:
            if monto <= 0:
                raise ValueError("El monto ingresado no puede ser negativo")
            self.saldo += monto
        except ValueError as error:
            print(f'Error : {error}')

    def seleccionar_producto(self,codigo):
        """Intenta vender una unidad del producto indicado.

        Parámetros:
            codigo: Código de la ranura que se desea comprar.

        Retorna:
            str: Mensaje de error o confirmación con el cambio.
        """
        if codigo not in self.ranuras:
            return "El código no existe"

        precio = self.ranuras[codigo].producto.precio
        item = self.ranuras[codigo] 

        if not item.esta_disponible():
            return "Producto agotado"

        if self.saldo < precio:
            return "Saldo insuficiente"

        item.cantidad -= 1
        cambio = self.saldo - precio
        self.saldo = 0
        self.dinero += precio

        return f"Entrega de {item.producto.nombre}. Su cambio es: {cambio}"



    def devolver_cambio(self):
        """Devuelve el saldo actual y reinicia la transacción.

        Retorna:
            str: Mensaje con el monto devuelto o indicando que no hay saldo.
        """
        if self.saldo <= 0:
            return 'No hay dinero para devolver'
        
        cambio = self.saldo
        self.saldo = 0
        return f'Se devuelve : {cambio}'

class Monedero:
    """Marcador reservado para la futura implementación de un monedero."""

    pass
