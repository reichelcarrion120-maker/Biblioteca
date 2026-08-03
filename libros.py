import sqlite3
from maker_conexion import conectar

def registrar_libro():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            codigo = input("Código: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            categoria = input("Categoría: ").strip()
            cantidad = int(input("Cantidad disponible: "))

            cursor.execute("""
                INSERT INTO libros (codigo, titulo, autor, categoria, cantidad)
                VALUES (?, ?, ?, ?, ?)
            """, (codigo, titulo, autor, categoria, cantidad))

            conexion.commit()
            print(f"\nLibro '{titulo}' registrado correctamente.")
        except Exception as e:
            print("Ocurrió un error al registrar el libro:", e)
        finally:
            conexion.close()

def consultar_libros():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo, titulo, autor, categoria, cantidad FROM libros")
            libros = cursor.fetchall()

            print("\n----- LISTA DE LIBROS -----")
            if not libros:
                print("No hay libros registrados.")
            else:
                for l in libros:
                    print(f"Código: {l[0]}")
                    print(f"Título: {l[1]}")
                    print(f"Autor: {l[2]}")
                    print(f"Categoría: {l[3]}")
                    print(f"Cantidad: {l[4]}")
                    print("--------------------------------")
        except Exception as e:
            print("Ocurrió un error al consultar libros:", e)
        finally:
            conexion.close()

def modificar_libro():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            codigo = input("Ingrese el código del libro a modificar: ").strip()

            cursor.execute("SELECT id_libro, titulo, autor, categoria, cantidad FROM libros WHERE codigo = ?", (codigo,))
            libro = cursor.fetchone()

            if not libro:
                print("Error: No se encontró ningún libro con ese código.")
                return

            print(f"\nModificando libro: {libro[1]}")
            nuevo_titulo = input(f"Nuevo título (presione Enter para mantener '{libro[1]}'): ").strip()
            nuevo_autor = input(f"Nuevo autor (presione Enter para mantener '{libro[2]}'): ").strip()
            nueva_cat = input(f"Nueva categoría (presione Enter para mantener '{libro[3]}'): ").strip()
            nueva_cant_input = input(f"Nueva cantidad (presione Enter para mantener '{libro[4]}'): ").strip()

            titulo = nuevo_titulo if nuevo_titulo else libro[1]
            autor = nuevo_autor if nuevo_autor else libro[2]
            categoria = nueva_cat if nueva_cat else libro[3]
            cantidad = int(nueva_cant_input) if nueva_cant_input else libro[4]

            cursor.execute("""
                UPDATE libros 
                SET titulo = ?, autor = ?, categoria = ?, cantidad = ?
                WHERE codigo = ?
            """, (titulo, autor, categoria, cantidad, codigo))

            conexion.commit()
            print("\n¡Libro actualizado con éxito!")

        except Exception as e:
            print("Ocurrió un error al modificar el libro:", e)
        finally:
            conexion.close()

def eliminar_libro():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            codigo = input("Ingrese el código del libro a eliminar: ").strip()

            cursor.execute("SELECT id_libro, titulo FROM libros WHERE codigo = ?", (codigo,))
            libro = cursor.fetchone()

            if not libro:
                print("Error: No se encontró ningún libro con ese código.")
                return

            confirmar = input(f"¿Está seguro de eliminar '{libro[1]}'? (s/n): ").strip().lower()
            if confirmar == 's':
                cursor.execute("DELETE FROM libros WHERE codigo = ?", (codigo,))
                conexion.commit()
                print("\n¡Libro eliminado con éxito!")
            else:
                print("\nOperación cancelada.")

        except Exception as e:
            print("Ocurrió un error al eliminar el libro:", e)
        finally:
            conexion.close()

def menu_libros():
    while True:
        print("\n--- MÓDULO DE LIBROS ---")
        print("1. Registrar libro")
        print("2. Consultar libros")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            consultar_libros()
        elif opcion == "3":
            modificar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")