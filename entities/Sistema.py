from entities.Pieza import Pieza
from entities.Maquina import Maquina
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []

    def registrar_pieza(self):
        descripcion = input("Descripción: ")
        # Validar descripción única
        for pieza in self.piezas:
            if pieza.descripcion() == descripcion():
                raise ExceptionPiezaYaExiste(descripcion)
        costo = float(input("Costo por unidad: "))
        tamanio_lote = int(input("Tamaño del lote: "))
        cantidad = int(input("Cantidad disponible: "))

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")


def registrar_maquina(self):
    descripcion = input("Descripción de la máquina: ")
    # Validar descripción única
    for maquina in self.maquinas:
        if maquina.descripcion == descripcion:
            print(f"Error: Ya existe una máquina con la descripción {descripcion}.")
            return

    nueva_maquina = Maquina(descripcion)
    piezas_agregadas = []

    while True:
        # Mostrar piezas disponibles para agregar (ocultar ya seleccionadas)
        piezas_disponibles = []
        for pieza in self.piezas:
            if pieza.codigo not in piezas_agregadas:
                piezas_disponibles.append(pieza)

        if not piezas_disponibles:
            print("No hay más piezas disponibles para agregar.")
            break

        print("Piezas disponibles:")
        for pieza in piezas_disponibles:
            print(f"{pieza.codigo}: {pieza.descripcion} (Stock: {pieza.cantidad_disponible})")

        codigo_pieza = input("Ingrese el código de la pieza a agregar (o ENTER para terminar): ")
        if not codigo_pieza.strip():
            break

        try:
            codigo_pieza = int(codigo_pieza)
        except ValueError:
            print("Código inválido.")
            # No usamos continue, simplemente saltamos al final del while
        else:
            pieza_seleccionada = None
            for p in piezas_disponibles:
                if p.codigo == codigo_pieza:
                    pieza_seleccionada = p
                    break

            if pieza_seleccionada is None:
                print("Pieza no encontrada o ya agregada.")
            else:
                cantidad_input = input(f"Cantidad necesaria de '{pieza_seleccionada.descripcion}': ")
                try:
                    cantidad = int(cantidad_input)
                except ValueError:
                    print("Cantidad inválida.")
                else:
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0.")
                    else:
                        nueva_maquina.agregar_requerimiento(pieza_seleccionada, cantidad)
                        piezas_agregadas.add(pieza_seleccionada.codigo)
                        print(f"Pieza '{pieza_seleccionada.descripcion}' agregada.")

    if not nueva_maquina.requerimientos:
        print("No se agregó ninguna pieza. La máquina no será registrada.")
        return

    self.maquinas.append(nueva_maquina)
    print(f"Máquina registrada ({nueva_maquina.codigo}).")
        


    
