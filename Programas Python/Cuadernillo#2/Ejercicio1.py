#Ejercicio 1: Declaración de Clases y objetos en HelpDesk EDU
#class Usuario: Representa a los usuarios del sistema
class Usuario:
    #pass es una palabra reservada que indica que no hay implementación en la clase
    pass

class Ticket:
    #class Ticket: Representa los tickets de soporte generados por los usuarios
    pass

class Notificacion:
    #class Notificacion: Representa las alertas enviadas a los usuarios
    pass

# --- Casos de Prueba (Instanciación básica) ---
if __name__ == "__main__":
    # Creamos instancias vacías para validar que no existan errores de sintaxis
    usuario_prueba = Usuario()
    ticket_prueba = Ticket()
    notificacion_prueba = Notificacion()
    
    print("las 3 clases se han instanciado correctamente y sin errores")
