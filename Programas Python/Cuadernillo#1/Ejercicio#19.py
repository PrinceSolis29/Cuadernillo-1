# Ejercicio 19: Control de intentos limitados

# Establecemos las constantes de control
MAX_INTENTOS = 3
intento_actual = 1
prioridad_valida = False
prioridad = ""

print("--- Validación de Prioridad con Intentos Limitados ---")

# el ciclo solo permite un máximo de 3 intentos o hasta que se ingrese un valor válido
while intento_actual <= MAX_INTENTOS and not prioridad_valida:
    print(f"\n[ Intento {intento_actual} de {MAX_INTENTOS} ]")
    
    # captura de la prioridad ingresada por el usuario
    prioridad_ingresada = input("Ingrese la prioridad del ticket (BAJA, MEDIA, ALTA): ")
    
    #normalización exacta del Ejercicio 6
    prioridad = prioridad_ingresada.strip().upper()
    
    # evaluación de la prioridad ingresada
    if prioridad in ["BAJA", "MEDIA", "ALTA"]:
        print(f"Ticket registrado con prioridad: {prioridad}")
        prioridad_valida = True  # Activamos la bandera para terminar el ciclo con éxito
    else:
        print("Error: prioridad no válida.")
        intento_actual += 1  # Incrementamos el contador si hay un fallo

print("----------------------------------------------------")

# Evaluación final tras agotar el ciclo
if not prioridad_valida:
    print("Se ha excedido el número máximo de intentos permitidos, ticket no registrado.")
