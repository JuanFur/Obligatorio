class Requerimiento:
    def __init__(self, pieza, maquina, cantidad):
        self.pieza = pieza
        self.cantidad = cantidad
    
    def __str__(self):
        return f"{self.cantidad} x {self.pieza.descripcion}"