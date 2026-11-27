def ejecutar():

    print("Productos")

    producto1 = input("Nombre del producto 1: ")
    precio1 = float(input("Precio: "))
    cantidad1 = int(input("Cantidad: "))

    producto2 = input("Nombre del producto 2: ")
    precio2 = float(input("Precio: "))
    cantidad2 = int(input("Cantidad: "))

    producto3 = input("Nombre del producto 3: ")
    precio3 = float(input("Precio: "))
    cantidad3 = int(input("Cantidad: "))

    subtotal1 = precio1 * cantidad1
    subtotal2 = precio2 * cantidad2
    subtotal3 = precio3 * cantidad3

    subtotal_general = subtotal1 + subtotal2 + subtotal3

    iva = subtotal_general * 0.16
    total = subtotal_general + iva

    print("\n----- Ticket de compra -----")
    print(producto1, "$", subtotal1)
    print(producto2, "$", subtotal2)
    print(producto3, "$", subtotal3)

    print("Subtotal: $", subtotal_general)
    print("IVA (16%): $", iva)
    print("Total: $", total)
if __name__ == "__main__":
    ejecutar()