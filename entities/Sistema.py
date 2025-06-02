from entities.Pieza import Pieza
from Maquina import Maquina
from Requerimiento import Requerimiento

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquina = []


    def registrar_pieza(self):
        descripcion = input("Descripción: ")
        costo = float(input("Costo por unidad: "))
        tamanio_lote = int(input("Tamaño del lote: "))
        cantidad = int(input("Cantidad disponible: "))

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")

    def registrar_maquina(self):
        descripcion = input("Descripción: ")
        
        for maquina in self.maquinas:
            if maquina.descripcion == descripcion:
                print("Ya existe esa máquina")
                return
        requerimientos = []
