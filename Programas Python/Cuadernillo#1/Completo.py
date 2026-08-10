#Ejercicio 1: Bienvenida al sistema hepdeskt EDU
print("HelpDesk EDU - Sistema de soporte academico")
print("Escriba su solicitud siguiendo las instrucciones en pantalla")
print("Su solicitud sera atendida por un operador lo mas pronto posible")

#Ejercio 2: Registro del solicitante
Nombre_Solicitante = input("Ingrese su nombre: ").strip()
Correo = input("Ingrese su correo electronico institucional: ").strip()
print(f"Gracias {Nombre_Solicitante}, su solicitud ha sido registrada, se le enviaran actualizaciones al correo {Correo}.")

#ejercicio #3: captura de datos del primer ticket
numero_ticket = input("Ingrese el numero de ticket: ").strip()
descripcion = input("Ingrese la descripcion del problema: ").strip()
tiempo = input("Ingrese el tiempo estimado (en horas): ").strip()

try:
    #convertir tiempo a float}
    tiempo_estimado = float(tiempo)
    print(f"Tiempo estimado: {tiempo_estimado} horas")
except ValueError:
    #si el usuario ingresa el tiempo erroneo
    print("Error: El tiempo estimado debe ser un numero valido.")
    
#Ejercicio 4: Normalizacion de texto del ticket

categoria_ticket = input("Ingrese la categoria del ticket: ")
#limpiar y normalizar el texto ingresado por el usuario y pasandolo a mayusculas
ticket_normalizado = categoria_ticket.strip().upper()

#mostrar el resultado de la normalizacion
print(f"Categoria del ticket original: {categoria_ticket}")
print(f"Categoria del ticket normalizado: {ticket_normalizado}")

#ejercicio 5: validacion de campos obligatorios
nombre = input("Ingrese su nombre: ").strip()
correo = input("Ingrese su correo electronico institucional: ").strip()
descripcion = input("Ingrese la descripcion del problema: ").strip()

#validamos de forma ordenada los campos obligatorios
if not nombre:
    print("Error: El campo 'nombre' es obligatorio.")
else:
    if not correo:
        print("Error: El campo 'correo' es obligatorio.") 
    else:
        if not descripcion:
            print("Error: El campo 'descripcion' es obligatorio.") 
        else:
            print("ticket registrado") 

# Ejercicio 6: Validacion de prioridad del ticket
prioridad_ingresada = input("Ingrese la prioridad del ticket (BAJA, MEDIA, ALTA): ")

# Normalizamos la entrada eliminando espacios y pasando a mayusculas
prioridad = prioridad_ingresada.strip().upper()

# Evaluamos si el valor esta dentro del conjunto permitido usando 'in'
if prioridad in ["BAJA", "MEDIA", "ALTA"]:
    print(f"Prioridad valida: {prioridad}")
else:
    print("Error: prioridad no valida.")

# Ejercicio 7: Reglas combinadas de escalamiento
categoria_ingresada = input("Ingrese la categoria del ticket: ")
prioridad_ingresada = input("Ingrese la prioridad del ticket: ")

# limpiamos y poenemos en mayusculas las entradas
categoria = categoria_ingresada.strip().upper()
prioridad = prioridad_ingresada.strip().upper()

# Combinamos las condiciones usando el operador logico 'AND'
if categoria == "INFRAESTRUCTURA" and prioridad == "ALTA":
    print("Ticket escalado a supervisor.")
else:
    print("Ticket sigue el flujo normal.")
   
# Ejercicio 8: Registro de varios tickets con centinela
contador_tickets = 0

# Primera captura (lectura inicial)
nombre = input("Ingrese nombre del solicitante (o '0' para salir): ").strip()

# El ciclo se ejecuta mientras el usuario NO escriba '0'
while nombre != "0":
    correo = input("Ingrese correo electronico institucional: ").strip()
    descripcion = input("Ingrese la descripcion del problema: ").strip()
    contador_tickets += 1
    print(f"-> Ticket #{contador_tickets} registrado temporalmente.")
    
    # Volvemos a pedir el dato para actualizar el ciclo
    nombre = input("Ingrese nombre del proximo solicitante (o '0' para salir): ").strip()

print(f"Se registraron {contador_tickets} tickets.")

# Ejercicio 9: Listado de tickets en memoria
# Creamos una lista vacia para almacenar los tickets
tickets = []

# Registramos exactamente 3 tickets usando un ciclo for
for i in range(1, 4):
    descripcion = input(f"Ingrese descripcion para el ticket {i}: ").strip()
    #append() agrega el elemento al final de la lista
    tickets.append(descripcion)

print("\n   Listado de Tickets en Memoria    ")

# Usamos un contador manual para llevar el numero de la lista
numero = 1
for ticket in tickets:
    print(f"{numero}. {ticket}")
    numero += 1  # Le sumamos 1 para el siguiente ticket
    
# Ejercicio 10: Conteo de tickets por estado 
# Inicializamos los contadores para cada estado
abierto = 0
en_proceso = 0
resuelto = 0

print("--- Registro de Estados de Tickets ---")
# Pedimos el primer estado. Escribir '0' sirve para terminar el registro.
estado = input("Ingrese estado del ticket (ABIERTO, EN_PROCESO, RESUELTO) o '0' para finalizar: ").strip().upper()

while estado != "0":
    if estado == "ABIERTO":
        abierto += 1
        print("-> Registrado: ABIERTO")
    elif estado == "EN PROCESO":
        en_proceso += 1
        print("-> Registrado: EN PROCESO")
    elif estado == "RESUELTO":
        resuelto += 1
        print("-> Registrado: RESUELTO")
    else:
        print("Error: Estado no valido. Solo se permite ABIERTO, EN PROCESO o RESUELTO.")
    
    # Separador visual y nueva solicitud para actualizar el ciclo
    print("--------------------------------------")
    estado = input("Ingrese el estado del siguiente ticket (o '0' para finalizar): ").strip().upper()

# Mostramos el reporte final consolidado
print("\n--- Reporte Final de Turno ---")
print(f"ABIERTO: {abierto}, EN_PROCESO: {en_proceso}, RESUELTO: {resuelto}")


