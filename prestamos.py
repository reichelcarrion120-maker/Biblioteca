from datetime import datetime, timedelta
import sqlite3
from maker_conexion import conectar


def registrar_prestamo():
    """Punto 9: Seleccionar usuario, libro, registrar fechas y disminuir stock"""
    print("\n--- REGISTRAR PRÉSTAMO ---")

    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()

        # 1. Seleccionar usuario (Validación numérica)
        while True:
            identificacion = input(
                "Identificación del usuario (solo números): "
            ).strip()
            if identificacion.isdigit():
                break
            print("Error: La identificación debe contener solo números.")

        cursor.execute(
            "SELECT id_usuario, nombre FROM Usuarios WHERE identificacion = ?",
            (identificacion,),
        )
        usuario = cursor.fetchone()
        if not usuario:
            print("Error: El usuario no está registrado.")
            return

        id_usuario, nombre_usuario = usuario[0], usuario[1]

        # 2. Seleccionar libro
        codigo_libro = input("Código del libro: ").strip()

        cursor.execute(
            "SELECT id_libro, titulo, cantidad FROM libros WHERE codigo = ?",
            (codigo_libro,),
        )
        libro = cursor.fetchone()

        if not libro:
            print("Error: El libro no existe.")
            return

        id_libro, titulo_libro, cantidad_disponible = (
            libro[0],
            libro[1],
            libro[2],
        )

        # Verificar disponibilidad
        if cantidad_disponible <= 0:
            print("Error: No hay ejemplares disponibles de este libro.")
            return

        # 3 y 4. Registrar fecha de préstamo y devolución
        fecha_input = input(
            "Fecha de préstamo (AAAA-MM-DD) [Presione Enter para usar la fecha de hoy]: "
        ).strip()

        if not fecha_input:
            fecha_prestamo = datetime.today()
        else:
            try:
                fecha_prestamo = datetime.strptime(fecha_input, "%Y-%m-%d")
            except ValueError:
                print(
                    "Error: Formato de fecha incorrecto. Debe ser AAAA-MM-DD."
                )
                return

        # Fecha de devolución automática a 7 días
        fecha_devolucion = fecha_prestamo + timedelta(days=7)
        fecha_prestamo_str = fecha_prestamo.strftime("%Y-%m-%d")
        fecha_devolucion_str = fecha_devolucion.strftime("%Y-%m-%d")

        # Insertar préstamo
        cursor.execute(
            """
            INSERT INTO Prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion, devuelto)
            VALUES (?, ?, ?, ?, 0)
        """,
            (id_usuario, id_libro, fecha_prestamo_str, fecha_devolucion_str),
        )

        # Disminuir cantidad disponible automáticamente (-1)
        cursor.execute(
            "UPDATE libros SET cantidad = cantidad - 1 WHERE id_libro = ?",
            (id_libro,),
        )

        conexion.commit()

        print("\n¡Préstamo registrado con éxito!")
        print(f"Usuario: {nombre_usuario}")
        print(f"Libro: {titulo_libro}")
        print(f"Fecha de préstamo: {fecha_prestamo_str}")
        print(f"Fecha límite de devolución: {fecha_devolucion_str}")

    except Exception as e:
        print("Ocurrió un error al registrar el préstamo:", e)
    finally:
        conexion.close()


def registrar_devolucion():
    """Punto 10: Marcar como devuelto y aumentar stock automáticamente (+1)"""
    print("\n--- REGISTRAR DEVOLUCIÓN ---")

    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()

        busqueda = input(
            "Ingrese ID de Préstamo, Código de Libro o Cédula de Usuario: "
        ).strip()

        # Buscar préstamo pendiente
        cursor.execute(
            """
            SELECT p.id_prestamo, p.id_libro, l.titulo, u.nombre
            FROM Prestamos p
            JOIN libros l ON p.id_libro = l.id_libro
            JOIN Usuarios u ON p.id_usuario = u.id_usuario
            WHERE p.devuelto = 0 AND (p.id_prestamo = ? OR l.codigo = ? OR u.identificacion = ?)
        """,
            (busqueda, busqueda, busqueda),
        )

        prestamos_pendientes = cursor.fetchall()

        if not prestamos_pendientes:
            print(
                "Error: No se encontraron préstamos pendientes asociados a los datos ingresados."
            )
            return

        # Si hay un solo registro encontrado
        if len(prestamos_pendientes) == 1:
            id_prestamo, id_libro, titulo, usuario_nom = prestamos_pendientes[0]
        else:
            print("\nSe encontraron varios préstamos pendientes:")
            for p in prestamos_pendientes:
                print(f"ID Préstamo: {p[0]} | Libro: {p[2]} | Usuario: {p[3]}")
            id_prestamo = input(
                "Ingrese el ID del préstamo exacto a devolver: "
            ).strip()

            cursor.execute(
                "SELECT id_libro FROM Prestamos WHERE id_prestamo = ? AND devuelto = 0",
                (id_prestamo,),
            )
            res = cursor.fetchone()
            if not res:
                print("ID no válido o el préstamo ya fue devuelto.")
                return
            id_libro = res[0]

        # 1. Marcar préstamo como devuelto (1)
        cursor.execute(
            "UPDATE Prestamos SET devuelto = 1 WHERE id_prestamo = ?",
            (id_prestamo,),
        )

        # 2. Aumentar la cantidad disponible del libro automáticamente (+1)
        cursor.execute(
            "UPDATE libros SET cantidad = cantidad + 1 WHERE id_libro = ?",
            (id_libro,),
        )

        conexion.commit()
        print(
            "\n¡Devolución registrada con éxito! El stock del libro ha sido restaurado."
        )

    except Exception as e:
        print("Error al registrar devolución:", e)
    finally:
        conexion.close()


def consultar_prestamos():
    """Punto 11: Ver préstamos activos, historial completo y consultar por usuario"""
    print("\n--- CONSULTAR PRÉSTAMOS ---")
    print("1. Ver préstamos activos (Pendientes)")
    print("2. Ver historial completo de préstamos")
    print("3. Consultar préstamos por usuario")
    opcion = input("Seleccione una opción: ").strip()

    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        query_base = """
            SELECT p.id_prestamo, u.nombre, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.devuelto
            FROM Prestamos p
            JOIN Usuarios u ON p.id_usuario = u.id_usuario
            JOIN libros l ON p.id_libro = l.id_libro
        """

        if opcion == "1":
            # Ver activos
            cursor.execute(f"{query_base} WHERE p.devuelto = 0")
        elif opcion == "2":
            # Ver historial completo
            cursor.execute(query_base)
        elif opcion == "3":
            # Consultar por usuario (por nombre o identificación)
            busqueda = input(
                "Ingrese el nombre o la identificación del usuario: "
            ).strip()
            cursor.execute(
                f"{query_base} WHERE u.identificacion = ? OR u.nombre LIKE ?",
                (busqueda, f"%{busqueda}%"),
            )
        else:
            print("Opción inválida.")
            return

        registros = cursor.fetchall()
        if not registros:
            print("No se encontraron registros de préstamos.")
            return

        print("\n----- LISTA DE PRÉSTAMOS -----")
        for reg in registros:
            estado = "Devuelto" if reg[5] == 1 else "Activo (Pendiente)"
            print(
                f"ID: {reg[0]} | Usuario: {reg[1]} | Libro: '{reg[2]}' | Fecha: {reg[3]} | Devolución: {reg[4]} | Estado: {estado}"
            )
        print("-------------------------------")

    except Exception as e:
        print("Error al consultar préstamos:", e)
    finally:
        conexion.close()


def menu_prestamos():
    """Menú Principal del Módulo de Préstamos"""
    while True:
        print("\n--- MÓDULO DE PRÉSTAMOS ---")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("3. Consultar préstamos")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            consultar_prestamos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")