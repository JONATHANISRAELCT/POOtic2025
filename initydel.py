class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """
        Constructor de la clase CuentaBancaria.
        Este método especial se llama automáticamente cuando se crea un objeto de la clase.
        Se utiliza para inicializar los atributos del objeto (en este caso, titular y saldo).
        
        :param titular: Nombre del titular de la cuenta.
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto, 0).
        """
        self.titular = titular  # Asignamos el nombre del titular a un atributo del objeto.
        self.saldo = saldo_inicial  # Asignamos el saldo inicial.
        print(f"Cuenta creada para {self.titular} con saldo inicial de {self.saldo}.")

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta bancaria.
        Este método añade una cantidad al saldo actual.

        :param monto: Cantidad de dinero que se desea depositar.
        """
        self.saldo += monto  # Incrementamos el saldo por el monto depositado.
        print(f"{monto} depositado. Nuevo saldo: {self.saldo}.")

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta bancaria.
        Verifica si el saldo disponible es suficiente antes de realizar el retiro.

        :param monto: Cantidad de dinero que se desea retirar.
        """
        if monto > self.saldo:
            # Si el monto es mayor que el saldo actual, mostramos un mensaje de error.
            print(f"Saldo insuficiente. No se puede retirar {monto}.")
        else:
            # Si hay saldo suficiente, descontamos el monto del saldo.
            self.saldo -= monto
            print(f"{monto} retirado. Nuevo saldo: {self.saldo}.")

    def __del__(self):
        """
        Destructor de la clase CuentaBancaria.
        Este método especial se llama automáticamente cuando un objeto es destruido
        (por ejemplo, cuando ya no hay referencias al objeto o al finalizar el programa).
        
        En este caso, se utiliza para notificar que la cuenta ha sido cerrada y mostrar el saldo final.
        """
        print(f"La cuenta de {self.titular} ha sido cerrada. Saldo final: {self.saldo}.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto de la clase CuentaBancaria.
    # Aquí se llama automáticamente al constructor (__init__).
    cuenta = CuentaBancaria("Amir Israel", 500)

    # Llamamos al método 'depositar' para agregar dinero a la cuenta.
    cuenta.depositar(200)

    # Llamamos al método 'retirar' para retirar dinero de la cuenta.
    cuenta.retirar(100)

    # Intentamos retirar más dinero del que hay en la cuenta para ver el manejo de errores.
    cuenta.retirar(700)

    # Cuando el programa termina, el destructor (__del__) se llama automáticamente.
