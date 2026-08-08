# Ejercicio 13: Función reutilizable de validación de prioridad

# Convertimos tu código del Ejercicio 6 en una función reutilizable
def validar_prioridad(prioridad_ingresada):
    # Tu misma normalización del Ejercicio 6
    prioridad = prioridad_ingresada.strip().upper()
    
    # Tu misma evaluación usando 'in'
    if prioridad in ["BAJA", "MEDIA", "ALTA"]:
        return prioridad  # Enviamos la prioridad válida hacia afuera
    else:
        return None       # Si no es válida, devolvemos None (requisito del ejercicio)

# --- Bloque de pruebas para verificar que tu función quedó perfecta ---
print("--- Probando tu Función Reutilizable (Basada en el Ejercicio 6) ---")

# Caso de prueba 1 (Del cuadernillo): Pasamos "alta" en minúsculas
resultado_1 = validar_prioridad("alta")
print(f"Resultado para 'alta': {resultado_1}")  # Debe imprimir: ALTA

# Caso de prueba 2 (Del cuadernillo): Pasamos "urgente"
resultado_2 = validar_prioridad("urgente")
print(f"Resultado para 'urgente': {resultado_2}")  # Debe imprimir: None
