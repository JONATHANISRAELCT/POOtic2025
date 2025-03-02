# Sistema Avanzado de Gestión de Inventario
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado exitosamente.")
        else:
            print("El producto no se encuentra en el inventario.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("El producto no se encuentra en el inventario.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return resultados if resultados else "Producto no encontrado."

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: ${producto.precio}")

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, f)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                self.productos = {k: Producto.from_dict(v) for k, v in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}

if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\nSistema Avanzado de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto: ")
            resultado = inventario.buscar_producto(nombre)
            if isinstance(resultado, list):
                for p in resultado:
                    print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio}")
            else:
                print(resultado)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Uso de colecciones y almacenamiento
# - Se utiliza un diccionario para gestionar los productos en el inventario.
# - Cada producto tiene un ID único como clave y un objeto Producto como valor.
# - Los datos se guardan en un archivo JSON para almacenamiento persistente.
# - Se carga automáticamente el inventario desde el archivo al iniciar el programa.
