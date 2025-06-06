class ExceptionValorInvalido(Exception):
    def __init__(self, campo):
        super().__init__(f"El valor ingresado para '{campo}' no es válido.")