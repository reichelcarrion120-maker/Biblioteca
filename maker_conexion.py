print("Iniciando conexión a la base de datos maker.db...")
import sqlite3

def conexion():
    try:
        conexion = sqlite3.connect('maker.db')
        print("Conexión exitosa a maker.db")
        return conexion
    except sqlite3.Error as e:
        print("Error al conectar a maker.db: {e}")
        return None

    if __name__ == "__main__":
        conexion=conexion()
        if conexion:
            conexion.close()