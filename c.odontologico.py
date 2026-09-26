VALOR_CITA_PARTICULAR = 80000
VALOR_CITA_EPS = 5000
VALOR_CITA_PREPAGADA = 30000

def calcular_valor_atencion(tipo_cliente, tipo_atencion):
    if tipo_cliente == "particular":
        if tipo_atencion == "limpieza":
            return 60000
        elif tipo_atencion == "calzas":
            return 80000
        elif tipo_atencion == "extraccion":
            return 100000
        elif tipo_atencion == "diagnostico":
            return 50000

    elif tipo_cliente == "eps":
        if tipo_atencion == "limpieza":
            return 0
        elif tipo_atencion == "calzas":
            return 40000
        elif tipo_atencion == "extraccion":
            return 40000
        elif tipo_atencion == "diagnostico":
            return 0

    elif tipo_cliente == "prepagada":
        if tipo_atencion == "limpieza":
            return 0
        elif tipo_atencion == "calzas":
            return 10000
        elif tipo_atencion == "extraccion":
            return 10000
        elif tipo_atencion == "diagnostico":
            return 0

    return 0

lista_clientes = []

print("==================================================")
print("   SISTEMA DE REGISTRO - CONSULTORIO ODONTOLÓGICO  ")
print("==================================================")

continuar_registro = "s"

while continuar_registro == "s":
    print("\n--- DATOS DEL CLIENTE ---")
    cedula = input("Ingrese la cédula: ").strip()
    nombre = input("Ingrese el nombre completo: ").strip()
    telefono = input("Ingrese el teléfono: ").strip()

    print("\nTipo de Cliente:")
    print(" 1. Particular")
    print(" 2. EPS")
    print(" 3. Prepagada")
    opcion_cliente = input("Seleccione una opción (1-3): ").strip()

    if opcion_cliente == "1":
        tipo_cliente = "particular"
        valor_base_cita = VALOR_CITA_PARTICULAR
    elif opcion_cliente == "2":
        tipo_cliente = "eps"
        valor_base_cita = VALOR_CITA_EPS
    elif opcion_cliente == "3":
        tipo_cliente = "prepagada"
        valor_base_cita = VALOR_CITA_PREPAGADA
    else:
        print("Opción no válida. Se asignará 'Particular' por defecto.")
        tipo_cliente = "particular"
        valor_base_cita = VALOR_CITA_PARTICULAR

    print("\nTipo de Atención:")
    print(" 1. Limpieza")
    print(" 2. Calzas")
    print(" 3. Extracción")
    print(" 4. Diagnóstico")
    opcion_atencion = input("Seleccione una opción (1-4): ").strip()

    if opcion_atencion == "1":
        tipo_atencion = "limpieza"
    elif opcion_atencion == "2":
        tipo_atencion = "calzas"
    elif opcion_atencion == "3":
        tipo_atencion = "extraccion"
    elif opcion_atencion == "4":
        tipo_atencion = "diagnostico"
    else:
        print("Opción no válida. Se asignará 'Diagnóstico' por defecto.")
        tipo_atencion = "diagnostico"

    if tipo_atencion == "limpieza" or tipo_atencion == "diagnostico":
        cantidad = 1
        print(f"Nota: Para {tipo_atencion} la cantidad asignada es 1.")
    else:
        cantidad = int(input(f"Ingrese la cantidad para {tipo_atencion} (debe ser mayor a 0): "))
        while cantidad <= 0:
            print("Error: La cantidad debe ser un número mayor a 0.")
            cantidad = int(input(f"Ingrese nuevamente la cantidad para {tipo_atencion}: "))

    print("\nPrioridad de Atención:")
    print(" 1. Normal")
    print(" 2. Urgente")
    opc_prioridad = input("Seleccione prioridad (1-2): ").strip()
    if opc_prioridad == "2":
        prioridad = "Urgente"
    else:
        prioridad = "Normal"

    fecha_cita = input("Ingrese la fecha de la cita (DD/MM/AAAA): ").strip()

    precio_unidad_atencion = calcular_valor_atencion(tipo_cliente, tipo_atencion)
    costo_total_atencion = precio_unidad_atencion * cantidad
    total_a_pagar = valor_base_cita + costo_total_atencion

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha_cita": fecha_cita,
        "valor_cita": valor_base_cita,
        "valor_atencion": costo_total_atencion,
        "total_pagar": total_a_pagar
    }

    lista_clientes.append(cliente)

    continuar_registro = input("\n¿Desea ingresar otro cliente? (s/n): ").strip().lower()

print("\n" + "="*50)
print("             RESUMEN Y ESTADÍSTICAS             ")
print("="*50)

total_clientes = len(lista_clientes)
ingresos_totales = 0
clientes_extraccion = 0

for c in lista_clientes:
    ingresos_totales = ingresos_totales + c["total_pagar"]
    if c["tipo_atencion"] == "extraccion":
        clientes_extraccion = clientes_extraccion + 1

print(f"1. Total de clientes atendidos: {total_clientes}")
print(f"2. Ingresos totales recibidos: ${ingresos_totales}")
print(f"3. Número de clientes para extracción de dientes: {clientes_extraccion}")

n = len(lista_clientes)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lista_clientes[j]["total_pagar"] < lista_clientes[j + 1]["total_pagar"]:
            aux = lista_clientes[j]
            lista_clientes[j] = lista_clientes[j + 1]
            lista_clientes[j + 1] = aux

print("\n" + "="*50)
print(" LISTA DE CLIENTES ORDENADA (MAYOR A MENOR VALOR) ")
print("="*50)

for i in range(len(lista_clientes)):
    cli = lista_clientes[i]
    print(f"{i + 1}. {cli['nombre']} | Cédula: {cli['cedula']} | Tipo: {cli['tipo_cliente']} | Atención: {cli['tipo_atencion']} | Total: ${cli['total_pagar']}")

print("\n" + "="*50)
print("             BÚSQUEDA DE CLIENTE                ")
print("="*50)

cedula_buscar = input("Ingrese la cédula del cliente que desea buscar: ").strip()
encontrado = False

for cli in lista_clientes:
    if cli["cedula"] == cedula_buscar:
        encontrado = True
        print("\n¡CLIENTE ENCONTRADO!")
        print(f" Cédula: {cli['cedula']}")
        print(f" Nombre: {cli['nombre']}")
        print(f" Teléfono: {cli['telefono']}")
        print(f" Tipo de Cliente: {cli['tipo_cliente']}")
        print(f" Tipo de Atención: {cli['tipo_atencion']}")
        print(f" Cantidad: {cli['cantidad']}")
        print(f" Prioridad: {cli['prioridad']}")
        print(f" Fecha de Cita: {cli['fecha_cita']}")
        print(f" Total a Pagar: ${cli['total_pagar']}")
        break

if not encontrado:
    print(f"\nNo se encontró ningún cliente registrado con la cédula {cedula_buscar}.")
