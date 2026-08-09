# Ejercicio 18: Filtrado de tickets por prioridad

# 1. Definición de la función modular requerida
def filtrar_por_prioridad(tickets, prioridad):
    # La función debe devolver una lista nueva, no imprimir ni modificar la recibida
    lista_filtrada = []
    # Normalizar la prioridad recibida antes de comparar
    prioridad_limpia = prioridad.strip().upper()
    
    # Recorrido lineal buscando múltiples coincidencias
    for ticket_individual in tickets:
        if ticket_individual["prioridad"] == prioridad_limpia:
            lista_filtrada.append(ticket_individual)
            
    return lista_filtrada  # Regresamos la lista con las coincidencias encontradas


# 2. Programa Principal - Módulo de Registro (Basado exactamente en tu Ejercicio 12)
tickets = []
contador_id = 1

print("--- Registro Inicial de Tickets para Filtrado ---")
solicitante = input("Ingrese el nombre del solicitante (o '0' para finalizar el registro): ").strip()

# Bucle dinámico con centinela para simular la base de datos en memoria
while solicitante != "0":
    prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
    
    # Validación interactiva de la prioridad (Siguiendo tu patrón del ejercicio 12)
    while prioridad not in ["BAJA", "MEDIA", "ALTA"]:
        print("Error: Prioridad inválida. Intente de nuevo.")
        prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
        
    # Creamos la estructura de diccionario requerida para este ejercicio (id, solicitante, prioridad)
    ticket = {
        "id": contador_id,
        "solicitante": solicitante,
        "prioridad": prioridad
    }
    tickets.append(ticket)
    print(f"-> Ticket registrado con éxito. ID Asignado: {contador_id}")
    contador_id += 1  # Incrementamos el ID para el siguiente ticket
    
    print("-------------------------------------------------")
    solicitante = input("Ingrese el nombre del siguiente solicitante (o '0' para finalizar): ").strip()


print("\n--- Módulo de Filtrado de Tickets (Vista del Supervisor) ---")
# Validación con len() para verificar que existan datos cargados en memoria
if len(tickets) == 0:
    print("No hay tickets en memoria para realizar un filtrado.")
else:
    prioridad_supervisor = input("Ingrese la prioridad que desea filtrar (BAJA, MEDIA, ALTA): ")
    
    # Invocamos nuestra función modular pasándole los datos necesarios
    resultados_busqueda = filtrar_por_prioridad(tickets, prioridad_supervisor)
    
    # Evaluamos los resultados devueltos por la función mediante len()
    if len(resultados_busqueda) > 0:
        # Mostramos cuántos se encontraron (Caso de prueba 1)
        print(f"\nTickets con prioridad {prioridad_supervisor.strip().upper()}: {len(resultados_busqueda)}")
        print("=" * 50)
        
        # Desplegamos todos los tickets que coincidieron con el filtro
        for t in resultados_busqueda:
            print(f"🔹 ID: {t['id']} | Solicitante: {t['solicitante']} | Prioridad: {t['prioridad']}")
        print("=" * 50)
    else:
        # Mensaje claro cuando no hay coincidencias (Caso de prueba 2)
        print(f"No hay tickets con prioridad {prioridad_supervisor.strip().upper()}.")
