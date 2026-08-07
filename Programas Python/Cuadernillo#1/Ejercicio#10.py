# Ejercicio 10: Conteo de tickets por estado 
abierto = 0
en_proceso = 0
resuelto = 0

print("--- Registro de Estados de Tickets ---")
# Pedimos el primer estado. Escribir '0' sirve para terminar el registro.
estado = input("Ingrese estado del ticket (ABIERTO, EN_PROCESO, RESUELTO) o '0' para finalizar: ").strip().upper()

while estado != "0":
    if estado == "ABIERTO":
        abierto += 1
        print("-> Registrado: ABIERTO")
    elif estado == "EN PROCESO":
        en_proceso += 1
        print("-> Registrado: EN PROCESO")
    elif estado == "RESUELTO":
        resuelto += 1
        print("-> Registrado: RESUELTO")
    else:
        print("Error: Estado no valido. Solo se permite ABIERTO, EN PROCESO o RESUELTO.")
    
    # Separador visual y nueva solicitud para actualizar el ciclo
    print("--------------------------------------")
    estado = input("Ingrese el estado del siguiente ticket (o '0' para finalizar): ").strip().upper()

# Mostramos el reporte final consolidado
print("\n--- Reporte Final de Turno ---")
print(f"ABIERTO: {abierto}, EN_PROCESO: {en_proceso}, RESUELTO: {resuelto}")
