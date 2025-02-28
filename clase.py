class Lote:
    def __init__(self, name, manzana, lote, direction, superficie, monto):
        self.name = name  # Tiene que ser una Cadena
        self.manzana = manzana  # Numero: entre 1 y 35
        self.lote = lote  # Numero entre 1 20
        self.direction = direction  # 1: Norte, 2: Sur, 3: Este, 4: Oeste
        self.superficie = superficie
        self.monto = monto


    def __str__(self):
        orientacion = ("Norte", "Sur", "Este", "Oeste")
        return (f" | Cliente: {self.name:<13} | Manzana: {self.manzana:<2} | Lote: {self.lote:<2} | Direccion: "
                f"{orientacion[self.direction -1]:<5} | Superficie: {self.superficie:<6} | Monto: {self.monto:<7} |")