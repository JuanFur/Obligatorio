from entities.Sistema import Sistema
from Exeptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from Exeptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste

def mostrar_menu_principal():
    print("\n=== Menú Principal ===")
    print("1. Registrar")
    print("2. Listar")
    print("3. Salir del Sistema")

def mostrar_menu_registrar():
    print("\n--- Menú Registrar ---")
    print("1. Pieza")
    print("2. Máquina")
    print("3. Cliente")
    print("4. Pedido")
    print("5. Reposición")
    print("6. Salir")

def mostrar_menu_listar():
    print("\n--- Menú Listar ---")
    print("1. Clientes")
    print("2. Pedidos")
    print("3. Máquinas")
    print("4. Piezas")
    print("5. Contabilidad")
    print("6. Salir")
    
sistema = Sistema() 

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ").strip()

        if opcion_principal == "1":  # Registrar
            while True:
                mostrar_menu_registrar()
                opcion_registrar = input("Seleccione una opción: ").strip()

                if opcion_registrar == "1":
                    try:
                        sistema.registrar_pieza()
                    except ExceptionPiezaYaExiste as e:
                        print(e)
                elif opcion_registrar == "2":
                    try:
                        sistema.registrar_maquina()
                    except ExceptionMaquinaYaExiste as e:
                        print(e)
                elif opcion_registrar == "3":
                    sistema.registrar_cliente()
                elif opcion_registrar == "4":
                    # registrar_pedido()
                    pass
                elif opcion_registrar == "5":
                    # registrar_reposicion()
                    pass
                elif opcion_registrar == "6":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion_principal == "2":  # Listar
            while True:
                mostrar_menu_listar()
                opcion_listar = input("Seleccione una opción: ").strip()

                if opcion_listar == "1":
                    # listar_clientes()
                    pass
                elif opcion_listar == "2":
                    # listar_pedidos()
                    pass
                elif opcion_listar == "3":
                    # listar_maquinas()
                    pass
                elif opcion_listar == "4":
                    # listar_piezas()
                    pass
                elif opcion_listar == "5":
                    # mostrar_contabilidad()
                    pass
                elif opcion_listar == "6":
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif opcion_principal == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main() 