#ejercicio #15: mini proyecto integrado: modular de HelpDesk EDU
# Este proyecto integra los ejercicios previos en un flujo de trabajo coherente

#funciones de validacion
def validar_prioridad(prioridad_ingresada):
    prioridad = prioridad_ingresada.strip().upper()
    if prioridad in ["BAJA", "MEDIA", "ALTA"]:
        return prioridad
    else:
        return None
#Menu
def mostrar_menu():
    print(" HelpDesk EDu - Menu Principal ")
    print("1. Registrar Ticket")
    print("2. listar Tickets")
    print("3. Buscar Ticket por ID")
    print("4. ver estadisticas de prioridad")
    print("0. Salir")
    print("---------------------------------")
    
mostrar_menu()

def registro_ticket(lista_tickets, contador_id):
    print("\n Opción 1: Registro de Ticket ")
    solicitante = input("Ingrese nombre del solicitante: ").strip()
    correo = input("Ingrese correo electrónico institucional: ").strip()
    descripcion = input("Ingrese la descripción del problema: ").strip()
    
 # validacion de campos oblogatorios (logica del ejercicio 5)
    if not solicitante or not correo or not descripcion:
        print("Error: Todos los campos son obligatorios.")
        return contador_id #retorna el contador sin incrementar si hay error
# ingreso y validacion de prioridad (logica del ejercicio 6)
    prioridad_ingresada = input("Ingrese la prioridad del ticket (BAJA, MEDIA, ALTA): ")
    prioridad = validar_prioridad(prioridad_ingresada)  
    
    while prioridad is None:
        print("Error: Prioridad no válida. Intente de nuevo.")
        prioridad_ingresada = input("Ingrese la prioridad del ticket (BAJA, MEDIA, ALTA): ")
        prioridad = validar_prioridad(prioridad_ingresada) 
        
#Empaquetado todos los datos ingresados en el diccionario
    nuevo_ticket = {
    "id": contador_id,
    "solicitante": solicitante,
    "correo": correo,
    "descripcion": descripcion,
    "prioridad": prioridad
    }
    lista_tickets.append(nuevo_ticket)
    print(f"-> Ticket registrado con éxito para {solicitante} con ID: {contador_id}")
    return contador_id + 1 #incrementamos el contador para el siguiente ticket
def listar_tickets(lista_tickets):
    print("\n Opción 2: Listado de Tickets ")
    if len(lista_tickets) == 0:
        print("No hay tickets registrados.")
    else:
        print(f"Total de tickets registrados: {len(lista_tickets)}")
        for ticket in lista_tickets:
            #mostramos el reporte con los tickets ingresados
            print(f"ID: {ticket['id']}, Solicitante: {ticket['solicitante']}, Correo: {ticket['correo']}, Descripción: {ticket['descripcion']}, Prioridad: {ticket['prioridad']}")
            print("-" * 50)  # Separador visual entre tickets
