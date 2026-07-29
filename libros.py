from clases import Libro

def menu_libros():
    while True:
        print("\n--- MÓDULO DE LIBROS ---")
        print("1. Registrar libro")
        print("2. Consultar libros")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                codigo = input("Código: ").strip()
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                categoria = input("Categoría: ").strip()
                cantidad = int(input("Cantidad disponible: "))

                if not codigo or not titulo or not autor or not categoria:
                    print("Error: Todos los campos son obligatorios.")
                elif cantidad < 0:
                    print("Error: La cantidad no puede ser negativa.")
                else:
                    libro = Libro(codigo, titulo, autor, categoria, cantidad)
                    # Aquí tu compañera conecta la inserción a la BD:
                    # registrar_libro_bd(libro)
                    print(f"Libro '{titulo}' registrado exitosamente.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido para la cantidad.")

        elif opcion == "2":
            print("\n-- Consulta de Libros --")
            # Aquí tu compañera conecta la consulta SELECT a la BD
            
        elif opcion == "3":
            print("\n-- Modificar Libro --")
            # Lógica de modificación vinculada a la BD

        elif opcion == "4":
            print("\n-- Eliminar Libro --")
            # Lógica de eliminación vinculada a la BD

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")