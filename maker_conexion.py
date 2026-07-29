import sqlite3

def conectar():
    """Crea y devuelve una conexión a la base de datos maker.db"""
    conexion = sqlite3.connect("maker.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

if __name__ == "__main__":
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas = cursor.fetchall()
    print("Tablas encontradas:", tablas)

    conexion.close()


        