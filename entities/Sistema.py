from entities.Pieza import Pieza
from entities.Maquina import Maquina
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []

    def registrar_pieza(self):
        descripcion = input("Descripción: ")
        # Validar descripción única
        for pieza in self.piezas:
            if pieza.descripcion.lower() == descripcion.lower():
                raise ExceptionPiezaYaExiste(descripcion)
        costo = float(input("Costo por unidad: "))
        tamanio_lote = int(input("Tamaño del lote: "))
        cantidad = int(input("Cantidad disponible: "))

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")


        


    
