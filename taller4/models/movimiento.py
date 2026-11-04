class Movimiento:
    def __init__(self, nombre: str, tipo: str, categoria: str, potencia: int, precision: int, pp_max: int):
        self.nombre = nombre
        self.tipo = tipo
        self.categoria = categoria
        self.potencia = potencia
        self.precision = precision
        self.pp_max = pp_max
        self.pp_actual = pp_max  # Inicia con el máximo de puntos de poder

    def consumir_pp(self) -> None:
        """Reduce en 1 los Puntos de Poder actuales."""
        if self.pp_actual > 0:
            self.pp_actual -= 1

    def es_valido(self) -> bool:
        """Verifica si el movimiento tiene PP restantes para ser usado."""
        return self.pp_actual > 0

    def copiar(self) -> 'Movimiento':
            """Crea y retorna una instancia completamente nueva e independiente."""
            return Movimiento(
                nombre=self.nombre,
                tipo=self.tipo,
                categoria=self.categoria,
                potencia=self.potencia,
                precision=self.precision,
                pp_max=self.pp_max
            )
        
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - PP: {self.pp_actual}/{self.pp_max}"