# Sistema de gestión de inventario con persistencia de datos
# Permite almacenar productos en memoria y en archivo de texto
# Incluye manejo de excepciones y validaciones de datos

class Producto:
    """
    Clase que representa un producto individual en el inventario.
    Almacena ID, nombre, cantidad y precio de cada producto.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor: inicializa los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Retorna una representación en string del producto para mostrar en consola
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_string_file(self):
        """

        Convierte el producto a formato CSV para guardar en archivo.
        Retorna: string con los datos del producto separados por comas
        """
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @classmethod
    def from_string_file(cls, line):
        """

        Parámetros:
            line (str): línea de texto del archivo con formato "id,nombre,cantidad,precio"
        Retorna:
            Nueva instancia de Producto
        """
        id_producto, nombre, cantidad, precio = line.strip().split(',')
        return cls(id_producto, nombre, int(cantidad), float(precio))


class Inventario:
    """
    Clase principal que gestiona la colección de productos.
    Maneja la persistencia de datos en archivo y operaciones CRUD.
    """

    def __init__(self):
        # Inicializa la lista de productos y el nombre del archivo
        self.productos = []
        self.archivo = "inventario.txt"
        # Carga los productos existentes del archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo al iniciar el programa.
        Maneja diferentes tipos de errores que pueden ocurrir durante la lectura.
        """
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    try:
                        # Intenta crear un producto desde cada línea del archivo
                        producto = Producto.from_string_file(linea)
                        self.productos.append(producto)
                    except (ValueError, IndexError) as e:
                        # Error al procesar una línea específica del archivo
                        print(f"Error al cargar producto desde archivo: {e}")
        except FileNotFoundError:
            # El archivo no existe, se creará uno nuevo cuando se agregue un producto
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except PermissionError:
            # No hay permisos para leer el archivo
            print("Error de permisos al acceder al archivo de inventario.")
        except Exception as e:
            # Cualquier otro error no esperado
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda todo el inventario en el archivo.
        Sobrescribe el archivo completo con el estado actual del inventario.
        """
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos:
                    f.write(producto.to_string_file())
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario si su ID no existe.
        Parámetros:
            producto (Producto): instancia de la clase Producto a agregar
        Retorna:
            bool: True si se agregó exitosamente, False en caso contrario
        """
        # Verifica si ya existe un producto con el mismo ID
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: ID de producto ya existente.")
            return False
        try:
            # Agrega el producto y guarda en archivo
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto agregado y guardado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al agregar el producto: {e}")
            return False

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        Actualiza el archivo después de la eliminación.
        """
        productos_originales = len(self.productos)
        # Filtra la lista dejando solo los productos con ID diferente
        self.productos = [p for p in self.productos if p.id_producto != id_producto]

        if len(self.productos) < productos_originales:
            try:
                self.guardar_inventario()
                print("Producto eliminado y cambios guardados exitosamente.")
            except Exception as e:
                print(f"Error al guardar los cambios: {e}")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o precio de un producto existente.
        Parámetros:
            id_producto (str): ID del producto a actualizar
            cantidad (int, opcional): nueva cantidad
            precio (float, opcional): nuevo precio
        """
        for p in self.productos:
            if p.id_producto == id_producto:
                # Actualiza solo los campos proporcionados
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                try:
                    self.guardar_inventario()
                    print("Producto actualizado y cambios guardados exitosamente.")
                except Exception as e:
                    print(f"Error al guardar los cambios: {e}")
                return
        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre o parte del nombre.
        Parámetros:
            nombre (str): término de búsqueda
        Retorna:
            list: lista de productos que coinciden con la búsqueda
            str: mensaje si no se encuentran productos
        """
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados if resultados else "No se encontraron productos."

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        Imprime un mensaje si el inventario está vacío.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    """
    Función principal que muestra el menú interactivo y maneja la interacción con el usuario.
    Incluye manejo de excepciones para entrada de usuario y operaciones.
    """
    try:
        # Crea una instancia de Inventario que cargará los datos del archivo
        inventario = Inventario()
        while True:
            # Muestra el menú principal
            print("\nSistema de Gestión de Inventarios")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Mostrar todos los productos")
            print("6. Salir")

            try:
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    # Agregar nuevo producto
                    try:
                        id_producto = input("Ingrese ID del producto: ")
                        nombre = input("Ingrese nombre del producto: ")
                        cantidad = int(input("Ingrese cantidad: "))
                        precio = float(input("Ingrese precio: "))

                        # Validación de valores negativos
                        if cantidad < 0 or precio < 0:
                            print("Error: La cantidad y el precio deben ser valores positivos.")
                            continue

                        producto = Producto(id_producto, nombre, cantidad, precio)
                        inventario.agregar_producto(producto)
                    except ValueError:
                        print("Error: Por favor ingrese valores numéricos válidos para cantidad y precio.")

                elif opcion == "2":
                    # Eliminar producto existente
                    id_producto = input("Ingrese ID del producto a eliminar: ")
                    inventario.eliminar_producto(id_producto)

                elif opcion == "3":
                    # Actualizar producto existente
                    try:
                        id_producto = input("Ingrese ID del producto a actualizar: ")
                        cantidad_str = input("Nueva cantidad (deje vacío si no desea cambiar): ")
                        precio_str = input("Nuevo precio (deje vacío si no desea cambiar): ")

                        # Convierte los valores solo si se proporcionaron
                        cantidad = None if not cantidad_str else int(cantidad_str)
                        precio = None if not precio_str else float(precio_str)

                        # Validación de valores negativos
                        if (cantidad is not None and cantidad < 0) or (precio is not None and precio < 0):
                            print("Error: La cantidad y el precio deben ser valores positivos.")
                            continue

                        inventario.actualizar_producto(id_producto, cantidad, precio)
                    except ValueError:
                        print("Error: Por favor ingrese valores numéricos válidos.")

                elif opcion == "4":
                    # Buscar productos por nombre
                    nombre = input("Ingrese nombre o parte del nombre a buscar: ")
                    resultados = inventario.buscar_producto(nombre)
                    if isinstance(resultados, list):
                        for p in resultados:
                            print(p)
                    else:
                        print(resultados)

                elif opcion == "5":
                    # Mostrar todo el inventario
                    inventario.mostrar_productos()

                elif opcion == "6":
                    # Guardar y salir
                    print("Guardando inventario y saliendo del sistema...")
                    inventario.guardar_inventario()
                    break

                else:
                    print("Opción inválida, intente de nuevo.")

            except Exception as e:
                # Manejo de errores inesperados durante la ejecución del menú
                print(f"Error inesperado: {e}")
                print("Por favor, intente de nuevo.")

    except Exception as e:
        # Error fatal que impide la ejecución del programa
        print(f"Error fatal: {e}")
        print("El programa se cerrará.")


if __name__ == "__main__":
    menu()

