import sqlite3
from maker_conexion import conectar


def registrar_usuario():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Validación: Identificación (solo números y no vacía)
            while True:
                identificacion = input(
                    "Identificación (solo números): "
                ).strip()
                if identificacion.isdigit():
                    break
                print("Error: La identificación debe contener solo números.")

            # Validación: Nombre no vacío
            while True:
                nombre = input("Nombre completo: ").strip()
                if nombre:
                    break
                print("Error: El nombre no puede estar vacío.")

            correo = input("Correo electrónico: ").strip()

            # Validación: Teléfono (solo números y no vacío)
            while True:
                telefono = input("Teléfono (solo números): ").strip()
                if telefono.isdigit():
                    break
                print("Error: El teléfono debe contener solo números.")

            cursor.execute(
                """
                INSERT INTO Usuarios (identificacion, nombre, correo, telefono)
                VALUES (?, ?, ?, ?)
            """,
                (identificacion, nombre, correo, telefono),
            )

            conexion.commit()
            print("Usuario guardado en la base de datos correctamente.")
        except sqlite3.IntegrityError:
            print(
                "Error: Ya existe un usuario registrado con esa identificación."
            )
        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            conexion.close()


def consultar_usuarios():
    """Cumple el Punto 6 del profesor: Ver todos y buscar por identificación o nombre"""
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            print("\n--- CONSULTAR USUARIOS ---")
            print("1. Ver lista general de usuarios")
            print("2. Buscar usuario por identificación o nombre")
            sub_opcion = input("Seleccione una opción: ").strip()

            if sub_opcion == "1":
                cursor.execute(
                    "SELECT identificacion, nombre, correo, telefono FROM Usuarios"
                )
                usuarios = cursor.fetchall()
            elif sub_opcion == "2":
                busqueda = input(
                    "Ingrese el nombre o la identificación a buscar: "
                ).strip()
                cursor.execute(
                    """
                    SELECT identificacion, nombre, correo, telefono FROM Usuarios
                    WHERE identificacion LIKE ? OR nombre LIKE ?
                """,
                    (f"%{busqueda}%", f"%{busqueda}%"),
                )
                usuarios = cursor.fetchall()
            else:
                print("Opción no válida.")
                return

            print("\n----- RESULTADOS -----")
            if not usuarios:
                print("No se encontraron usuarios.")
            else:
                for u in usuarios:
                    print(
                        f"Identificación: {u[0]} | Nombre: {u[1]} | Correo: {u[2]} | Teléfono: {u[3]}"
                    )
                print("----------------------")
        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            conexion.close()


def modificar_usuario():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            while True:
                identificacion = input(
                    "Ingrese la identificación del usuario a modificar: "
                ).strip()
                if identificacion.isdigit():
                    break
                print("Error: Ingrese una identificación válida (solo números).")

            cursor.execute(
                "SELECT id_usuario, nombre, correo, telefono FROM Usuarios WHERE identificacion = ?",
                (identificacion,),
            )
            usuario = cursor.fetchone()

            if not usuario:
                print(
                    "Error: No se encontró ningún usuario con esa identificación."
                )
                return

            print(f"\nModificando usuario: {usuario[1]}")
            nuevo_nombre = input(
                f"Nuevo nombre (presione Enter para mantener '{usuario[1]}'): "
            ).strip()
            nuevo_correo = input(
                f"Nuevo correo (presione Enter para mantener '{usuario[2]}'): "
            ).strip()

            while True:
                nuevo_tel = input(
                    f"Nuevo teléfono (presione Enter para mantener '{usuario[3]}'): "
                ).strip()
                if not nuevo_tel or nuevo_tel.isdigit():
                    break
                print("Error: El teléfono solo debe contener números.")

            nombre = nuevo_nombre if nuevo_nombre else usuario[1]
            correo = nuevo_correo if nuevo_correo else usuario[2]
            telefono = nuevo_tel if nuevo_tel else usuario[3]

            cursor.execute(
                """
                UPDATE Usuarios 
                SET nombre = ?, correo = ?, telefono = ?
                WHERE identificacion = ?
            """,
                (nombre, correo, telefono, identificacion),
            )

            conexion.commit()
            print("\nUsuario actualizado con éxito.")

        except Exception as e:
            print("Ocurrió un error al modificar el usuario:", e)
        finally:
            conexion.close()


def eliminar_usuario():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            while True:
                identificacion = input(
                    "Ingrese la identificación del usuario a eliminar: "
                ).strip()
                if identificacion.isdigit():
                    break
                print("Error: Ingrese una identificación válida (solo números).")

            cursor.execute(
                "SELECT id_usuario, nombre FROM Usuarios WHERE identificacion = ?",
                (identificacion,),
            )
            usuario = cursor.fetchone()

            if not usuario:
                print(
                    "Error: No se encontró ningún usuario con esa identificación."
                )
                return

            confirmar = (
                input(f"¿Está seguro de eliminar a '{usuario[1]}'? (s/n): ")
                .strip()
                .lower()
            )
            if confirmar == "s":
                cursor.execute(
                    "DELETE FROM Usuarios WHERE identificacion = ?",
                    (identificacion,),
                )
                conexion.commit()
                print("\nUsuario eliminado con éxito.")
            else:
                print("\nOperación cancelada.")

        except Exception as e:
            print("Ocurrió un error al eliminar el usuario:", e)
        finally:
            conexion.close()


def menu_usuarios():
    while True:
        print("\n--- MÓDULO DE USUARIOS ---")
        print("1. Registrar usuario")
        print("2. Consultar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            consultar_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")