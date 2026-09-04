# Definimos credenciales
usuario_correcto = "alumno"
contraseña_correcta = "python123"
acceso_concedido = False

for i in range(1, 4):  # Permitir hasta 3 intentos
    usuario_ingresado = input(f"Intento {i}/3 - usuario: ")
    contraseña_ingresada = input(f"Intento {i}/3 - contraseña: ")
    if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("Credenciales incorrectas.")

if acceso_concedido:
    opcion = 0
    while opcion != 4:
        print("1 - Ver estado de inscripción")
        print("2 - Cambiar contraseña")
        print("3 - Mostrar mensaje motivacional")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ")
        
        if not opcion.isdigit():
            print ("Error: ingrese un numero válido.")
            continue
        
        opcion = int(opcion)
        
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
        
        if opcion == 1:
            print("Estado de inscripción: Inscrito")
            
        elif opcion == 2:
            confirmacion_contraseña = input("Ingrese su contraseña actual: ")
            while confirmacion_contraseña != contraseña_correcta:
                confirmacion_contraseña = input("Contraseña incorrecta. Ingrese su contraseña actual: ")
                
            nueva_correcta = input("Ingrese la nueva contraseña: ")
            while len(nueva_correcta) < 6:
                print("Error: la contraseña debe tener al menos 6 caracteres.")
                nueva_correcta = input("Ingrese la nueva contraseña: ")
                
            contraseña_correcta = nueva_correcta
            print("Contraseña cambiada exitosamente.")
            
        elif opcion == 3:
            print("el ahora es un regalo, por eso se llama presente")

