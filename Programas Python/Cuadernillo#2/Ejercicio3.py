#Ejercicio 3: clase ticket con validacion en el constructor
class Ticket:
    def __init__(self, ticket_id, solicitante, prioridad):
    #constructor de la clase Ticket que inicializa los atributos del ticket y valida la prioridad
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"  # Estado inicial por defecto obligatoriamente
        
        # Eliminamos espacios en blanco y convertimos a mayúsculas
        prioridad_convertida = prioridad.strip().upper()
        
        # Validación del catálogo de opciones permitidas
        if prioridad_convertida in ["BAJA", "MEDIA", "ALTA"]:
            self.prioridad = prioridad_convertida
        else:
            raise ValueError(f"Prioridad inválida: '{prioridad}'. Unicamente debe ser BAJA, MEDIA o ALTA.")

# --- Casos de Prueba ---
if __name__ == "__main__":
    print("    Pruebas de casos")
    
    # Caso 1: Creación de ticket exitoso
    try:
        ticket1 = Ticket(1, "Ana Lopez", "alta")
        print(f"Ticket {ticket1.ticket_id} creado.")
        print(f"Solicitante: {ticket1.solicitante} | Prioridad: {ticket1.prioridad} | Estado: {ticket1.estado}")
    except ValueError as e:
        print(f"[ERROR] {e}")
        
    print("-" * 45)

    # Caso 2: Intento de creación erróneo (prioridad incorrecta)
    try:
        print("Intentando crear ticket con prioridad 'urgente'...")
        ticket2 = Ticket(2, "Luis Perez", "urgente")
        print("La validación no se ejecutó.")
    except ValueError as e:
        print(f"Mensaje de error del sistema: {e}")