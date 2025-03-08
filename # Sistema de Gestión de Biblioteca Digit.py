# Sistema de Gestión de Biblioteca Digital

class Libro:
    """
    Representa un libro en la biblioteca.
    Utiliza una tupla para almacenar el título y el autor, ya que estos valores son inmutables.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable para título y autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.datos[0]} - {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    """
    Representa a un usuario con un nombre, un ID único y una lista de libros prestados.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados
    
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    """
    Gestiona la colección de libros, usuarios y el sistema de préstamos.
    """
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs de usuarios únicos
        self.registro_usuarios = {}  # Diccionario para almacenar objetos Usuario
    
    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya está en la biblioteca.")
    
    def eliminar_libro(self, isbn):
        """Elimina un libro por su ISBN."""
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("No se encontró un libro con ese ISBN.")
    
    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Este usuario ya está registrado.")
    
    def dar_baja_usuario(self, id_usuario):
        """Elimina un usuario de la biblioteca."""
        if id_usuario in self.usuarios:
            del self.registro_usuarios[id_usuario]
            self.usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("No se encontró un usuario con ese ID.")
    
    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario si está disponible."""
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[id_usuario]
            usuario.libros_prestados.append(self.libros[isbn])
            del self.libros[isbn]
            print(f"Libro prestado a {usuario.nombre}.")
        else:
            print("No se puede prestar el libro. Usuario o libro no encontrado.")
    
    def devolver_libro(self, id_usuario, isbn):
        """Devuelve un libro prestado y lo agrega nuevamente a la biblioteca."""
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto.")
                    return
        print("No se pudo devolver el libro.")
    
    def buscar_libro(self, clave):
        """Busca libros por título, autor o categoría."""
        resultados = [libro for libro in self.libros.values() 
                      if clave.lower() in libro.datos[0].lower() or
                         clave.lower() in libro.datos[1].lower() or
                         clave.lower() in libro.categoria.lower()]
        
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")
    
    def listar_libros_prestados(self, id_usuario):
        """Muestra los libros prestados a un usuario específico."""
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas
if __name__ == "__main__":
    biblioteca = Biblioteca()
    
    # Crear libros
    libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "67890")
    
    # Agregar libros
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    
    # Crear usuarios
    usuario1 = Usuario("Juan Pérez", "U001")
    usuario2 = Usuario("María López", "U002")
    
    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    
    # Prestar libros
    biblioteca.prestar_libro("U001", "12345")
    
    # Listar libros prestados
    biblioteca.listar_libros_prestados("U001")
    
    # Buscar libros
    biblioteca.buscar_libro("soledad")
    
    # Devolver libro
    biblioteca.devolver_libro("U001", "12345")
    
    # Verificar libros después de la devolución
    biblioteca.buscar_libro("1984")
