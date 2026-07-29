class Persona:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre


class Usuario(Persona):
    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)
        self.correo = correo
        self.telefono = telefono

    def mostrar(self):
        print(f"ID: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Teléfono: {self.telefono}")


class Libro:
    def __init__(self, codigo, titulo, autor, categoria, cantidad):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Categoría: {self.categoria}")
        print(f"Cantidad disponible: {self.cantidad}")


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion, devuelto=False):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = devuelto

    def mostrar(self):
        print(f"Usuario: {self.usuario}")
        print(f"Libro: {self.libro}")
        print(f"Fecha préstamo: {self.fecha_prestamo}")
        print(f"Fecha devolución: {self.fecha_devolucion}")
        print(f"Devuelto: {'Sí' if self.devuelto else 'No'}")