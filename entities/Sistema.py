from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Clientes import ClienteParticular, Empresa
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from Exeptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste

def ingresar_int(msg, min_value = 0):

    while True:
        try:
            a = int(input(msg))
            if a < min_value:
                raise Exception # Se podría tirar otra excepcion

        except ValueError as e:
            print("El valor ingresado debe ser un entero. Ingrese el dato nuevamente")

        except: # Tirar una excepción ...
            print(f"El valor ingresado debe ser mayor o igual a {min_value}")

        else:
            break

    return a



def ingresar_float(msg, min_value = 0):

    while True:
        try:
            a = float(input(msg))
            if a < min_value:
                raise Exception # Se podría tirar otra excepcion

        except ValueError as e:
            print("El valor ingresado debe ser un número. Ingrese el dato nuevamente")

        except Exception as e:
            print(f"El valor ingresado debe ser mayor o igual a {min_value}")

        else:
            break

    return a

        

    

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []

    def registrar_pieza(self):
        descripcion = input("Descripción: ")
        # Validar descripción única
        for pieza in self.piezas:
            if pieza.descripcion.lower() == descripcion.lower():
                raise ExceptionPiezaYaExiste(descripcion)

        costo = ingresar_float("Costo por unidad: ")
        tamanio_lote = int(input("Tamaño del lote: ")) 
        cantidad = int(input("Cantidad disponible: ")) 

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")


    def registrar_maquina(self):
        descripcion = input("Descripción de la máquina: ")
        # Validar descripción única
        for maquina in self.maquinas:
            if maquina.descripcion.lower() == descripcion.lower():
                raise ExceptionMaquinaYaExiste(descripcion)

        nueva_maquina = Maquina(descripcion)
        piezas_agregadas = []

        while True:
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
                            piezas_agregadas.append(pieza_seleccionada.codigo)
                            print(f"Pieza '{pieza_seleccionada.descripcion}' agregada.")

        if not nueva_maquina.requerimientos:
            print("No se agregó ninguna pieza. La máquina no será registrada.")
            return

        self.maquinas.append(nueva_maquina)
        print(f"Máquina registrada ({nueva_maquina.codigo}).")

        
    def registrar_cliente(self):
        tipo = input("Seleccionar tipo cliente:\n1 Particular\n2 Empresa\n>")
        if tipo == "1":
            cedula = input("Ingrese cédula: ")
            nombre = input("Ingrese nombre completo: ")
            telefono = input("Ingrese teléfono: ")
            correo = input("Ingrese correo electrónico: ")
            cliente = ClienteParticular(cedula, nombre, telefono, correo)
        elif tipo == "2":
            rut = input("Ingrese RUT: ")
            nombre = input("Ingrese nombre de la empresa: ")
            pagina = input("Ingrese página web: ")
            telefono = input("Ingrese teléfono de contacto: ")
            correo = input("Ingrese correo electrónico de contacto: ")
            cliente = Empresa(rut, nombre, pagina, telefono, correo)
        else:
            print ("Tipo cliente no disponible")
            return None
        
        self.clientes.append(cliente)
        print("\nCliente registrado:")
        print(cliente)
        return cliente
        


    
