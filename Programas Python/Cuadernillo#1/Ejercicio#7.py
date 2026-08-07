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
