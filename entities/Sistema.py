from entities.Pieza import Pieza

class Sistema:
    def __init__(self):
        self.piezas = []

    def registrar_pieza(self):
        descripcion = input("Descripción: ")
        costo = float(input("Costo por unidad: "))
        tamanio_lote = int(input("Tamaño del lote: "))
        cantidad = int(input("Cantidad disponible: "))

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")

    
