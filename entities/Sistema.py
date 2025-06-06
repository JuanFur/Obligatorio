from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Clientes import ClienteParticular, Empresa
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from Exeptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste
from entities.Pedido import Pedido
from Exeptions.ExceptionValorInvalido import ExceptionValorInvalido

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
        self.pedido = []

    def registrar_pieza(self):
        while True: #Esto esta raro
            descripcion = input("Descripción: ").strip()
            if not descripcion:
                print("La descripción no puede estar vacía. Intente nuevamente.")
                continue
            # Validar descripción única
            if any(pieza.descripcion == descripcion for pieza in self.piezas):
                raise ExceptionPiezaYaExiste(descripcion)
            break

        while True: 
            try:
                costo = float(input("Costo por unidad: "))
                if costo <= 0:
                    raise ExceptionValorInvalido("Costo por unidad")
            except ValueError:
                print("Debe ingresar un número válido para el costo.")
            except ExceptionValorInvalido as e:
                print(e)
            else:
                break
        
        while True:
            try:
                tamanio_lote_input = input("Tamaño del lote: ")
                tamanio_lote = int(tamanio_lote_input)
                if tamanio_lote <= 0:
                    raise ExceptionValorInvalido("Tamaño del lote")
            except ValueError:
                print("Debe ingresar un número entero para el tamaño del lote.")
            except ExceptionValorInvalido as e:
                print(e)
            else:
                break

        while True:
            try:
                cantidad_input = input("Cantidad disponible: ")
                cantidad = int(cantidad_input)
                if cantidad < 0:
                    raise ExceptionValorInvalido("Cantidad disponible")
            except ValueError:
                print("Debe ingresar un número entero para la cantidad disponible.")
            except ExceptionValorInvalido as e:
                print(e)
            else:
                break

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")


    def registrar_maquina(self):
        descripcion = input("Descripción de la máquina: ")
        while descripcion.strip() == "":
            descripcion = input("La descripcion debe contener caracteres. Intentalo de nuevo: ")
            
        # Validar descripción única
        for maquina in self.maquinas:
            if maquina.descripcion == descripcion:
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
    
    def registrar_pedido(self):
        if not self.clientes:
            print("No hay clientes registrados. Registre un cliente")
            return
        if not self.maquinas:
            print("No hay maquinas registradas. Registre una máquina primero.")
            return
        print("\nClientes disponibles: ")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i} - {cliente}")

        while True:
                opcion_cliente = int(input("\nSeleccione el número del cliente: ")) - 1
                if 0 <= opcion_cliente < len(self.clientes):
                    cliente = self.clientes[opcion_cliente]
                    break
                else:
                    print("Número de cliente inválido. Intente nuevamente")
        
        print("\nMaquinas disponibles: ")
        for i, maquina in enumerate(self.maquinas, 1):
            print(f"{i} - {maquina} - {disponibilidad}")    
        
        while True:
                opcion_maquina = int(input("\nSeleccione el número de la maquina: ")) - 1
                if 0 <= opcion_maquina < len(self.maquinas):
                    maquina = self.maquinas[opcion_maquina]
                    break
                else:
                    print("Número de máquina inválido. Intente nuevamente")

        nuevo_pedido = Pedido(cliente, maquina)
        self.pedidos.append(nuevo_pedido)

        print("\nPedido registrado de forma correcta")
        print(f"ID: {nuevo_pedido.id}")
        print(f"Cliente: {cliente}")
        print(f"Maquina: {maquina.descripcion}")
        print(f"Estado: {nuevo_pedido.estado}")
        print(f"Precio: USD {nuevo_pedido.precio}")
        print(f"Fecha de recepción: {nuevo_pedido.fecha_recibimiento.strftime('%Y-%m-%d %H:%M:%S')}")
        
    def listar_piezas(self):
        if not self.piezas:
            print("No hay piezas registradas.")
            return None
        print("\nListado de piezas:")
        print(f"{'Código':<6} {'Descripción':<20} {'Stock':<8} {'Tamaño lote':<12} {'Costo':<8}")
        for pieza in self.piezas:
            print(f"{pieza.codigo:<6} {pieza.descripcion:<20} {pieza.cantidad_disponible:<8} {pieza.tamanio_lote:<12} {pieza.costo:<8.2f}")

    def listar_maquinas(self):
        if not self.maquinas:
            print("No hay máquinas registradas.")
            return None
        print("\nListado de máquinas:")
        print(f"{'Código':<6} {'Descripción':<20} {'Costo prod.':<12} {'Disponible':<10}")
        for maquina in self.maquinas:
            disponible = "Sí" if maquina.stock > 0 else "No"
            print(f"{maquina.codigo:<6} {maquina.descripcion:<20} {maquina.costo_produccion():<12.2f} {disponible:<10}")   