# ==========================
# CLASE PERSONA
# ==========================

class Persona:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre


# ==========================
# CLASE USUARIO (HEREDA DE PERSONA)
# ==========================

class Usuario(Persona):
    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)
        self.correo = correo
        self.telefono = telefono

    def mostrar(self):
        return (
            f"ID: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )


# ==========================
# CLASE LIBRO
# ==========================

class Libro:
    def __init__(self, codigo, titulo, autor, categoria, cantidad):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.cantidad = cantidad

    def mostrar(self):
        return (
            f"Código: {self.codigo}\n"
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Categoría: {self.categoria}\n"
            f"Cantidad disponible: {self.cantidad}"
        )


# ==========================
# CLASE PRESTAMO
# ==========================

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion, devuelto=False):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = devuelto

    def mostrar(self):
        estado = "Sí" if self.devuelto else "No"

        return (
            f"Usuario: {self.usuario}\n"
            f"Libro: {self.libro}\n"
            f"Fecha préstamo: {self.fecha_prestamo}\n"
            f"Fecha devolución: {self.fecha_devolucion}\n"
            f"Devuelto: {estado}"
        )