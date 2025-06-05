
from entities.Requerimiento import Requerimiento

class Maquina:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.requerimientos = []

    def agregar_requerimiento(self, pieza, cantidad):
        requerimiento = Requerimiento(pieza, self,cantidad)
        self.requerimientos.append(requerimiento)

    def costo_produccion(self):
        return sum(requerimiento.pieza.costo*requerimiento.cantidad)
