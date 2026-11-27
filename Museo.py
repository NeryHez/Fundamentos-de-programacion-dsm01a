def ejecutar():

    print("Entrada al Museo")

    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Edad no válida")

    else:
        estudiante = input("¿Eres estudiante? (si/no): ").lower()

        if edad < 12:
            precio = 40

        elif edad <= 59:
            precio = 100

            if estudiante == "si":
                descuento = precio * 0.25
                precio = precio - descuento

        else:
            precio = 60

        print("El precio de entrada es: $", precio)
if __name__ == "__main__":
    ejecutar()