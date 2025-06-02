"""
Pieza
Cada pieza tendrá un código único numérico, una descripción, un costo de adquisición por
unidad en USD, la cantidad inicial disponible en el stock y el tamaño del lote de reposición
(las piezas son repuestas mediante la compra de lotes de tamaño fijo).
Se piden los siguientes datos por terminal:
- Descripción
- Costo unitario
- Tamaño de lote de reposición
- Cantidad disponible (0 por defecto)
El código del producto es generado automáticamente por el sistema, de modo que sea
único. Debe validarse que la descripción sea única también.

"""

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
  