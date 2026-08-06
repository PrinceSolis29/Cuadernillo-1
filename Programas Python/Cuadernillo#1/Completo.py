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