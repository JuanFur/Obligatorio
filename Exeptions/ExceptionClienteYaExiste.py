class ExceptionClienteYaExiste(Exception):
    def __init__(self, mensaje="Cliente existente"):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def nombre_valido(nombre):
        if not nombre(" ","").isalpha():
            raise ExceptionClienteYaExiste("El nombre debe contener solo letras")
        return nombre
    def cedula_valida(cedula):
        if len(cedula) != 8 and not cedula.isdigit():
            raise ValueError("Debe tener 8 digitos numericos")
        return cedula
    def telefono_valido(telefono):
        if len(telefono) != 9 and not telefono.isdigit():
            raise ValueError("Debe ser de 9 digitos numericos")
        
    def rut_valido (rut):
        if len(rut) != 12 and not rut.isdigit():
            raise ValueError ("Debe ser de 12 digitos numericos")
            
        