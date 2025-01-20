# Clase base que representa un Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre  # Atributo público
        self.__salario = salario  # Atributo privado (encapsulación)
    
    def obtener_salario(self):
        return self.__salario  # Método para acceder al atributo privado
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Salario: {self.__salario}"
    
    def trabajar(self):
        return "El empleado está trabajando..."

# Clase derivada que representa un Gerente y hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    # Polimorfismo: sobrescritura del método "trabajar"
    def trabajar(self):
        return f"El gerente {self.nombre} está gestionando el departamento de {self.departamento}."

# Clase derivada que representa un Desarrollador y hereda de Empleado
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    
    # Polimorfismo: sobrescritura del método "trabajar"
    def trabajar(self):
        return f"El desarrollador {self.nombre} está programando en {self.lenguaje}."

# Creación de objetos e invocación de métodos
gerente1 = Gerente("Carlos", 5000, "Ventas")
dev1 = Desarrollador("Ana", 4000, "Python")

# Demostración de herencia, encapsulación y polimorfismo
print(gerente1.mostrar_info())
print(gerente1.trabajar())

print(dev1.mostrar_info())
print(dev1.trabajar())
