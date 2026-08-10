#Ejercicio 4: metodo mostrar_resumen()
class Ticket:
    def __init__(self, ticket_id, solicitante, prioridad):
        #constructor de la clase Ticket que inicializa los atributos del ticket y valida la prioridad
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"
        # Eliminamos espacios en blanco y convertimos a mayúsculas para la validación
        prioridad_limpia = prioridad.strip().upper()
        if prioridad_limpia in ["BAJA", "MEDIA", "ALTA"]:
            self.prioridad = prioridad_limpia
        else: #raise ValueError(f"Prioridad inválida: '{prioridad}'. Debe ser BAJA, MEDIA o ALTA.")
            raise ValueError(f"Prioridad inválida: '{prioridad}'")

    def mostrar_resumen(self):
        # Método que imprime un resumen del ticket en un formato legible
        print(f"ID: #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}")

# --- Casos de Prueba ---
if __name__ == "__main__":
    print("    Pruebas de Control")
    
    # Creación del ticket para la prueba
      # --- Casos de Prueba ---
    
    # Caso 1: Creación de ticket correcto (prioridad válida)
    print("--- Caso 1: Prioridad Válida ---")
    try:
        ticket_prueba = Ticket(101, "Ana Lopez", "alta")
        print("Ejecutando ticket_prueba.mostrar_resumen():")
        ticket_prueba.mostrar_resumen()
    except ValueError as e:
        print(f"Error inesperado: {e}")
        
    print() # Salto de línea
    
    # Caso 2: Intento de creación erróneo (prioridad incorrecta)
    print("    Caso 2: Prioridad Inválida ")
    try:
        print("Intentando crear ticket con prioridad 'urgente'...")
        ticket_uno = Ticket(102, "Luis Perez", "urgente")
        # Esta línea no se ejecutará si se lanza el error:
        ticket_uno.mostrar_resumen() 
    except ValueError as e:
        print(f"Mensaje de error del sistema -> {e} Solo se permite BAJA, MEDIA o ALTA.")
        print()
        
