from datetime import datetime

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()

        self.cantidad_total = self.tamanio_lote * self.cantidad_lotes
        self.costo = self.pieza.costo * self.cantidad_total

        self.actualizarstock()

        def actualizarstock(self):
            self.pieza.cantidad_disponible += self.cantidad_total

        def __str__(self):
            return (f"Reposición de {self.pieza.descripcion}, {self.cantidad_lotes} lotes"
                    f"en {self.fecha}"
                    f"Stock sumado: {self.cantidad_total}"
                    f"Costo total: USD {self.costo_total}")

        