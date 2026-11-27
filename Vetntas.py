def ejecutar():

    print("Registro de ventas")

    total = 0
    cantidad = 0
    venta_mayor = False

    venta = float(input("Ingresa el importe de la venta (ingrese solo 0 para terminar): "))

    while venta != 0:

        if venta < 0:
            print("Importe no válido")

        else:
            total += venta
            cantidad += 1

            if venta >= 1000:
                venta_mayor = True

        venta = float(input("Ingresa otra venta (ingrese solo 0 para terminar): "))

    if cantidad > 0:
        promedio = total / cantidad
    else:
        promedio = 0

    print("\n----- REPORTE DE VENTAS -----")
    print("Cantidad de ventas:", cantidad)
    print("Total vendido: $", total)
    print("Promedio por venta: $", round(promedio, 2))

    if venta_mayor:
        print("Venta de $1,000 o más: Sí")
    else:
        print("Venta de $1,000 o más: No")
if __name__ == "__main__":
    ejecutar()