class Producto:
    """
    Clase que representa un producto en el inventario.
    """
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        """
        Representación en cadena del producto.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad del producto.
        :param nueva_cantidad: Nueva cantidad del producto.
        """
        self.cantidad = nueva_cantidad
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        :param nuevo_precio: Nuevo precio del producto.
        """
        self.precio = nuevo_precio


class Inventario:
    """
    Clase que gestiona una colección de productos.
    """
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía de productos.
        """
        self.productos = []
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario si el ID es único.
        :param producto: Objeto de la clase Producto a agregar.
        """
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: ID de producto ya existente.")
            return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")
    
    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        :param id_producto: Identificador del producto a eliminar.
        """
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía en el inventario.")
    
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto identificado por su ID.
        :param id_producto: Identificador del producto.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.actualizar_cantidad(cantidad)
                if precio is not None:
                    p.actualizar_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")
    
    def buscar_producto(self, nombre):
        """
        Busca productos por nombre o parte del nombre.
        :param nombre: Nombre o parte del nombre del producto.
        :return: Lista de productos encontrados o mensaje si no hay coincidencias.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return resultados if resultados else "No se encontraron productos."
    
    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    """
    Función que muestra el menú interactivo en la consola y gestiona las opciones del usuario.
    """
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Nuevo precio (deje vacío si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for p in resultados:
                    print(p)
            else:
                print(resultados)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
