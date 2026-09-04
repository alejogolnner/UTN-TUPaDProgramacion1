# Ejercicio 1 - Caja del Kiosco

# Pedir nombre del cliente
nombre = input("Ingrese el nombre del cliente: ")

while not nombre.isalpha(): # Validación de que el nombre contenga solo letras
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")

# Pedir cantidad de productos
cantidad = input("Ingrese la cantidad de productos a comprar: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: la cantidad debe ser un número entero positivo.")
    cantidad = input("Ingrese la cantidad de productos a comprar: ")

cantidad = int(cantidad)

# Variables para acumular los totales
total_sin_descuentos = 0
total_con_descuentos = 0

# Pedir datos de cada producto
for i in range(1, cantidad + 1):

    # Pedir precio
    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    # Preguntar si tiene descuento
    descuento = input(f"Producto {i} - Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: debe ingresar S o N.")
        descuento = input(f"Producto {i} - Descuento (S/N): ").lower()

    # Acumular precio sin descuento
    total_sin_descuentos += precio

    # Aplicar descuento si corresponde
    if descuento == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuentos += precio_final


# Cálculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

# Mostrar resultados
print("\n-------------------------------------------------")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print("\n-------------------------------------------------")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")