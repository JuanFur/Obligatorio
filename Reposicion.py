from datetime import datetime

class Reposición:
    def __init__(self, pieza, cantidad_lotes):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = datetime.now()
        