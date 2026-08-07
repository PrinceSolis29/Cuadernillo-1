#ejercicio 5: validacion de campos obligatorios
nombre = input("Ingrese su nombre: ").strip()
correo = input("Ingrese su correo electronico institucional: ").strip()
descripcion = input("Ingrese la descripcion del problema: ").strip()

#validamos de forma ordenada los campos obligatorios
if not nombre:
    print("Error: El campo 'nombre' es obligatorio.")
else:
    if not correo:
        print("Error: El campo 'correo' es obligatorio.") 
    else:
        if not descripcion:
            print("Error: El campo 'descripcion' es obligatorio.") 
        else:
            print("ticket registrado") 
