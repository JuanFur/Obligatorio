contador_id = 1

def generar_id():
    global contador_id
    id_actual = contador_id
    contador_id += 1
    return id_actual


class Cliente():
    
    def __init__(self,telefono,correo_electronico):
        self.telefono = telefono
        self.correo = correo_electronico
        self.id = generar_id()
    
    def info_cliente (self):
       print(f"ID: {self.id}")
       print(f"Correo: {self.correo}")
       print(f"tel: {self.telefono}")
    
        
class ClienteParticular (Cliente):
   def __init__(self,nombre, cedula, telefono, correo_electronico):
      super().__init__(telefono, correo_electronico)
      self.nombre = nombre
      self.cedula = cedula
   def info_cliente(self):
     print("Tipo: Particular")
     print(f"Cedula: {self.cedula}")
     print(f"Nombre: {self.nombre}")
     super().info_cliente()



class Empresa(Cliente):
   def __init__(self, rut, nombre,pag_web, telefono, correo_electronico):
      super().__init__(telefono, correo_electronico)
      self.rut = rut
      self.nombre = nombre
      self.pagina = pag_web

   def info_cliente(self):
       print("Tipo: Empresa")
       print(f"RUT: {self.rut}")
       print(f"Nombre: {self.nombre}")
       print(f"Pagina web: {self.pagina}")
       super().info_cliente()

       
       

def registro_cliente():
   tipo = input("Seleccionar tipo cliente:\n1 Particular\n2 Empresa\n>")
   if tipo == "1":
        cedula = input("Ingrese cédula: ")
        nombre = input("Ingrese nombre completo: ")
        telefono = input("Ingrese teléfono: ")
        correo = input("Ingrese correo electrónico: ")
        cliente = ClienteParticular(cedula, nombre, telefono, correo)
   if tipo == "2":
        rut = input("Ingrese RUT: ")
        nombre = input("Ingrese nombre de la empresa: ")
        pagina = input("Ingrese página web: ")
        telefono = input("Ingrese teléfono de contacto: ")
        correo = input("Ingrese correo electrónico de contacto: ")
        cliente = Empresa(rut, nombre, pagina, telefono, correo)
   else:
       print ("Tipo cliente no disponible")
       return
   print("\n Cliente registrado")
   cliente.info_cliente()


registro_cliente()