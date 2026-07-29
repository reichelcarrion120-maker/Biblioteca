from libros import menu_libros
from usuarios import menu_usuarios
from prestamos import menu_prestamos

def menu_principal():
    while True:
        print("\n==================================")
        print(" SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("==================================")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_libros()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_prestamos()
        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()