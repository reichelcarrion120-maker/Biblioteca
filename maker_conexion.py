import os
import sqlite3

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

RUTA_BD = os.path.join(DIRECTORIO_ACTUAL, "maker.db")


def conectar():
    """Conecta a la base de datos maker.db en una ruta fija"""
    try:
        conexion = sqlite3.connect(RUTA_BD)
        conexion.execute("PRAGMA foreign_keys = ON")
        return conexion
    except sqlite3.Error as e:
        print(f"Error de conexión: {e}")
        return None


def crear_tablas():
    """Crea la estructura correcta de tablas en el archivo maker.db unificado"""
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.executescript(
                """
                CREATE TABLE IF NOT EXISTS Usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    identificacion TEXT NOT NULL UNIQUE,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    telefono TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS libros (
                    id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT NOT NULL UNIQUE,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    cantidad INTEGER NOT NULL DEFAULT 1
                );

                CREATE TABLE IF NOT EXISTS Prestamos (
                    id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    id_libro INTEGER NOT NULL,
                    fecha_prestamo TEXT NOT NULL,
                    fecha_devolucion TEXT NOT NULL,
                    devuelto INTEGER DEFAULT 0,
                    FOREIGN KEY(id_usuario) REFERENCES Usuarios(id_usuario),
                    FOREIGN KEY(id_libro) REFERENCES libros(id_libro)
                );
            """
            )
            conn.commit()
        finally:
            conn.close()


if __name__ == "__main__":
    crear_tablas()
    print("¡Base de datos unificada y reconstruida con éxito!")