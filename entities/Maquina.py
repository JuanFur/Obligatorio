"""
Máquina
Cada máquina deberá tener un código único numérico, una descripción, una lista de
requerimientos de piezas con las respectivas cantidades necesarias para construirla y su
costo de producción.
Se piden los siguientes datos por terminal:
- Descripción
- Agregar requisito de pieza (continuar pidiendo hasta que el usuario seleccione “No”)
- Sí
- Pieza (listar piezas para poder seleccionar una ingresando su código)
- Cantidad
- No
Nuevamente, el código de máquina es generado automáticamente y la descripción debe ser
única. Para seleccionar una pieza, se listan todas las existentes para que el usuario pueda
seleccionar una según el código de pieza correspondiente. Al agregar un nuevo requisito de
pieza, deben ocultarse del listado las piezas ya seleccionadas (para evitar duplicados).
El costo de producción se obtiene directamente como la suma de los costos unitarios de
cada pieza multiplicados por la cantidad necesaria (se omiten costos asociados al proceso
de ensamblado).
"""



class Maquina:
    codigo = 1 
    def __init__(self, codigo, descripcion, agregar_requisito, requerimientos, pieza, cantidad):
        self.codigo = codigo
        Maquina.codigo +=1
        self.descripcion = descripcion
        self.requerimientos = requerimientos
        self.agregar_requisito = agregar_requisito
        self.pieza = pieza
        self.cantidad = cantidad

if __name__ == "__main__":
    print("Hola")
    print(__name__)
    



