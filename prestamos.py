from clases import Prestamo

def menu_prestamos():
    while True:
        print("\n--- MÓDULO DE PRÉSTAMOS ---")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("3. Consultar préstamos")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_usuario = input("Identificación del usuario: ").strip()
            cod_libro = input("Código del libro: ").strip()
            fecha_p = input("Fecha de préstamo (DD/MM/AAAA): ").strip()
            fecha_d = input("Fecha de devolución (DD/MM/AAAA): ").strip()

            # Lógica a integrar con la BD:
            # 1. Verificar si hay stock (cantidad > 0)
            # 2. Si hay stock: registrar préstamo y REDUCIR stock en 1 (UPDATE libros SET cantidad = cantidad - 1)
            # 3. Si no hay stock: mostrar mensaje "Libro no disponible"
            print("Préstamo registrado correctamente. Stock actualizado.")

        elif opcion == "2":
            id_prestamo = input("Código/ID del préstamo a devolver: ").strip()
            
            # Lógica a integrar con la BD:
            # 1. Marcar préstamo como devuelto (devuelto = True)
            # 2. AUMENTAR stock del libro en 1 (UPDATE libros SET cantidad = cantidad + 1)
            print("Devolución registrada correctamente. Stock actualizado.")

        elif opcion == "3":
            print("\n-- Historial y Consultas de Préstamos --")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")