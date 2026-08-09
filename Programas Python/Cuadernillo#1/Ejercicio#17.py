# Ejercicio 17: Conteo por categoría con diccionario dinámico
# Usamos un diccionario vacío que aprenderá las categorías sobre la marcha.
conteo_categorias = {}

print("--- Registro Dinámico de Categorías de Tickets ---")
# se solicita la primera categoría. Escribir '0' sirve para terminar el registro.
categoria_input = input("Ingrese la categoría del ticket (Ej: Redes, Software, Impresoras) o '0' para finalizar: ").strip().upper()

# Bucle interactivo idéntico al de tu Ejercicio 10
while categoria_input != "0":
    if categoria_input != "":
        # el metodo .get() permite obtener el valor de una clave en el diccionario, y si no existe, devuelve un valor por defecto (en este caso 0).
        # Si la categoría no existe en el diccionario, devuelve 0 y le suma 1
        # Si ya existía, toma el número anterior y le suma 1
        conteo_categorias[categoria_input] = conteo_categorias.get(categoria_input, 0) + 1
        print(f"-> Registrado en la categoría: {categoria_input}")
    else:
        print("Error: No se permiten categorías vacías.")
        
    print("-------------------------------------------------")
    categoria_input = input("Ingrese la categoría del siguiente ticket (o '0' para finalizar): ").strip().upper()

print("\n--- Reporte Final de Categorías ---")

# validación de diccionario vacío exigida
if len(conteo_categorias) == 0:
    print("No hay categorías registradas.")
else:
    # Recorremos con .items() y ordenamos alfabéticamente con sorted()
    # mostramos cada categoría y su cantidad de tickets registrados
    for categoria, cantidad in sorted(conteo_categorias.items()):
        print(f"{categoria}: {cantidad}\n")
