# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
bloqueado = False
anti_spam = 0


print("Sos un agente que intenta abrir una bóveda con 3 cerraduras.")
print("Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.")

nombre_agente = input("Agente, ingrese su nombre: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Error: el nombre debe contener solo letras, ingrese su nombre: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    
    if alarma and tiempo <= 3:
        print(f"Derrota agente {nombre_agente}. Alarma activada y tiempo crítico. El sistema se bloquea. cerraduras abiertas: {cerraduras_abiertas}")
        bloqueado = True
        continue   
    
    print(f"\nAgente {nombre_agente}, su energía es {energia}, quedan {tiempo} minutos, ha abierto {cerraduras_abiertas} cerraduras, y la alarma está {'encendida' if alarma else 'apagada'}.")
    print("Opciones:")
    print(" 1 - Forzar cerradura (-20 de energía y -2 minutos)")
    print(" 2 - Hackear panel (-10 de energía y -3 minutos)")
    print(" 3 - Descansar (+15 de energía y -1 minuto; si alarma ON: -10 energía extra)")
    
    opcion = input("Seleccione una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error: opción inválida. Seleccione 1, 2 o 3: ")
    
    if opcion == "1":
        anti_spam += 1
        energia -= 20
        tiempo -= 2
        
        if anti_spam >= 3:
            print("Demasiados intentos de forzar cerradura seguidos.")
            alarma = True
            print("La cerradura se trabó. Alarma activada.")
            continue
            
        if energia < 40:
            print("¡Riesgo de alarma! Tu energía es baja.")
            riesgo = input("Ingrese un número del 1 al 3: ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Error: opción inválida. Ingrese un número del 1 al 3: ")
            
            if int(riesgo) == 3:
                alarma = True
                print("¡Alarma activada!")
            
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura forzada con éxito.")
        else:
            print("No se pudo abrir la cerradura porque la alarma está encendida.")
    
    elif opcion == "2":
        anti_spam = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            letra = input(f"Ingrese letra {i+1} del código parcial: ")
            while not letra.isalpha() or len(letra) != 1:
                letra = input(f"Error: ingrese una letra válida para la posición {i+1}: ")
            codigo_parcial += letra.upper()
        if len(codigo_parcial) >= 8:
            print(f"Panel hackeado con éxito. Código parcial: {codigo_parcial}; ¡Cerradura abierta!")
            cerraduras_abiertas += 1
    
    elif opcion == "3":
        anti_spam = 0
        energia += 15
        tiempo -= 1
        
        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma estaba encendida. Energía reducida en 10.")
        else:
            print("Descanso completado. Energía aumentada.")

        if energia > 100:
            energia = 100
            print("Energía máxima alcanzada (100).")
    
if cerraduras_abiertas >= 3:
    print(f"VICTORIA, Agente {nombre_agente}")   

if energia <= 0 or tiempo <= 0:
    print(f"\nDERROTA agente {nombre_agente}. Energía: {energia}, Tiempo: {tiempo} minutos, Cerraduras abiertas: {cerraduras_abiertas}.")

if bloqueado:
    print(f"\nDERROTA agente {nombre_agente}. El sistema se bloqueó debido a la alarma y tiempo crítico.")