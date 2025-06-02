contador_id = 1

def generar_id():
    global contador_id
    id_actual = contador_id
    contador_id += 1
    return id_actual

    
class Cliente():
    
    def __init__(self,tipo):
       self.id = generar_id()
       self.tipo =  tipo
        
        
class ClienteParticular (Cliente):
   def __init__(self,nombre, cedula, telefono, correo_electronico):
      super().__init__("Particular")
      self.nombre = nombre
      self.cedula = cedula
      self.telefono = telefono
      self.correo = correo_electronico
   
   def descuento (self):
       return 0.0
  


class Empresa(Cliente):
   def __init__(self, rut, nombre,pag_web, telefono, correo_electronico):
      super().__init__("Empresa")
      self.rut = rut
      self.nombre = nombre
      self.pagina = pag_web
      self.telefono = telefono
      self.correo = correo_electronico
   def descuento(self):
       return 0.2

def registro_cliente():
   tipo = input("Seleccionar tipo cliente:\n1 Particular\n2 Empresa\n>")
   if tipo == "1":
        cedula = input("Ingrese cédula: ")
        nombre = input("Ingrese nombre completo: ")
        telefono = input("Ingrese teléfono: ")
        correo = input("Ingrese correo electrónico: ")
        cliente = ClienteParticular(cedula, nombre, telefono, correo)
   elif tipo == "2":
        rut = input("Ingrese RUT: ")
        nombre = input("Ingrese nombre de la empresa: ")
        pagina = input("Ingrese página web: ")
        telefono = input("Ingrese teléfono de contacto: ")
        correo = input("Ingrese correo electrónico de contacto: ")
        cliente = Empresa(rut, nombre, pagina, telefono, correo)
   else:
       print ("Tipo cliente no disponible")
       return None
   
   print("\nCliente registrado:")
   for clave, valor in vars(cliente).items():
        print(f"{clave}: {valor}")