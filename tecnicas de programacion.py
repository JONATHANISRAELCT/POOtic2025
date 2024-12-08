# Clase base Personaje: Representa un personaje genérico en el juego.
class Personaje:
    def _init_(self, nombre, fuerza, agilidad, defensa, vida):
        self.nombre = nombre  # Nombre del personaje.
        self.fuerza = fuerza  # Nivel de fuerza física.
        self.agilidad = agilidad  # Nivel de agilidad (habilidad para esquivar ataques).
        self.defensa = defensa  # Nivel de defensa contra ataques.
        self.vida = vida  # Puntos de vida del personaje.

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Agilidad:", self.agilidad)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha caído en combate.")

    def atacar(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


# Clase Arquero: Especializado en ataques a distancia con un multiplicador basado en precisión.
class Arquero(Personaje):
    def _init_(self, nombre, fuerza, agilidad, defensa, vida, precision):
        super()._init_(nombre, fuerza, agilidad, defensa, vida)
        self.precision = precision  # Multiplicador de daño basado en precisión.

    def atributos(self):
        super().atributos()
        print("·Precisión:", self.precision)

    def daño(self, enemigo):
        # El daño depende de la fuerza del arquero y su precisión.
        return max(0, (self.fuerza * self.precision) - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} dispara una flecha causando {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


# Clase Caballero: Especializado en combate cuerpo a cuerpo con alta defensa.
class Caballero(Personaje):
    def _init_(self, nombre, fuerza, agilidad, defensa, vida, escudo):
        super()._init_(nombre, fuerza, agilidad, defensa, vida)
        self.escudo = escudo  # Valor adicional de defensa proporcionado por el escudo.

    def atributos(self):
        super().atributos()
        print("·Escudo:", self.escudo)

    def daño(self, enemigo):
        # El daño depende de la fuerza del caballero.
        return max(0, self.fuerza - enemigo.defensa - self.escudo)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} golpea con su espada causando {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


# Función de combate: Simula una batalla entre dos personajes.
def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(f">>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)
        turno += 1

    # Resultado del combate.
    if jugador_1.esta_vivo():
        print(f"\n¡{jugador_1.nombre} ha ganado el combate!")
    elif jugador_2.esta_vivo():
        print(f"\n¡{jugador_2.nombre} ha ganado el combate!")
    else:
        print("\nEl combate ha terminado en empate.")


# Crear instancias de Arquero y Caballero.
personaje_1 = Arquero("Legolas", 15, 20, 5, 80, 2)
personaje_2 = Caballero("Aragorn", 20, 10, 10, 100, 5)

# Mostrar atributos iniciales.
print("Atributos iniciales de los personajes:")
personaje_1.atributos()
personaje_2.atributos()

# Iniciar el combate.
combate(personaje_1, personaje_2)