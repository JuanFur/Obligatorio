id_contador = 1
class Cliente():
    
    
    def __init__(self,telefono,correo_electronico):
        self.telefono = telefono
        self.correo = correo_electronico
        global id_contador
        self.id = id_contador
        id_contador =+ 1
        
        
        
    def numero_telefono (self):
       return  self.telefono
    
    def correo_elec (self):
       return self.correo
       
class ClienteParticular (Cliente):
   def __init__(self,nombre, cedula, telefono, correo_electronico):
      super().__init__(telefono, correo_electronico)
      self.nombre = nombre
      self.cedula = cedula
   def __str__ (self):
      return f"ID: {self.id}\nNOMBRE: {self.nombre}\nCEDULA: {self.cedula}\nCORREO: {self.correo}\nTEL: 0{self.telefono}"

class Empresa(Cliente):
   def __init__(self, rut, nombre,pag_web, telefono, correo_electronico):
      super().__init__(telefono, correo_electronico)
      self.rut = rut
      self.nombre = nombre
      self.pagina = pag_web

   def __str__(self):
       return f"ID:{self.id}\nRut: {self.rut}\nNOMBRE: {self.nombre}\nPAGINA WEB: {self.pagina}\nTEL: 0{self.telefono}\nCORREO:{self.correo}"   



if __name__ == "__main__":
 

 cliente1 = ClienteParticular("Gaspar Reimundez", 59770060, 95745816, "gasparreimundez@gmail.com")
 cliente2 = Empresa(216827000013, "Antonin SA", "antoninSA.www.empresa.uy", 95734882, "antoninsa@empresa.com")
 print(cliente1)
 print ("\n--------------------------------------")
 print (cliente2)