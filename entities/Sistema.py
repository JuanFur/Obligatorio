from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Clientes import ClienteParticular, Empresa
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from Exeptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste
from entities.Pedido import Pedido
from Exeptions.ExceptionValorInvalido import ExceptionValorInvalido
from entities.Reposicion import Reposicion
from entities.Reposicion import Reposicion


# Agregar import o definición de la excepción y funciones de validación
class ExceptionClienteYaExiste(Exception):
    pass

def nombre_valido(nombre):
    if not nombre or not nombre.strip():
        raise ExceptionClienteYaExiste("El nombre no puede estar vacío.")
    # Aquí puedes agregar más validaciones si es necesario

def cedula_valida(cedula):
    if not cedula or not cedula.strip():
        raise ExceptionClienteYaExiste("La cédula no puede estar vacía.")
    # Aquí puedes agregar más validaciones si es necesario

def telefono_valido(telefono):
    if not telefono or not telefono.strip():
        raise ExceptionClienteYaExiste("El teléfono no puede estar vacío.")
    # Aquí puedes agregar más validaciones si es necesario

def rut_valido(rut):
    if not rut or not rut.strip():
        raise ExceptionClienteYaExiste("El RUT no puede estar vacío.")
    # Aquí puedes agregar más validaciones si es necesario

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
        self.pedidos = []
        self.reposiciones = []        

    def registrar_pieza(self):
        descripcion = input("Descripción: ").strip()
        while not descripcion or self.descripcion_ya_existe(descripcion):
            if not descripcion:
                print("La descripción no puede estar vacía. Intente nuevamente.")
            elif self.descripcion_ya_existe(descripcion):
                print(f"Ya existe una pieza con la descripción: {descripcion}")
            descripcion = input("Descripción: ").strip()
            
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
                tamanio_lote = int(input("Tamaño del lote: "))
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
                cantidad = int(input("Cantidad disponible: "))
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
        if not self.piezas:
            print("Debe registrar al menos una pieza antes de registrar una máquina.")
            return

        descripcion = input("Descripción de la máquina: ")
        if descripcion.strip().lower() == "cancelar":
            print("Registro de máquina cancelado.")
            return
        while descripcion.strip() == "":
            descripcion = input("La descripción debe contener caracteres. Inténtelo de nuevo: ")
            if descripcion.strip().lower() == "cancelar":
                print("Registro de máquina cancelado.")
                return

        for i in self.maquinas:
            if i.descripcion == descripcion:
                print(f"Ya existe una máquina con la descripción: {descripcion}")
                return

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

            # Solicitar código de pieza hasta que sea válido o se cancele
            codigo_valido = False
            while not codigo_valido:
                codigo_pieza = input("Ingrese el código de la pieza a agregar (o 'No' para terminar, 'cancelar' para volver): ").strip()
                if codigo_pieza.lower() == "cancelar":
                    print("Registro de máquina cancelado.")
                    return
                if codigo_pieza.lower() == "no":
                    break
                try:
                    codigo_pieza_int = int(codigo_pieza)
                    pieza_seleccionada = None
                    for p in piezas_disponibles:
                        if p.codigo == codigo_pieza_int:
                            pieza_seleccionada = p
                            break
                    if pieza_seleccionada is None:
                        print("Pieza no encontrada o ya agregada.")
                    else:
                        codigo_valido = True
                except ValueError:
                    print("Código inválido. Debe ingresar un número.")
            if codigo_pieza.lower() == "no":
                break

            # Solicitar cantidad necesaria
            cantidad_valida = False
            while not cantidad_valida:
                cantidad_input = input(f"Cantidad necesaria de '{pieza_seleccionada.descripcion}' (o 'cancelar' para volver): ")
                if cantidad_input.strip().lower() == "cancelar":
                    print("Registro de máquina cancelado.")
                    return
                try:
                    cantidad = int(cantidad_input)
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0.")
                    else:
                        cantidad_valida = True
                except ValueError:
                    print("Debe ingresar un número entero válido para la cantidad necesaria.")

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
            cliente = None
            if tipo == "1":
                while True:
                    nombre = input("Ingrese nombre completo: ")
                    try:
                        nombre_valido(nombre)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                while True:
                    cedula = input("Ingrese cédula: ")
                    try:
                        cedula_valida(cedula)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                while True:
                    telefono = input("Ingrese teléfono: ")
                    try:
                        telefono_valido(telefono)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                    correo = input("Ingrese correo electrónico: ")
                    cliente = ClienteParticular(nombre, cedula, telefono, correo)
            elif tipo == "2":
                while True:
                    rut = input("Ingrese RUT: ")
                    try:
                        rut_valido(rut)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                while True:
                    nombre = input("Ingrese nombre de la empresa: ")
                    try:
                        nombre_valido(nombre)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                pagina = input("Ingrese página web: ")
                while True:
                    telefono = input("Ingrese teléfono de contacto: ")
                    try:
                        telefono_valido(telefono)
                        break
                    except ExceptionClienteYaExiste as e:
                        print(e)
                
                correo = input("Ingrese correo electrónico de contacto: ")
                cliente = Empresa(rut, nombre, pagina, telefono, correo)
            else:
                print ("Tipo cliente no disponible")
                return None
            
            if cliente:
                self.clientes.append(cliente)
                print("\nCliente registrado:")
                print(cliente)
                return cliente
        
    def registrar_reposicion(self):
            if not self.piezas:
                print("No hay piezas registradas para reponer.")
                return

            print("\nPiezas disponibles para reponer:")
            for pieza in self.piezas:
                print(f"{pieza.codigo}: {pieza.descripcion} (Stock: {pieza.cantidad_disponible}, Tamaño lote: {pieza.tamanio_lote})")

            while True:
                codigo_input = input("Ingrese el código de la pieza a reponer (o 'Cancelar' para volver): ").strip()
                if codigo_input == "Cancelar":
                    print("Registro de reposición cancelado.")
                    return
                try:
                    codigo = int(codigo_input)
                except ValueError:
                    print("Debe ingresar un número de código válido.")
                    continue

                pieza_seleccionada = None
                for pieza in self.piezas:
                    if pieza.codigo == codigo:
                        pieza_seleccionada = pieza
                        break

                if pieza_seleccionada is None:
                    print("Código de pieza no encontrado.")
                    continue
                break

            while True:
                lotes_input = input(f"Ingrese la cantidad de lotes a comprar para '{pieza_seleccionada.descripcion}' (o 'Cancelar' para volver): ").strip()
                if lotes_input == "Cancelar":
                    print("Registro de reposición cancelado.")
                    return
                try:
                    cantidad_lotes = int(lotes_input)
                    if cantidad_lotes <= 0:
                        print("La cantidad de lotes debe ser mayor a 0.")
                        continue
                except ValueError:
                    print("Debe ingresar un número entero válido para la cantidad de lotes.")
                    continue
                break

            reposicion = Reposicion(pieza_seleccionada, cantidad_lotes)
            self.reposiciones.append(reposicion)



            print(f"\nReposición registrada correctamente.")
            print(f"Pieza: {pieza_seleccionada.descripcion}")
            print(f"Cantidad total repuesta: {reposicion.cantidad_total}")
            print(f"Nuevo stock: {pieza_seleccionada.cantidad_disponible}")
            print(f"Costo total de la reposición: USD {reposicion.costo_total:.2f}")
            print(f"Fecha de reposición: {reposicion.fecha.strftime('%Y-%m-%d %H:%M:%S')}")

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
            print(f"{i} - {maquina}")    
        
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

    def listar_clientes(self):
        if not self.clientes:
            print("\nNo hay clientes registrados.")
            return
        print("\nLista de clientes") 
        print(f"{'ID':<5} {'Nombre':<30} {'Tipo':<15} {'Contacto':<20}")
        for cliente in self.clientes:
            try:
                nombre = cliente.nombre_completo
            except AttributeError:
                try:
                    nombre = cliente.nombre
                except AttributeError:
                    nombre = "-"
            try:
                tipo = cliente.tipo
            except AttributeError:
                tipo = "-"
            try:
                telefono = cliente.telefono
            except AttributeError:
                telefono = "-"
            try:
                id_cliente = cliente.id
            except AttributeError:
                id_cliente = "-"
            print(f"{id_cliente:<5} {nombre:<30} {tipo:<15} {telefono:<20}")
    
    def listar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos registrados.")
            return None

        print("\n¿Desea filtrar los pedidos por estado?")
        print("1. Pendientes")
        print("2. Entregados")
        print("3. No filtrar (mostrar todos)")
        opcion = input("Seleccione una opción: ").strip()

        pedidos_filtrados = []
        if opcion == "1":
            for pedido in self.pedidos:
                if hasattr(pedido, "estado") and pedido.estado.lower() == "pendiente":
                    pedidos_filtrados.append(pedido)
        elif opcion == "2":
            for pedido in self.pedidos:
                if hasattr(pedido, "estado") and pedido.estado.lower() == "entregado":
                    pedidos_filtrados.append(pedido)
        else:
            pedidos_filtrados = self.pedidos

        if not pedidos_filtrados:
            print("No hay pedidos para mostrar con ese filtro.")
            return

        print("\nListado de pedidos:")
        print(f"{'ID':<5} {'Cliente':<30} {'Máquina':<20} {'Estado':<15} {'Precio':<10} {'Fecha recepción':<20}")
        for pedido in pedidos_filtrados:
            try:
                nombre_cliente = pedido.cliente.nombre_completo
            except AttributeError:
                try:
                    nombre_cliente = pedido.cliente.nombre
                except AttributeError:
                    nombre_cliente = "-"
            print(f"{pedido.id:<5} {nombre_cliente:<30} {pedido.maquina.descripcion:<20} {pedido.estado:<15} {pedido.precio:<10.2f} {pedido.fecha_recibimiento.strftime('%Y-%m-%d %H:%M:%S'):<20}")

    def listar_contabilidad(self):
        pedidos_entregados = []
        for p in self.pedidos:
            if hasattr(p, "estado") and p.estado.lower() == "entregado":
                pedidos_entregados.append(p)

        if not pedidos_entregados:
            print("No hay pedidos entregados para mostrar contabilidad.")
            return

        costo_total = 0
        ingreso_total = 0

        for pedido in pedidos_entregados:
            costo_total += pedido.maquina.costo_produccion()
            ingreso_total += pedido.precio

        ganancia = ingreso_total - costo_total
        impuesto = ganancia * 0.25
        ganancia_final = ganancia - impuesto

        print("\n--- Contabilidad ---")
        print(f"Costo total de producción: USD {costo_total:.2f}")
        print(f"Ingreso total por ventas: USD {ingreso_total:.2f}")
        print(f"Ganancia bruta: USD {ganancia:.2f}")
        print(f"Impuesto a la ganancia (25% IRAE): USD {impuesto:.2f}")
        print(f"Ganancia final (después de impuestos): USD {ganancia_final:.2f}")

    def descripcion_ya_existe(self, descripcion):
        for pieza in self.piezas:
            if pieza.descripcion == descripcion:
                return True
        return False
