import Cotizador
import Museo
import Luz
import Vetntas

opcion = -1

while opcion != 0:

    print("\n===== Menu de act=====")
    print("1. Cotizador de productos")
    print("2. Entrada al museo")
    print("3. Calculadora de consumo electrico")
    print("4. Registro de ventas")
    print("0. Salir")

    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        Cotizador.ejecutar()

    elif opcion == 2:
        Museo.ejecutar()

    elif opcion == 3:
        Luz.ejecutar()

    elif opcion == 4:
        Vetntas.ejecutar()

    elif opcion == 0:
        print("Saliendo del programa...")

    else:
        print("Opcion no valida")

print("Programa finalizado")