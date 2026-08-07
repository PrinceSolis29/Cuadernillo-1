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
