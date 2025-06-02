from datetime import datetime

class Pedido:

 def __init__(self, cliente, maquina):
    self.cliente = cliente
    self.maquina = maquina
    self.fecha_recibimiento = datetime.now()
    self.fecha_entrega = None 
    self.estado = "Pendiente"
    self.precio = self.calculo_precio()


    if self.maquina.esta_disponible():
      self.entrega


 def calculo_precio(self):
    precio_ini = self.maquina.precio * 1,5
    descuento = self.cliente.get_descuento()
    return precio_ini * (1- descuento) 
   
 def entrega (self):