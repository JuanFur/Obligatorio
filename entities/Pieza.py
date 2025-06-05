class Pieza: 
    contador_codigo = 1
    def __init__(self, descripcion, costo, tamanio_lote, cantidad_disponible=0):
        self.codigo = Pieza.contador_codigo
        Pieza.contador_codigo += 1
        self.descripcion = descripcion
        self.costo = costo
        self.tamanio_lote = tamanio_lote
        self.cantidad_disponible = cantidad_disponible

    def __str__(self):
        return f"Pieza {self.codigo}: {self.descripcion} (Stock actualizado: {self.cantidad_disponible})"
  