class ExceptionMaquinaYaExiste(Exception):
    def __init__(self, descripcion):
        super().__init__(f"Ya existe una máquina con la descripción: {descripcion}")