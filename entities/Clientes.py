from Exeptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste

contador_id = 1
cedulas_registradas=[]

def nombre_valido(nombre):
    if not nombre.replace(" ","").isalpha():
        raise ExceptionClienteYaExiste("El nombre debe contener solo letras")
    return nombre
def cedula_valida(cedula):
    if len(cedula) != 8 or not cedula.isdigit():
        raise ValueError("Debe tener 8 digitos numericos")
    return cedula
    
    
def generar_id():
    global contador_id
    id_actual = contador_id
    contador_id += 1
    return id_actual

class Cliente():
    
    def __init__(self,tipo, telefono, correo_electronico):
       self.id = generar_id()
       self.tipo =  tipo
       self.telefono=telefono
       self.correo = correo_electronico
      

    def get_descuento (self):
       return 0.0
    
    def __str__(self):
        return f"{self.tipo} ID: {self.id}"
        
        
class ClienteParticular (Cliente):
   def __init__(self, nombre, cedula, telefono, correo_electronico):
      super().__init__("Particular", telefono, correo_electronico)
      self.nombre_completo = nombre
      self.cedula = cedula
      cedulas_registradas.append(cedula)
   
   def __str__(self):
       return f"{super().__str__()}- Nombre: {self.nombre_completo}- Cédula: {self.cedula}"
   
class Empresa(Cliente):
   def __init__(self, rut, nombre,pag_web, telefono, correo_electronico):
      super().__init__("Empresa", telefono, correo_electronico)
      self.rut = rut
      self.nombre = nombre
      self.pagina = pag_web
   
   def get_descuento(self):
       return 0.2
   
   def __str__(self):
       return f"{super().__str__()} Empresa: {self.nombre} RUT: {self.rut}"