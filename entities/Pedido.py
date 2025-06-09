from datetime import datetime
contador_id = 1

def generar_id():
    global contador_id
    id_actual = contador_id
    contador_id += 1
    return id_actual

class Pedido:
    def __init__(self, cliente, maquina):
        self.id = generar_id()
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recibimiento = datetime.now()
        self.fecha_entrega = None 
        self.estado = "pendiente"
        self.precio = maquina.costo_produccion() * 1.5 * (1 - cliente.get_descuento())

    def entrega(self):
        if self.maquina.stock > 0:
            self.maquina.stock -= 1
            self.estado = "entregado"
            self.fecha_entrega = datetime.now()
            print(f"{self.maquina} entregada a {self.cliente}")
        else:
            print(f"Pedido pendiente, no hay stock")