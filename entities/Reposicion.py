from datetime import datetime
from entities.Pieza import Pieza

class Reposicion:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()

        self.cantidad_total = self.pieza.tamanio_lote * self.cantidad_lotes
        self.costo_total = self.pieza.costo * self.cantidad_total

        self.actualizar_stock()

    def actualizar_stock(self):
            self.pieza.cantidad_disponible += self.cantidad_total

    def __str__(self):
            return (f"Reposición de {self.pieza.descripcion}, {self.cantidad_lotes} lotes\n"
                    f"en {self.fecha}\n"
                    f"Stock sumado: {self.cantidad_total}\n"
                    f"Costo total: USD {self.costo_total}\n")

if __name__=="__main__":
    pieza = Pieza("Tornillo", 1.5, 100, 50)
    reposicion = Reposicion(pieza, 2)
    reposicion = Reposicion(pieza, 1)
    print(reposicion)
    print("Nuevo stock:", pieza.cantidad_disponible)