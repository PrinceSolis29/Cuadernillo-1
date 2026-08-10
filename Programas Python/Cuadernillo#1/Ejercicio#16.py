
# Ejercicio 16: Reporte de tiempos de atención

tiempos = []

print("--- Registro de Tiempos de Atención ---")
tiempo_input = input("Ingrese el tiempo en horas (Ej: 1.5, 2.25) o '0' para finalizar: ").strip()

# Bucle interactivo con centinela para recolectar los tiempos del día
while tiempo_input != "0":
    try:
        horas = float(tiempo_input)
        if horas > 0:
            tiempos.append(horas)
            print(f"-> Registrado: {horas} horas")
        else:
            print("Error: El tiempo debe ser una cantidad mayor a cero.")
    except ValueError:
        print("Error: Debe ingresar un número válido (use punto para decimales).")
        
    print("---------------------------------------")
    tiempo_input = input("Ingrese el tiempo del siguiente ticket (o '0' para finalizar): ").strip()

print("\n--- Reporte Final de Tiempos (Cierre de Turno) ---")
total_registros = len(tiempos)

# Validación obligatoria de lista vacía
if total_registros == 0:
    print("No hay tiempos registrados.")
else:
    # Requisito estricto: Inicializar variables y recorrer la lista UNA SOLA VEZ
    acumulador_total = 0.0
    atencion_mas_rapida = tiempos[0]
    atencion_mas_lenta = tiempos[0]
    
    for t in tiempos:
        acumulador_total += t  # Acumulamos el total
        
        if t < atencion_mas_rapida:
            atencion_mas_rapida = t  # Localizamos el mínimo
            
        if t > atencion_mas_lenta:
            atencion_mas_lenta = t   # Localizamos el máximo
            
    # Cálculo de promedio con redondeo a 2 decimales
    #round() redondea el resultado a 2 decimales
    promedio_horas = round(acumulador_total / total_registros, 2)
    
    # Despliegue de resultados con el formato del cuadernillo
    print(f"Tiempo total: {acumulador_total} horas")
    print(f"Tiempo promedio: {promedio_horas} horas")
    print(f"Atención más rápida: {atencion_mas_rapida} horas")
    print(f"Atención más lenta: {atencion_mas_lenta} horas")
