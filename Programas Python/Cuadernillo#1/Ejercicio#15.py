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
    print(" Bienvenido a HelpDesk EDu - Menu Principal ")
    print("1. Registrar Ticket")
    print("2. listar Tickets")
    print("3. Buscar Ticket por ID")
    print("4. ver estadisticas de prioridad")
    print("0. Salir")
    print("---------------------------------")
    

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
    print(f"-> Ticket registrado con éxito para {solicitante} con ID: {contador_id} \n")
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

#funcion de busqueda de ticket por ID (logica del ejercicio 12)
def buscar_ticket_por_id(lista_tickets):
    print("\n Opción 3: Búsqueda de Ticket por ID ")
    if len(lista_tickets) == 0:
        print("No hay tickets registrados.\n")
        return

    try:
        id_buscar = int(input("Ingrese el ID del ticket que desea buscar: "))
        ticket_encontrado = None

        for ticket in lista_tickets:
            if ticket["id"] == id_buscar:
                ticket_encontrado = ticket
                break

        if ticket_encontrado:
            print("\n[ Ticket Localizado ]")
            print(f"ID: {ticket_encontrado['id']}")
            print(f"Solicitante: {ticket_encontrado['solicitante']}")
            print(f"Correo: {ticket_encontrado['correo']}")
            print(f"Descripción: {ticket_encontrado['descripcion']}")
            print(f"Prioridad: {ticket_encontrado['prioridad']}")
        else:
            print("No existe ticket con el ID proporcionado.\n")

    except ValueError:
        print("Error: Debe ingresar un número entero válido para el ID.\n")
        
#funcion de estadisticas de prioridad (logica del ejercicio 11)        
def estadisticas_prioridad(lista_tickets):
    print("\n Opción 4: Estadísticas de Prioridad ")
    total_tickets = len(lista_tickets)
    if total_tickets == 0:
        print("No hay tickets registrados.")
    else:
        lista_prioridades = [ticket["prioridad"] for ticket in lista_tickets]
        baja = lista_prioridades.count("BAJA")
        media = lista_prioridades.count("MEDIA")   
        alta = lista_prioridades.count("ALTA")
        porcentaje_baja = round((baja / total_tickets) * 100)
        porcentaje_media = round((media / total_tickets) * 100)
        porcentaje_alta = round((alta / total_tickets) * 100)
        
        print(f"Total de tickets procesados: {total_tickets}")
        print(f"BAJA: {porcentaje_baja}% {baja} tickets")
        print(f"MEDIA: {porcentaje_media}% {media} tickets")
        print(f"ALTA: {porcentaje_alta}% {alta} tickets \n")
        
# control principal del sistema
#definimos la funcion main() para encapsular la logica principal del programa
def main():
    base_tickets = []  # Lista para almacenar los tickets
    id_secuencial = 1  # Contador de ID para los tickets
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4) o '0' para salir: ").strip()
        if opcion == "1":
            id_secuencial = registro_ticket(base_tickets, id_secuencial)
        elif opcion == "2":
            listar_tickets(base_tickets)
        elif opcion == "3":
            buscar_ticket_por_id(base_tickets)
        elif opcion == "4":
            estadisticas_prioridad(base_tickets)
        elif opcion == "0":
            print("Saliendo del sistema HelpDesk EDu. ¡Hasta luego!")
        else:
            print("Opción no válida. Intente de nuevo.\n")
#punto de entrada del programa
if __name__ == "__main__":
    main()
