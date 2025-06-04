from datetime import datetime

class Pedido:

 def __init__(self, cliente, maquina, empresa):
    self.cliente = cliente
    self.maquina = maquina
    self.fecha_recibimiento = datetime.now()
    self.fecha_entrega = None 
    self.estado = "Pendiente"
    self.precio = self.calculo_precio()

 def calculo_precio(self):
    precio_ini = self.maquina.costo_produccion * 1,5
    if self.cliente.empresa():
      return precio_ini * 0.8
    return precio_ini
   
 def entrega (self):
   if self.estado == "pendiente":

     self.estado = "entregado"   
     self.fecha_entrega = self.fecha_recibimiento
     print(f"{self.maquina} entregada a {self.cliente}")