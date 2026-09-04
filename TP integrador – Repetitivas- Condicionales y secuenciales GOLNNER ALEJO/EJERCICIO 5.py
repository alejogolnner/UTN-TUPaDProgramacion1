vida_gladiador = 100
vida_enemigo = 100
pocion = 3
ataque_gladiador = 15
ataque_enemigo = 12
turno_gladiador = True

print("--- BIENVENIDO A LA ARENA ---")
gladiador = input("Nombre del Gladiador: ").capitalize()
while not gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    gladiador = input("Nombre del Gladiador: ").capitalize()

print("\n=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pocion}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Opción: ")
    
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
    
    opcion = int(opcion)
    
    # 1 Ataque Pesado
    if opcion == 1:
        if vida_enemigo < 20:
            dano_final = ataque_gladiador * 1.5
        else:
            dano_final = ataque_gladiador
            
        vida_enemigo -= dano_final
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

    # 2 Ráfaga Veloz
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
    
    # 3 Curar
    elif opcion == 3:
        if pocion > 0:
            vida_gladiador += 30
            pocion -= 1
        else:
            print("¡No quedan pociones!")
    
    if vida_enemigo > 0:
        vida_gladiador -= ataque_enemigo
        print(f">> ¡El enemigo contraataca por {ataque_enemigo} puntos!")
    
    print("\n === NUECVO TURNO ===")

# fin del juego
print("\n=== FIN DEL JUEGO ===")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")