
from datetime import datetime


class Paciente:
    """Representa un paciente del consultorio odontologico."""

    def __init__(self, nombre, documento, tratamiento, prioridad, fecha):
        self.nombre = nombre
        self.documento = documento
        self.tratamiento = tratamiento
        self.prioridad = prioridad
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d").date()


class PilaUrgencias:
    """Gestiona la pila de pacientes con citas urgentes."""

    def __init__(self):
        self.pila = []

    def agregar(self, paciente):
        """Agrega un paciente a la parte superior de la pila."""
        self.pila.append(paciente)

    def retirar(self):
        """Retira y devuelve el paciente de la parte superior."""
        if self.esta_vacia():
            return None
        return self.pila.pop()

    def esta_vacia(self):
        return len(self.pila) == 0

    def mostrar(self):
        """Muestra la pila desde la cima hasta el fondo."""
        if self.esta_vacia():
            print("\nNo hay pacientes urgentes registrados.")
            return

        print("\n=== INFORME DE PILA DE URGENCIAS ===")
        print("Orden de atención: fecha más cercana a más lejana\n")

        for posicion, paciente in enumerate(reversed(self.pila), start=1):
            print(f"{posicion}. Nombre: {paciente.nombre}")
            print(f"   Documento: {paciente.documento}")
            print(f"   Tratamiento: {paciente.tratamiento}")
            print(f"   Prioridad: {paciente.prioridad}")
            print(f"   Fecha: {paciente.fecha}")
            print("-" * 40)


def crear_pacientes_ejemplo():
    """Crea datos ficticios para demostrar el programa."""
    return [
        Paciente("Laura Gomez", "1001", "Extraccion dental",
                 "Urgente", "2026-10-12"),
        Paciente("Carlos Ruiz", "1002", "Limpieza dental",
                 "Urgente", "2026-10-11"),
        Paciente("Ana Torres", "1003", "Extraccion dental",
                 "Normal", "2026-10-10"),
        Paciente("Mateo Perez", "1004", "Extraccion dental",
                 "Urgente", "2026-10-11"),
        Paciente("Sofia Diaz", "1005", "Extraccion dental",
                 "Urgente", "2026-10-15"),
    ]


def construir_pila(pacientes):
    """Filtra, ordena y carga los pacientes elegibles."""
    pila = PilaUrgencias()

    elegibles = [
        paciente for paciente in pacientes
        if paciente.tratamiento.strip().lower() == "extraccion dental"
        and paciente.prioridad.strip().lower() == "urgente"
    ]

    # Orden cronologico: de la fecha mas cercana a la mas lejana.
    elegibles.sort(key=lambda paciente: paciente.fecha)

    # Se cargan en orden inverso para que la fecha mas cercana
    # quede en la cima de la pila.
    for paciente in reversed(elegibles):
        pila.agregar(paciente)

    return pila


def menu():
    pacientes = crear_pacientes_ejemplo()
    pila = construir_pila(pacientes)

    while True:
        print("\n===== CONSULTORIO ODONTOLOGICO =====")
        print("1. Mostrar informe de urgencias")
        print("2. Atender siguiente paciente urgente")
        print("3. Ver cantidad de pacientes pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            pila.mostrar()

        elif opcion == "2":
            paciente = pila.retirar()

            if paciente is None:
                print("No hay pacientes urgentes pendientes.")
            else:
                print("\nPaciente retirado de la pila:")
                print(f"Nombre: {paciente.nombre}")
                print(f"Tratamiento: {paciente.tratamiento}")
                print(f"Fecha de cita: {paciente.fecha}")

        elif opcion == "3":
            print(f"Pacientes pendientes: {len(pila.pila)}")

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
