class Maquina:
    codigo = 1 
    def __init__(self, codigo, descripcion, agregar_requisito, requerimientos, pieza, cantidad):
        self.codigo = codigo
        Maquina.codigo +=1
        self.descripcion = descripcion
        self.requerimientos = requerimientos
        self.agregar_requisito = agregar_requisito
        self.pieza = pieza
        self.cantidad = cantidad

if __name__ == "__main__":