#Ejercicio 4: Normalizacion de texto del ticket

categoria_ticket = input("Ingrese la categoria del ticket: ")
#limpiar y normalizar el texto ingresado por el usuario y pasandolo a mayusculas
ticket_normalizado = categoria_ticket.strip().upper()

#mostrar el resultado de la normalizacion
print(f"Categoria del ticket original: {categoria_ticket}")
print(f"Categoria del ticket normalizado: {ticket_normalizado}")
