#Ejercicio 5: Metodo cambiar_estado() con validacion de estados
class Ticket:
    def __init__(self, ticket_id, solicitante, prioridad):
        #constructor de la clase Ticket que inicializa los atributos del ticket y valida la prioridad
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"  # Estado inicial por defecto
        # Eliminamos espacios en blanco y convertimos a mayúsculas para la validación
        prioridad_limpia = prioridad.strip().upper()
        if prioridad_limpia in ["BAJA", "MEDIA", "ALTA"]:
            self.prioridad = prioridad_limpia
        else:
            raise ValueError(f"Prioridad inválida: '{prioridad}'")

    def mostrar_resumen(self):
        # Método que imprime un resumen del ticket en un formato legible
        print(f"ID: #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
      # Método que permite cambiar el estado del ticket, validando que el nuevo estado sea uno de los permitidos.
        # Normalizamos el valor recibido (eliminamos espacios y pasamos a mayúsculas)
        estado_limpio = nuevo_estado.strip().upper()
        
        # Catálogo oficial de estados permitidos por la regla de negocio
        estados_validos = ["ABIERTO", "EN_PROCESO", "RESUELTO"]
        
        if estado_limpio in estados_validos:
            self.estado = estado_limpio
            return True
        else:
            return False

# --- Casos de Prueba ---
if __name__ == "__main__":
    
    print("--- Caso de Prueba 1 ---")
    ticket1 = Ticket(1, "Ana Lopez", "alta") # Nace en ABIERTO
    print('Entrada: cambiar_estado("en_proceso")')
    
    if ticket1.cambiar_estado("en_proceso"):
        print("Salida esperada: SI se actualizo, estado actualizado.")
    else:
        print("Salida esperada: NO se actualizo, estado sin cambios.")
        
    print(f"Estado actual del ticket: {ticket1.estado}")
    print() # Salto de línea
    
    print("    Caso de Prueba 2 ")
    ticket2 = Ticket(2, "Luis Perez", "media") # Nace limpio en ABIERTO
    print('Entrada: cambiar_estado("pausado")')
    
    if ticket2.cambiar_estado("pausado"):
        print("Salida esperada: SI se actualizo, estado actualizado.")
    else:
        print("Salida esperada: NO se actualizo, estado sin cambios.")
        
    print(f"Estado actual del ticket: {ticket2.estado}")
    print() # Salto de línea


