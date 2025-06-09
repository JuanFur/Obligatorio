from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Clientes import ClienteParticular, Empresa
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from Exeptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste
from Exeptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste
from Exeptions.ExceptionValorInvalido import ExceptionValorInvalido
from entities.Pedido import Pedido
from entities.Reposicion import Reposicion

class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []

    # ----------- PIEZAS -----------
    def descripcion_ya_existe(self, descripcion):
        for pieza in self.piezas:
            if pieza.descripcion.lower() == descripcion.lower():
                return True
        return False

    def registrar_pieza(self):
        while True:
            descripcion = input("Descripción: ").strip()
            if not descripcion:
                print("La descripción no puede estar vacía. Intente nuevamente.")
            elif self.descripcion_ya_existe(descripcion):
                print(f"Ya existe una pieza con la descripción: {descripcion}")
            else:
                break

        while True:
            try:
                costo = float(input("Costo por unidad: "))
                if costo <= 0:
                    raise ExceptionValorInvalido("Costo por unidad")
                break
            except ValueError:
                print("Debe ingresar un número válido para el costo.")
            except ExceptionValorInvalido as e:
                print(e)

        while True:
            try:
                tamanio_lote = int(input("Tamaño del lote: "))
                if tamanio_lote <= 0:
                    raise ExceptionValorInvalido("Tamaño del lote")
                break
            except ValueError:
                print("Debe ingresar un número entero para el tamaño del lote.")
            except ExceptionValorInvalido as e:
                print(e)

        while True:
            try:
                cantidad = int(input("Cantidad disponible: "))
                if cantidad < 0:
                    raise ExceptionValorInvalido("Cantidad disponible")
                break
            except ValueError:
                print("Debe ingresar un número entero para la cantidad disponible.")
            except ExceptionValorInvalido as e:
                print(e)

        nueva_pieza = Pieza(descripcion, costo, tamanio_lote, cantidad)
        self.piezas.append(nueva_pieza)
        print(f"Pieza registrada ({nueva_pieza.codigo}).")
        self.actualizar_pedidos_pendientes()

    # ----------- MAQUINAS -----------
    def registrar_maquina(self):
        if not self.piezas:
            print("Debe registrar al menos una pieza antes de registrar una máquina.")
            return

        while True:
            descripcion = input("Descripción de la máquina: ").strip()
            if descripcion.lower() == "cancelar":
                print("Registro de máquina cancelado.")
                return
            if not descripcion:
                print("La descripción debe contener caracteres. Inténtelo de nuevo.")
            else:
                existe = False
                for m in self.maquinas:
                    if m.descripcion.lower() == descripcion.lower():
                        existe = True
                        break
                if existe:
                    print(f"Ya existe una máquina con la descripción: {descripcion}")
                else:
                    break

        nueva_maquina = Maquina(descripcion)
        piezas_agregadas = []

        while True:
            piezas_disponibles = [pieza for pieza in self.piezas if pieza.codigo not in piezas_agregadas]
            if not piezas_disponibles:
                print("No hay más piezas disponibles para agregar.")
                break

            print("Piezas disponibles:")
            for pieza in piezas_disponibles:
                print(f"{pieza.codigo}: {pieza.descripcion} (Stock: {pieza.cantidad_disponible})")

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
                    continue
            except ValueError:
                print("Código inválido. Debe ingresar un número.")
                continue

            while True:
                cantidad_input = input(f"Cantidad necesaria de '{pieza_seleccionada.descripcion}' (o 'cancelar' para volver): ")
                if cantidad_input.strip().lower() == "cancelar":
                    print("Registro de máquina cancelado.")
                    return
                try:
                    cantidad = int(cantidad_input)
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a 0.")
                    else:
                        break
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

    # ----------- CLIENTES -----------
    def registrar_cliente(self):
        while True:
            tipo = input("Seleccionar tipo cliente:\n1 Particular\n2 Empresa\n>").strip()
            if tipo == "1" or tipo == "2":
                break
            print("Tipo cliente no disponible. Ingrese 1 o 2.")

        cliente = None

        if tipo == "1":
            # Cliente Particular
            while True:
                nombre = input("Ingrese nombre completo (solo letras y espacios): ").strip()
                solo_letras = True
                for c in nombre:
                    if not ((c >= "A" and c <= "Z") or (c >= "a" and c <= "z") or c == " "):
                        solo_letras = False
                        break
                if solo_letras and nombre != "":
                    break
                print("El nombre debe contener solo letras y espacios.")

            while True:
                cedula = input("Ingrese cédula (8 dígitos, sin guiones): ").strip()
                es_numero = True
                if len(cedula) == 8:
                    for c in cedula:
                        if not (c >= "0" and c <= "9"):
                            es_numero = False
                            break
                else:
                    es_numero = False
                cedula_duplicada = False
                for cli in self.clientes:
                    if "cedula" in cli.__dict__:
                        if cli.cedula == cedula:
                            cedula_duplicada = True
                            break
                if es_numero:
                    if cedula_duplicada:
                        print("La cédula ya está registrada en el sistema.")
                    else:
                        break
                else:
                    print("La cédula debe tener exactamente 8 dígitos numéricos, sin guiones.")

            while True:
                telefono = input("Ingrese teléfono (9 dígitos): ").strip()
                es_numero = True
                if len(telefono) == 9:
                    for c in telefono:
                        if not (c >= "0" and c <= "9"):
                            es_numero = False
                            break
                else:
                    es_numero = False
                if es_numero:
                    break
                print("El teléfono debe tener exactamente 9 dígitos numéricos.")

            while True:
                correo = input("Ingrese correo electrónico: ").strip()
                tiene_arroba = False
                tiene_letra = False
                for c in correo:
                    if c == "@":
                        tiene_arroba = True
                    if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"):
                        tiene_letra = True
                if tiene_arroba and tiene_letra:
                    break
                print("Correo electrónico inválido. Debe contener letras y un '@'.")

            cliente = ClienteParticular(nombre, cedula, telefono, correo)

        elif tipo == "2":
            # Empresa
            while True:
                rut = input("Ingrese RUT (12 dígitos, sin guiones): ").strip()
                es_numero = True
                if len(rut) == 12:
                    for c in rut:
                        if not (c >= "0" and c <= "9"):
                            es_numero = False
                            break
                else:
                    es_numero = False
                rut_duplicado = False
                for cli in self.clientes:
                    if "rut" in cli.__dict__:
                        if cli.rut == rut:
                            rut_duplicado = True
                            break
                if es_numero:
                    if rut_duplicado:
                        print("El RUT ya está registrado en el sistema.")
                    else:
                        break
                else:
                    print("El RUT debe tener exactamente 12 dígitos numéricos, sin guiones.")

            while True:
                nombre = input("Ingrese nombre de la empresa (solo letras y espacios): ").strip()
                solo_letras = True
                for c in nombre:
                    if not ((c >= "A" and c <= "Z") or (c >= "a" and c <= "z") or c == " "):
                        solo_letras = False
                        break
                if solo_letras and nombre != "":
                    break
                print("El nombre debe contener solo letras y espacios.")

            while True:
                pagina = input("Ingrese página web (sin espacios): ").strip()
                tiene_espacio = False
                for c in pagina:
                    if c == " ":
                        tiene_espacio = True
                        break
                if pagina != "" and not tiene_espacio:
                    break
                print("Página web inválida. No debe contener espacios.")

            while True:
                telefono = input("Ingrese teléfono de contacto (9 dígitos): ").strip()
                es_numero = True
                if len(telefono) == 9:
                    for c in telefono:
                        if not (c >= "0" and c <= "9"):
                            es_numero = False
                            break
                else:
                    es_numero = False
                if es_numero:
                    break
                print("El teléfono debe tener exactamente 9 dígitos numéricos.")

            while True:
                correo = input("Ingrese correo electrónico de contacto: ").strip()
                tiene_arroba = False
                tiene_letra = False
                for c in correo:
                    if c == "@":
                        tiene_arroba = True
                    if (c >= "A" and c <= "Z") or (c >= "a" and c <= "z"):
                        tiene_letra = True
                if tiene_arroba and tiene_letra:
                    break
                print("Correo electrónico inválido. Debe contener letras y un '@'.")

            cliente = Empresa(rut, nombre, pagina, telefono, correo)

        if cliente:
            self.clientes.append(cliente)
            print("\nCliente registrado:")
            print(cliente)
            return cliente

    # ----------- REPOSICION -----------
    def registrar_reposicion(self):
        if not self.piezas:
            print("No hay piezas registradas para reponer.")
            return

        print("\nPiezas disponibles para reponer:")
        for pieza in self.piezas:
            print(f"{pieza.codigo}: {pieza.descripcion} (Stock: {pieza.cantidad_disponible}, Tamaño lote: {pieza.tamanio_lote})")

        while True:
            codigo_input = input("Ingrese el código de la pieza a reponer (o 'Cancelar' para volver): ").strip()
            if codigo_input.lower() == "cancelar":
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
            if lotes_input.lower() == "cancelar":
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
        self.actualizar_pedidos_pendientes()

    # ----------- PEDIDOS -----------
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
            try:
                opcion_cliente = int(input("\nSeleccione el número del cliente: ")) - 1
                if 0 <= opcion_cliente < len(self.clientes):
                    cliente = self.clientes[opcion_cliente]
                    break
                else:
                    print("Número de cliente inválido. Intente nuevamente")
            except ValueError:
                print("Debe ingresar un número válido.")

        print("\nMaquinas disponibles: ")
        for i, maquina in enumerate(self.maquinas, 1):
            print(f"{i} - {maquina}")

        while True:
            try:
                opcion_maquina = int(input("\nSeleccione el número de la maquina: ")) - 1
                if 0 <= opcion_maquina < len(self.maquinas):
                    maquina = self.maquinas[opcion_maquina]
                    break
                else:
                    print("Número de máquina inválido. Intente nuevamente")
            except ValueError:
                print("Debe ingresar un número válido.")

        nuevo_pedido = Pedido(cliente, maquina)
        self.pedidos.append(nuevo_pedido)
        print("\nPedido registrado de forma correcta")
        print(f"ID: {nuevo_pedido.id}")
        print(f"Cliente: {cliente}")
        print(f"Maquina: {maquina.descripcion}")
        print(f"Estado: {nuevo_pedido.estado}")
        print(f"Precio: USD {nuevo_pedido.precio}")
        print(f"Fecha de recepción: {nuevo_pedido.fecha_recibimiento.strftime('%Y-%m-%d %H:%M:%S')}")
        self.actualizar_pedidos_pendientes()

    # ----------- ACTUALIZAR PEDIDOS PENDIENTES -----------
    def actualizar_pedidos_pendientes(self):
        for pedido in self.pedidos:
            if "estado" in pedido.__dict__ and pedido.estado == "pendiente":
                maquina = pedido.maquina
                puede_entregar = True
                # Verificar si hay stock suficiente para todos los requerimientos
                for req in maquina.requerimientos:
                    pieza = req.pieza
                    if pieza.cantidad_disponible < req.cantidad:
                        puede_entregar = False
                        break
                if puede_entregar:
                    # Descontar stock y marcar como entregado
                    for req in maquina.requerimientos:
                        req.pieza.cantidad_disponible -= req.cantidad
                    pedido.estado = "entregado"
                    from datetime import datetime
                    pedido.fecha_entrega = datetime.now()

    # ----------- LISTADOS -----------
    def listar_piezas(self):
        if not self.piezas:
            print("No hay piezas registradas.")
            return None
        print("\nListado de piezas:")
        print(f"{'Código':<6} {'Descripción':<20} {'Stock disponible':<16} {'Tamaño lote':<12} {'Costo en $':<10} {'Faltante para pedidos':<22} {'Lotes recomendados':<18}")
        for pieza in self.piezas:
            faltante = 0
            for pedido in self.pedidos:
                if "estado" in pedido.__dict__ and pedido.estado == "pendiente":
                    if "maquina" in pedido.__dict__:
                        maquina = pedido.maquina
                        if "requerimientos" in maquina.__dict__:
                            for req in maquina.requerimientos:
                                if "pieza" in req.__dict__ and "codigo" in req.pieza.__dict__:
                                    if req.pieza.codigo == pieza.codigo:
                                        cantidad_necesaria = req.cantidad
                                        if pieza.cantidad_disponible < cantidad_necesaria:
                                            faltante += (cantidad_necesaria - pieza.cantidad_disponible)
            if faltante > 0:
                lotes_recomendados = (faltante + pieza.tamanio_lote - 1) // pieza.tamanio_lote
            else:
                lotes_recomendados = 0
            print(f"{pieza.codigo:<6} {pieza.descripcion:<20} {pieza.cantidad_disponible:<16} {pieza.tamanio_lote:<12} {pieza.costo:<10.2f} {faltante:<22} {lotes_recomendados:<18}")

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
            nombre = "-"
            if "nombre_completo" in cliente.__dict__:
                nombre = cliente.nombre_completo
            elif "nombre" in cliente.__dict__:
                nombre = cliente.nombre
            tipo = cliente.__dict__.get("tipo", "-")
            telefono = cliente.__dict__.get("telefono", "-")
            id_cliente = cliente.__dict__.get("id", "-")
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
                if "estado" in pedido.__dict__ and pedido.estado == "pendiente":
                    pedidos_filtrados.append(pedido)
        elif opcion == "2":
            for pedido in self.pedidos:
                if "estado" in pedido.__dict__ and pedido.estado == "entregado":
                    pedidos_filtrados.append(pedido)
        else:
            pedidos_filtrados = self.pedidos

        if not pedidos_filtrados:
            print("No hay pedidos para mostrar con ese filtro.")
            return

        print("\nListado de pedidos:")
        print(f"{'ID':<5} {'Cliente':<30} {'Máquina':<20} {'Estado':<15} {'Precio':<10} {'Fecha recepción':<20}")
        for pedido in pedidos_filtrados:
            nombre_cliente = "-"
            if "nombre_completo" in pedido.cliente.__dict__:
                nombre_cliente = pedido.cliente.nombre_completo
            elif "nombre" in pedido.cliente.__dict__:
                nombre_cliente = pedido.cliente.nombre
            print(f"{pedido.id:<5} {nombre_cliente:<30} {pedido.maquina.descripcion:<20} {pedido.estado:<15} {pedido.precio:<10.2f} {pedido.fecha_recibimiento.strftime('%Y-%m-%d %H:%M:%S'):<20}")

    def listar_contabilidad(self):
        pedidos_entregados = []
        for p in self.pedidos:
            if "estado" in p.__dict__ and p.estado == "entregado":
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