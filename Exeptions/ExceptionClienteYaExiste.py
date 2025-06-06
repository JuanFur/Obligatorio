class ExceptionClienteYaExiste(Exception):
    def __init__(self, mensaje="Cliente existente"):
        self.mensaje = mensaje
        def __str__(self):
            return f"Problema: {self.mensaje}"