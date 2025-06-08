class ExceptionClienteYaExiste(Exception):
    def __init__(self, mensaje="Cliente existente"):
        super().__init__(mensaje)
        self.mensaje = mensaje

   
            
        