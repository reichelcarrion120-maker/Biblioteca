from libros import menu_libros
from usuarios import menu_usuarios
from prestamos import menu_prestamos


def mostrar_menu():
    print("\n========================================")
    print("     SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("========================================")
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Gestión de Préstamos")
    print("4. Salir")
    print("========================================")


def menu_principal():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_libros()

        elif opcion == "2":
            menu_usuarios()

        elif opcion == "3":
            menu_prestamos()

        elif opcion == "4":
            print("\nGracias por utilizar el Sistema de Gestión de Biblioteca.")
            print("¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()