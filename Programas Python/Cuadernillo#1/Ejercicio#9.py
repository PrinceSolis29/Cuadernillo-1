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
