# Ejercicio 11: Estadística de prioridad
prioridades = []

print("--- Registro de Prioridades de Tickets ---")
# Captura inicial aplicando normalización de texto
prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA) o '0' para finalizar: ").strip().upper()

# Bucle dinámico con centinela
while prioridad != "0":
    if prioridad in ["BAJA", "MEDIA", "ALTA"]:
        #append() agrega el elemento al final de la lista
        prioridades.append(prioridad)
        print(f"-> Registrada prioridad: {prioridad}")
    else:
        print("Error: Prioridad no válida. Solo se permite BAJA, MEDIA o ALTA.")
    
    print("------------------------------------------")
    prioridad = input("Ingrese la prioridad del siguiente ticket (o '0' para finalizar): ").strip().upper()

print("\n--- Reporte Estadístico de Prioridades ---")
#len() devuelve el tamaño de la lista
total_tickets = len(prioridades)

# Validación de lista vacía exigida por el requisito
if total_tickets == 0:
    print("No hay tickets registrados.")
else:
    # Contar ocurrencias exactas en la lista
    #count() devuelve el número de veces que un elemento aparece en la lista
    baja = prioridades.count("BAJA")
    media = prioridades.count("MEDIA")
    alta = prioridades.count("ALTA")
    
    # Cálculo con redondeo integrado
    #round() redondea el resultado a un entero
    porcentaje_baja = round((baja / total_tickets) * 100)
    porcentaje_media = round((media / total_tickets) * 100)
    porcentaje_alta = round((alta / total_tickets) * 100)
    
    print(f"Total de tickets procesados: {total_tickets}")
    #las {} permiten mostrar variables dentro de un string
    print(f"BAJA: {porcentaje_baja}%, MEDIA: {porcentaje_media}%, ALTA: {porcentaje_alta}%")
