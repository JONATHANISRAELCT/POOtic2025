"""
Sistema de Gestión Policial
Este programa implementa un sistema para gestionar casos, agentes y patrullajes.

Clases principales:
- Agente: Representa a un agente de policía
- Caso: Representa un caso policial
- Patrullaje: Representa un patrullaje realizado por un agente
- Comisaria: Clase principal que coordina todas las operaciones
"""

from datetime import datetime
from typing import List, Dict

class Agente:
    def __init__(self, id_agente: str, nombre: str, rango: str):
        self._id_agente = id_agente
        self._nombre = nombre
        self._rango = rango
        self._casos_asignados: List[Caso] = []
        self._patrullajes_realizados: List[Patrullaje] = []

    def asignar_caso(self, caso: Caso) -> None:
        self._casos_asignados.append(caso)

    def realizar_patrullaje(self, patrullaje: Patrullaje) -> None:
        self._patrullajes_realizados.append(patrullaje)

    def __str__(self) -> str:
        return f"{self._nombre} ({self._rango})"

class Caso:
    def __init__(self, codigo: str, descripcion: str, fecha: datetime):
        self._codigo = codigo
        self._descripcion = descripcion
        self._fecha = fecha
        self._estado = "Abierto"
        self._agentes_asignados: List[Agente] = []

    def asignar_agente(self, agente: Agente) -> None:
        self._agentes_asignados.append(agente)

    def cerrar(self) -> None:
        self._estado = "Cerrado"

    def __str__(self) -> str:
        agentes = ', '.join([agente._nombre for agente in self._agentes_asignados])
        return f"Caso {self._codigo} - {self._descripcion} - Estado: {self._estado} - Agentes: {agentes}"

class Patrullaje:
    def __init__(self, agente: Agente, ubicacion: str, fecha: datetime):
        self._agente = agente
        self._ubicacion = ubicacion
        self._fecha = fecha

    def __str__(self) -> str:
        return f"Patrullaje realizado por {self._agente._nombre} en {self._ubicacion} el {self._fecha.strftime('%Y-%m-%d %H:%M:%S')}"

class Comisaria:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._agentes: Dict[str, Agente] = {}
        self._casos: List[Caso] = []

    def registrar_agente(self, agente: Agente) -> None:
        self._agentes[agente._id_agente] = agente

    def crear_caso(self, caso: Caso) -> None:
        self._casos.append(caso)

    def mostrar_agentes(self) -> None:
        print(f"\nAgentes de {self._nombre}")
        for agente in self._agentes.values():
            print(agente)

    def mostrar_casos(self) -> None:
        print(f"\nCasos en {self._nombre}")
        for caso in self._casos:
            print(caso)

def main():
    # Crear comisaría
    comisaria = Comisaria("Comisaría Central")

    # Crear agentes
    agentes = [
        Agente("A001", "Carlos Méndez", "Inspector"),
        Agente("A002", "Ana López", "Subinspectora"),
        Agente("A003", "Juan Pérez", "Oficial")
    ]
    for agente in agentes:
        comisaria.registrar_agente(agente)

    # Crear casos
    casos = [
        Caso("C001", "Robo en tienda", datetime(2025, 1, 10)),
        Caso("C002", "Asalto en calle", datetime(2025, 1, 11))
    ]
    for caso in casos:
        comisaria.crear_caso(caso)

    # Asignar agentes a casos
    casos[0].asignar_agente(agentes[0])  # Carlos Méndez
    casos[1].asignar_agente(agentes[1])  # Ana López

    # Realizar patrullajes
    patrullaje_1 = Patrullaje(agentes[2], "Barrio San Juan", datetime(2025, 1, 12))
    patrullaje_2 = Patrullaje(agentes[0], "Calle 5", datetime(2025, 1, 12))
    agentes[2].realizar_patrullaje(patrullaje_1)
    agentes[0].realizar_patrullaje(patrullaje_2)

    # Mostrar información
    print("Agentes registrados:")
    comisaria.mostrar_agentes()

    print("\nCasos registrados:")
    comisaria.mostrar_casos()

    print("\nPatrullajes realizados:")
    for agente in agentes:
        for patrullaje in agente._patrullajes_realizados:
            print(patrullaje)

if __name__ == "__main__":
    main()
