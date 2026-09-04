# Definimos variables
lunes_turno_1 = "alejo"
lunes_turno_2 = "juan"
lunes_turno_3 = ""
lunes_turno_4 = ""
martes_turno_1 = ""
martes_turno_2 = "maria"
martes_turno_3 = ""

# 1. Pedir nombre
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("Por favor, ingrese un nombre válido (solo letras).")
    nombre = input("Ingrese su nombre: ")

opcion = 0
# 2. Menú repetitivo
while opcion != 5:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1 - Reservar turno")
    print("2 - Cancelar turno")
    print("3 - Ver agenda del día")
    print("4 - Ver resumen general")
    print("5 - Cerrar sistema")
    
    entrada = input("Seleccione una opción: ")
    
    # Validaciones con isdigit()
    if not entrada.isdigit():
        print("Error: ingrese un numero válido.")
        continue
    
    opcion = int(entrada)
    
    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue
    
    # 3. Reservar
    if opcion == 1:
        seleccion_dia = input("Ingrese el día para reservar (1 - Lunes, 2 - Martes): ")
        while seleccion_dia != "1" and seleccion_dia != "2":
            seleccion_dia = input("Error: ingrese un número válido (1 - Lunes, 2 - Martes): ")
            
        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
            print("Error: ingrese un nombre válido (solo letras).")
            paciente = input("Ingrese nombre del paciente: ")
        
        paciente = paciente.lower()
        
        if seleccion_dia == "1":
            if paciente == lunes_turno_1 or paciente == lunes_turno_2 or paciente == lunes_turno_3 or paciente == lunes_turno_4:
                print("Error: El paciente ya tiene un turno asignado el Lunes.")
            else:
                if lunes_turno_1 == "": 
                    lunes_turno_1 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 1).")
                elif lunes_turno_2 == "": 
                    lunes_turno_2 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 2).")
                elif lunes_turno_3 == "": 
                    lunes_turno_3 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 3).")
                elif lunes_turno_4 == "": 
                    lunes_turno_4 = paciente
                    print("Turno reservado con éxito en Lunes (Turno 4).")
                else:
                    print("Lo sentimos, no hay turnos libres el Lunes.")
                    
        elif seleccion_dia == "2":
            if paciente == martes_turno_1 or paciente == martes_turno_2 or paciente == martes_turno_3:
                print("Error: El paciente ya tiene un turno asignado el Martes.")
            else:
                if martes_turno_1 == "": 
                    martes_turno_1 = paciente
                    print("Turno reservado con éxito en Martes (Turno 1).")
                elif martes_turno_2 == "": 
                    martes_turno_2 = paciente
                    print("Turno reservado con éxito en Martes (Turno 2).")
                elif martes_turno_3 == "": 
                    martes_turno_3 = paciente
                    print("Turno reservado con éxito en Martes (Turno 3).")
                else:
                    print("Lo sentimos, no hay turnos libres el Martes.")

    # 4. Cancelar
    elif opcion == 2:
        seleccion_dia = input("Ingrese el día para cancelar (1 - Lunes, 2 - Martes): ")
        while seleccion_dia != "1" and seleccion_dia != "2":
            seleccion_dia = input("Error: ingrese un número válido (1 - Lunes, 2 - Martes): ")
            
        paciente = input("Ingrese nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            print("Error: ingrese un nombre válido (solo letras).")
            paciente = input("Ingrese nombre del paciente a cancelar: ")
        
        paciente = paciente.lower()
        
        encontrado = False
        if seleccion_dia == "1":
            if lunes_turno_1 == paciente: 
                lunes_turno_1 = ""
                encontrado = True
            elif lunes_turno_2 == paciente: 
                lunes_turno_2 = ""
                encontrado = True
            elif lunes_turno_3 == paciente: 
                lunes_turno_3 = ""
                encontrado = True
            elif lunes_turno_4 == paciente: 
                lunes_turno_4 = ""
                encontrado = True
        elif seleccion_dia == "2":
            if martes_turno_1 == paciente: 
                martes_turno_1 = ""
                encontrado = True
            elif martes_turno_2 == paciente: 
                martes_turno_2 = ""
                encontrado = True
            elif martes_turno_3 == paciente: 
                martes_turno_3 = ""
                encontrado = True
                
        if encontrado:
            print("Turno cancelado exitosamente.")
        else:
            print("No se encontró ningún turno a nombre de ese paciente en el día seleccionado.")

    # 5. Ver agenda del día
    elif opcion == 3:
        seleccion_dia = input("Ingrese el día a consultar (1 - Lunes, 2 - Martes): ")
        while seleccion_dia != "1" and seleccion_dia != "2":
            seleccion_dia = input("Error: ingrese un número válido (1 - Lunes, 2 - Martes): ")
            
        if seleccion_dia == "1":
            print("\n--- Agenda del Lunes ---")
            print("Turno 1:", lunes_turno_1 if lunes_turno_1 != "" else "(libre)")
            print("Turno 2:", lunes_turno_2 if lunes_turno_2 != "" else "(libre)")
            print("Turno 3:", lunes_turno_3 if lunes_turno_3 != "" else "(libre)")
            print("Turno 4:", lunes_turno_4 if lunes_turno_4 != "" else "(libre)")
        elif seleccion_dia == "2":
            print("\n--- Agenda del Martes ---")
            print("Turno 1:", martes_turno_1 if martes_turno_1 != "" else "(libre)")
            print("Turno 2:", martes_turno_2 if martes_turno_2 != "" else "(libre)")
            print("Turno 3:", martes_turno_3 if martes_turno_3 != "" else "(libre)")

    # 6. Resumen general
    elif opcion == 4:
        ocupados_lunes = 0
        if lunes_turno_1 != "": ocupados_lunes += 1
        if lunes_turno_2 != "": ocupados_lunes += 1
        if lunes_turno_3 != "": ocupados_lunes += 1
        if lunes_turno_4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes
        
        ocupados_martes = 0
        if martes_turno_1 != "": ocupados_martes += 1
        if martes_turno_2 != "": ocupados_martes += 1
        if martes_turno_3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes
        
        print("\n--- Resumen General ---")
        print(f"Lunes:  {ocupados_lunes} turnos ocupados, {libres_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} turnos ocupados, {libres_martes} disponibles.")
        
        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos ocupados es el: LUNES")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos ocupados es el: MARTES")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados (Empate).")

    elif opcion == 5:
        print(f"\nCerrando el sistema... ¡Hasta luego, {nombre}!")
            