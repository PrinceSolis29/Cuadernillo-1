# Ejercicio 14: Función booleana de validación de estado

# 1. Definición de la función modular (Sin prints internos y con retornos booleanos)
def es_estado_valido(estado_ingresado):
    # Estandarizamos el texto recibido
    estado_limpio = estado_ingresado.strip().upper()
    
    # Evaluación estricta contra el catálogo permitido
    if estado_limpio in ["ABIERTO", "EN PROCESO", "RESUELTO"]:
        return True
    else:
        return False

# 2. Bloque principal interactivo (Prueba de 3 estados ingresados por el usuario)
print("--- MÓDULO INTERACTIVO DE VALIDACIÓN ---")
print("Por favor, ingrese 3 estados para evaluar el sistema.\n")

# Usamos un ciclo para pedir exactamente las 3 pruebas solicitadas
for i in range(1, 4):
    print(f"[ Entrada Número {i} de 3 ]")
    estado_usuario = input("Ingrese un estado de ticket (Ej: ABIERTO, PAUSADO, EN PROCESO): ")
    
    # Evaluamos usando nuestra función booleana
    resultado = es_estado_valido(estado_usuario)
    
    # Mostramos una respuesta clara en consola según el booleano devuelto
    if resultado:  # Es equivalente a: if resultado == True:
        print(f"-> ¡Éxito! El valor es VÁLIDO ({resultado})")
    else:
        print(f"-> ¡Error! El valor es INVÁLIDO ({resultado})")

