#Ejercicio 2: clase de usuario con atributis basicos
class Usuario:
    #_int_ es un método especial que se llama automáticamente cuando se crea una nueva instancia de la clase. Se utiliza para inicializar los atributos del objeto.
    def __init__(self, nombre, correo, rol):
        # self es una referencia al objeto actual de la clase. Se utiliza para acceder a los atributos y métodos de la instancia.
        self.nombre = nombre    # Almacena el nombre completo
        self.correo = correo    # Almacena el email institucional
        self.rol = rol          # Almacena el tipo de rol asignado

#Casos de Prueba ---
if __name__ == "__main__":
    # Caso 1: Crear e imprimir los datos del primer usuario (Solicitante)
    usuario1 = Usuario("Ana Lopez", "ana@umg.edu.gt", "solicitante")
    print("    Datos de Usuario 1    ")
    print(f"Nombre: {usuario1.nombre}")
    print(f"Correo: {usuario1.correo}")
    print(f"Rol:    {usuario1.rol}")
    print() # Salto de línea

    # Caso 2: Crear e imprimir los datos del segundo usuario (Técnico)
    usuario2 = Usuario("Luis Perez", "luis@umg.edu.gt", "tecnico")
    print("    Datos de Usuario 2    ")
    print(f"Nombre: {usuario2.nombre}")
    print(f"Correo: {usuario2.correo}")
    print(f"Rol:    {usuario2.rol}")
    print() # Salto de línea
    
 # Caso 23: Crear e imprimir los datos del segundo usuario (Técnico)
    usuario3 = Usuario("Juan Juarez", "juan@umg.edu.gt", "supervisor")
    print("    Datos de Usuario 3    ")
    print(f"Nombre: {usuario3.nombre}")
    print(f"Correo: {usuario3.correo}")
    print(f"Rol:    {usuario3.rol}")
    print() # Salto de línea