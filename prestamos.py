import sqlite3
from datetime import datetime, timedelta
from maker_conexion import conectar

def registrar_prestamo():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            identificacion = input("Identificación del usuario: ").strip()
            codigo = input("Código del libro: ").strip()

            # 1. Buscar ID del usuario
            cursor.execute("SELECT id_usuario FROM Usuarios WHERE identificacion = ?", (identificacion,))
            usuario = cursor.fetchone()
            if not usuario:
                print("Error: El usuario no existe.")
                conexion.close()
                return

            # 2. Buscar ID y disponibilidad del libro
            cursor.execute("SELECT id_libro, cantidad FROM libros WHERE codigo = ?", (codigo,))
            libro = cursor.fetchone()
            if not libro:
                print("Error: El libro no existe.")
                conexion.close()
                return
            
            if libro[1] <= 0:
                print("Error: No hay copias disponibles de este libro.")
                conexion.close()
                return

            # 3. Registrar el préstamo
            id_usuario = usuario[0]
            id_libro = libro[0]
            fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
            fecha_devolucion = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO Prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion, devuelto)
                VALUES (?, ?, ?, ?, 0)
            """, (id_usuario, id_libro, fecha_prestamo, fecha_devolucion))

            # 4. Restar 1 al stock del libro
            cursor.execute("UPDATE libros SET cantidad = cantidad - 1 WHERE id_libro = ?", (id_libro,))

            conexion.commit()
            conexion.close()
            print("\n¡Préstamo registrado con éxito!")
            print(f"Fecha límite de devolución: {fecha_devolucion}")

        except Exception as e:
            print("Ocurrió un error:", e)

def consultar_prestamos():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT p.id_prestamo, u.nombre, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.devuelto
                FROM Prestamos p
                JOIN Usuarios u ON p.id_usuario = u.id_usuario
                JOIN libros l ON p.id_libro = l.id_libro
            """)
            prestamos = cursor.fetchall()
            conexion.close()

            print("\n----- LISTA DE PRÉSTAMOS -----")
            if not prestamos:
                print("No hay préstamos registrados actualmente.")
            else:
                for p in prestamos:
                    estado = "Devuelto" if p[5] == 1 else "Pendiente"
                    print(f"ID Préstamo: {p[0]} | Usuario: {p[1]} | Libro: '{p[2]}' | Fecha: {p[3]} | Devolución: {p[4]} | Estado: {estado}")
                print("--------------------------------")

        except Exception as e:
            print("Ocurrió un error al consultar préstamos:", e)

def menu_prestamos():
    while True:
        print("\n--- MÓDULO DE PRÉSTAMOS ---")
        print("1. Registrar préstamo")
        print("2. Consultar préstamos")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            consultar_prestamos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")