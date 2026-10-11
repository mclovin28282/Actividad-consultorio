
from collections import deque


class Paciente:
    """Representa un paciente de la agenda diaria."""

    def __init__(self, nombre, documento, hora, tratamiento):
        self.nombre = nombre
        self.documento = documento
        self.hora = hora
        self.tratamiento = tratamiento


class ColaAtencion:
    """Administra la fila de pacientes mediante una cola FIFO."""

    def __init__(self):
        self.cola = deque()

    def registrar(self, paciente):
        """Agrega un paciente al final de la cola."""
        self.cola.append(paciente)
        print(f"Paciente {paciente.nombre} registrado correctamente.")

    def atender(self):
        """Retira al primer paciente de la cola."""
        if self.esta_vacia():
            return None
        return self.cola.popleft()

    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar_agenda(self):
        """Muestra los pacientes en orden de llegada."""
        if self.esta_vacia():
            print("\nLa agenda no tiene pacientes pendientes.")
            return

        print("\n=== AGENDA DIARIA ===")

        for posicion, paciente in enumerate(self.cola, start=1):
            print(f"\nTurno {posicion}")
            print(f"Nombre: {paciente.nombre}")
            print(f"Documento: {paciente.documento}")
            print(f"Hora: {paciente.hora}")
            print(f"Tratamiento: {paciente.tratamiento}")

    def cantidad_pendientes(self):
        return len(self.cola)


def cargar_agenda_ejemplo(cola):
    """Registra una agenda ficticia inicial."""
    cola.registrar(
        Paciente("Laura Gomez", "1001", "08:00", "Extraccion dental")
    )
    cola.registrar(
        Paciente("Carlos Ruiz", "1002", "08:30", "Limpieza dental")
    )
    cola.registrar(
        Paciente("Ana Torres", "1003", "09:00", "Revision dental")
    )


def menu():
    cola = ColaAtencion()
    cargar_agenda_ejemplo(cola)

    while True:
        print("\n===== AGENDA DEL CONSULTORIO =====")
        print("1. Registrar paciente")
        print("2. Mostrar agenda")
        print("3. Atender siguiente paciente")
        print("4. Consultar pacientes pendientes")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            nombre = input("Nombre del paciente: ").strip()
            documento = input("Documento ficticio: ").strip()
            hora = input("Hora de la cita (HH:MM): ").strip()
            tratamiento = input("Tratamiento: ").strip()

            if not nombre or not documento or not tratamiento:
                print("Error: complete todos los campos.")
                continue

            try:
                from datetime import datetime
                datetime.strptime(hora, "%H:%M")
            except ValueError:
                print("Hora invalida. Use el formato HH:MM.")
                continue

            paciente = Paciente(nombre, documento, hora, tratamiento)
            cola.registrar(paciente)

        elif opcion == "2":
            cola.mostrar_agenda()

        elif opcion == "3":
            paciente = cola.atender()

            if paciente is None:
                print("No hay pacientes pendientes por atender.")
            else:
                print("\nSiguiente paciente llamado:")
                print(f"Nombre: {paciente.nombre}")
                print(f"Hora: {paciente.hora}")
                print(f"Tratamiento: {paciente.tratamiento}")

        elif opcion == "4":
            print(
                "Pacientes pendientes:",
                cola.cantidad_pendientes()
            )

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
