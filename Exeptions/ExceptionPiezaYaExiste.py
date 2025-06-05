class ExceptionPiezaYaExiste(Exception):
    def __init__(self, descripcion):
        super().__init__(f"Ya existe una pieza con la descripción: {descripcion}")