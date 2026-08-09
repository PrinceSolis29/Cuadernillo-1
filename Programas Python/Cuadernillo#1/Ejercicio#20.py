# Ejercicio 20: Reporte de cierre de turno en formato tabular

tickets = []
contador_id = 1

print("--- Registro de Tickets para Cierre de Turno ---")
solicitante = input("Ingrese el nombre del solicitante (o '0' para finalizar): ").strip()

# Bucle dinámico interactivo con centinela para simular la base de datos
while solicitante != "0":
    prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
    #while para validar la prioridad ingresada, repitiendo hasta que sea correcta
    while prioridad not in ["BAJA", "MEDIA", "ALTA"]:
        print("Error: Prioridad inválida.")
        prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
       #try-except para validar que las horas ingresadas sean un número positivo 
    try:
        horas = float(input("Ingrese las horas de atención (Ej: 1.5): "))
        while horas <= 0:
            print("Error: Las horas deben ser mayores a cero.")
            horas = float(input("Ingrese las horas de atención: "))
    except ValueError:
        print("Error: Formato numérico inválido. Se asignará 1.0 hora por defecto.")
        horas = 1.0
        
    # Empaquetamos los datos en un diccionario y lo agregamos a la lista de tickets
    ticket = {
        "id": contador_id,
        "solicitante": solicitante,
        "prioridad": prioridad,
        "horas": horas
    }
    tickets.append(ticket)
    print(f"-> Datos guardados temporalmente para el ID: {contador_id}")
    contador_id += 1
    
    print("-------------------------------------------------")
    solicitante = input("Ingrese el nombre del siguiente solicitante (o '0' para finalizar): ").strip()


# --- MÓDULO DE GENERACIÓN DEL REPORTE TABULAR ---
print("\n==========================================================")
print("                REPORTE DE CIERRE DE TURNO                ")
print("==========================================================")

if len(tickets) == 0:
    print("ℹNo se registraron tickets atendidos en este turno.")
else:
    # ENCABEZADO ALINEADO: Usamos :< para reservar espacios exactos por columna
    # Código toma 10 espacios, Solicitante 22, Prioridad 12 y Horas 8
    print(f"{'CÓDIGO':<10} | {'SOLICITANTE':<22} | {'PRIORIDAD':<12} | {'HORAS':<8}")
    print("-" * 58)
    
    acumulador_horas = 0.0
    
    # Recorrido para construir la tabla fila por fila
    for t in tickets:
        # REQUISITO: Generamos el código TCK-001 a partir del id numérico
        codigo_formateado = f"TCK-{t['id']:03d}"
        acumulador_horas += t["horas"]
        
        # FILA ALINEADA: Imprime cada ticket perfectamente alineado bajo su encabezado
        print(f"{codigo_formateado:<10} | {t['solicitante']:<22} | {t['prioridad']:<12} | {t['horas']:<8.2f}")
        
    print("-" * 58)
    # LÍNEA FINAL: Muestra el total consolidado perfectamente cuadrado
    print(f"{'TOTAL DE HORAS DEL TURNO:':<48} | {acumulador_horas:<8.2f}")

print("==========================================================")
