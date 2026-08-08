# Ejercicio 12: Búsqueda de ticket por ID
tickets = []
contador_id = 1

print("--- Registro Inicial de Tickets para Búsqueda ---")
# ingreso de datos iniciales para la lista de tickets
solicitante = input("Ingrese el nombre del solicitante (o '0' para finalizar el registro): ").strip()

# Bucle dinámico con centinela para simular la base de datos en memoria
while solicitante != "0":
    estado = input("Ingrese el estado (ABIERTO, EN PROCESO, RESUELTO): ").strip().upper()
    
    # Validación interactiva del estado antes de guardar el registro
    while estado not in ["ABIERTO", "EN PROCESO", "RESUELTO"]:
        print("Error: Estado inválido. Intente de nuevo.")
        estado = input("Ingrese el estado (ABIERTO, EN PROCESO, RESUELTO): ").strip().upper()
        
    # Creamos la estructura de diccionario requerida para este ejercicio
    ticket = {
        "id": contador_id,
        "solicitante": solicitante,
        "estado": estado
    }
    tickets.append(ticket)
    print(f"-> Ticket registrado con éxito. ID Asignado: {contador_id}")
    contador_id += 1  # Incrementamos el ID para el siguiente ticket
    
    print("-------------------------------------------------")
    solicitante = input("Ingrese el nombre del siguiente solicitante (o '0' para finalizar): ").strip()

print("\n--- Módulo de Búsqueda de Tickets ---")
# Validación con len() para verificar que existan datos cargados
if len(tickets) == 0:
    print("No hay tickets en memoria para realizar una búsqueda.")
else:
    #try except para manejar errores de conversión de tipo
    try:
        id_buscar = int(input("Ingrese el ID del ticket que desea buscar: "))
        #none es un valor especial que indica ausencia de valor, útil para inicializar variables
        ticket_encontrado = None
        
        # Búsqueda lineal obligatoria usando ciclo for
        for ticket_individual in tickets:
            if ticket_individual["id"] == id_buscar:
                ticket_encontrado = ticket_individual
                break # Coincidencia hallada, detenemos el recorrido inmediatamente
                
        # Despliegue de resultados según los Casos de Prueba
        if ticket_encontrado:
            print("\n[ Ticket Localizado ]")
            print(f"ID: {ticket_encontrado['id']}")
            print(f"Solicitante: {ticket_encontrado['solicitante']}")
            print(f"Estado: {ticket_encontrado['estado']}")
        else:
            print("No existe ticket con el ID proporcionado.")
            
    except ValueError:
        print("Error: Debe ingresar un número entero válido para el ID.")
