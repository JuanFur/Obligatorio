from datetime import datetime

class Pedido:

 def __init__(self, cliente, maquina):
    self.cliente = cliente
    self.maquina = maquina
    self.fecha_recibimiento = datetime.now()
    self.fecha_entrega = None 
    self.estado = "Pendiente"
    self.precio = self.calculo_precio()

 def calculo_precio(self):
    precio_ini = self.maquina.precio
   
 def entrega (self):