from clases import Usuario

def menu_usuarios():
    while True:
        print("\n--- MÓDULO DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Consultar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                identificacion = input("Identificación: ").strip()
                nombre = input("Nombre completo: ").strip()
                correo = input("Correo electrónico: ").strip()
                telefono = input("Teléfono: ").strip()

                if not identificacion or not nombre or not correo or not telefono:
                    print("Error: Todos los campos son obligatorios.")
                else:
                    usuario = Usuario(identificacion, nombre, correo, telefono)
                    # Aquí tu compañera conecta la inserción a la BD:
                    # registrar_usuario_bd(usuario)
                    print(f"Usuario '{nombre}' registrado exitosamente.")
            except Exception as e:
                print(f"Ocurrió un error al registrar: {e}")

        elif opcion == "2":
            print("\n-- Consulta de Usuarios --")
            # Aquí tu compañera conecta la consulta SELECT a la BD

        elif opcion == "3":
            print("\n-- Modificar Usuario --")
            # Lógica de modificación vinculada a la BD

        elif opcion == "4":
            print("\n-- Eliminar Usuario --")
            # Lógica de eliminación vinculada a la BD

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")