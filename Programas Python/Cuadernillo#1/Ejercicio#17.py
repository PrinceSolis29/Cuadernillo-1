# Ejercicio 18: Filtrado de tickets por prioridad

# 1. Función modular: Recibe minúsculas o mayúsculas, pero busca en mayúsculas
def filtrar_por_prioridad(tickets, prioridad):
    lista_filtrada = []
    # Estandarizamos a mayúsculas para que la búsqueda funcione siempre
    prioridad_limpia = prioridad.strip().upper()
    
    for ticket_individual in tickets:
        if ticket_individual["prioridad"] == prioridad_limpia:
            lista_filtrada.append(ticket_individual)
            
    return lista_filtrada


# 2. Programa Principal - Registro de Datos (Lógica de tu Ejercicio 12)
tickets = []
contador_id = 1

print("--- Registro Inicial de Tickets para Filtrado ---")
solicitante = input("Ingrese el nombre del solicitante (o '0' para finalizar el registro): ").strip()

while solicitante != "0":
    prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
    
    while prioridad not in ["BAJA", "MEDIA", "ALTA"]:
        print("Error: Prioridad inválida. Intente de nuevo.")
        prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ").strip().upper()
        
    ticket = {
        "id": contador_id,
        "solicitante": solicitante,
        "prioridad": prioridad
    }
    tickets.append(ticket)
    print(f"-> Ticket registrado con éxito. ID Asignado: {contador_id}")
    contador_id += 1
    
    print("-------------------------------------------------")
    solicitante = input("Ingrese el nombre del siguiente solicitante (o '0' para finalizar): ").strip()


print("\n--- Módulo de Filtrado de Tickets (Vista del Supervisor) ---")
if len(tickets) == 0:
    print("No hay tickets en memoria para realizar un filtrado.")
else:
    # 🌟 AQUÍ SE CUMPLE TU CASO DE PRUEBA: El usuario puede escribir "alta" o "baja" en minúsculas
    prioridad_supervisor = input("Ingrese la prioridad que desea filtrar (BAJA, MEDIA, ALTA): ")
    
    # Pasamos la entrada tal cual a la función
    resultados_busqueda = filtrar_por_prioridad(tickets, prioridad_supervisor)
    
    # Creamos una variable en mayúsculas únicamente para los textos de salida de la pantalla
    prioridad_salida_mayuscula = prioridad_supervisor.strip().upper()
    
    if len(resultados_busqueda) > 0:
        # 🌟 Salida exacta Caso 1: "Tickets con prioridad ALTA: 2"
        print(f"\nTickets con prioridad {prioridad_salida_mayuscula}: {len(resultados_busqueda)}, seguido de los dos tickets.")
        print("=" * 65)
        for t in resultados_busqueda:
            print(f"🔹 ID: {t['id']} | Solicitante: {t['solicitante']} | Prioridad: {t['prioridad']}")
        print("=" * 65)
    else:
        # 🌟 Salida exacta Caso 2: "No hay tickets con prioridad BAJA."
        print(f"No hay tickets con prioridad {prioridad_salida_mayuscula}.")

