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