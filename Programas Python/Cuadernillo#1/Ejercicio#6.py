# Ejercicio 6: Validacion de prioridad del ticket
prioridad_ingresada = input("Ingrese la prioridad del ticket (BAJA, MEDIA, ALTA): ")

# Normalizamos la entrada eliminando espacios y pasando a mayusculas
prioridad = prioridad_ingresada.strip().upper()

# Evaluamos si el valor esta dentro del conjunto permitido usando 'in'
if prioridad in ["BAJA", "MEDIA", "ALTA"]:
    print(f"Prioridad valida: {prioridad}")
else:
    print("Error: prioridad no valida.")
