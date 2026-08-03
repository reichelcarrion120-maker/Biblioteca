import sqlite3
from maker_conexion import conectar

def registrar_usuario():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            identificacion = input("Identificación: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()
            telefono = input("Teléfono: ").strip()

            cursor.execute("""
                INSERT INTO Usuarios (identificacion, nombre, correo, telefono)
                VALUES (?, ?, ?, ?)
            """, (identificacion, nombre, correo, telefono))

            conexion.commit()
            print("Usuario guardado en la base de datos correctamente.")
        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            conexion.close()

def consultar_usuarios():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT identificacion, nombre, correo, telefono FROM Usuarios")
            usuarios = cursor.fetchall()

            print("\n----- LISTA DE USUARIOS -----")
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for u in usuarios:
                    print(f"Identificación: {u[0]} | Nombre: {u[1]} | Correo: {u[2]} | Teléfono: {u[3]}")
                print("-----------------------------")
        except Exception as e:
            print("Ocurrió un error:", e)
        finally:
            conexion.close()

def modificar_usuario():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            identificacion = input("Ingrese la identificación del usuario a modificar: ").strip()

            cursor.execute("SELECT id_usuario, nombre, correo, telefono FROM Usuarios WHERE identificacion = ?", (identificacion,))
            usuario = cursor.fetchone()

            if not usuario:
                print("Error: No se encontró ningún usuario con esa identificación.")
                return

            print(f"\nModificando usuario: {usuario[1]}")
            nuevo_nombre = input(f"Nuevo nombre (presione Enter para mantener '{usuario[1]}'): ").strip()
            nuevo_correo = input(f"Nuevo correo (presione Enter para mantener '{usuario[2]}'): ").strip()
            nuevo_tel = input(f"Nuevo teléfono (presione Enter para mantener '{usuario[3]}'): ").strip()

            nombre = nuevo_nombre if nuevo_nombre else usuario[1]
            correo = nuevo_correo if nuevo_correo else usuario[2]
            telefono = nuevo_tel if nuevo_tel else usuario[3]

            cursor.execute("""
                UPDATE Usuarios 
                SET nombre = ?, correo = ?, telefono = ?
                WHERE identificacion = ?
            """, (nombre, correo, telefono, identificacion))

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
            identificacion = input("Ingrese la identificación del usuario a eliminar: ").strip()

            cursor.execute("SELECT id_usuario, nombre FROM Usuarios WHERE identificacion = ?", (identificacion,))
            usuario = cursor.fetchone()

            if not usuario:
                print("Error: No se encontró ningún usuario con esa identificación.")
                return

            confirmar = input(f"¿Está seguro de eliminar a '{usuario[1]}'? (s/n): ").strip().lower()
            if confirmar == 's':
                cursor.execute("DELETE FROM Usuarios WHERE identificacion = ?", (identificacion,))
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