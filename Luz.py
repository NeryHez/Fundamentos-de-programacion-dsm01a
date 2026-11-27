def ejecutar():

    TARIFA = 2.50
    CUOTA_FIJA = 40

    def calcular_consumo(anterior, actual):
        consumo = actual - anterior
        return consumo

    def calcular_importe(consumo):
        importe = (consumo * TARIFA) + CUOTA_FIJA
        return importe

    def clasificar_consumo(consumo):
        if consumo < 50:
            return "Bajo"
        elif consumo <= 150:
            return "Medio"
        else:
            return "Alto"

    def mostrar_recibo(anterior, actual, consumo, importe):
        print("\n===== RECIBO DE ELECTRICIDAD =====")
        print("Lectura anterior:", anterior, "kWh")
        print("Lectura actual:", actual, "kWh")
        print("Consumo:", consumo, "kWh")
        print("Tarifa: $", TARIFA)
        print("Cuota fija: $", CUOTA_FIJA)
        print("Clasificacion:", clasificar_consumo(consumo))
        print("Importe a pagar: $", format(importe, ".2f"))
        print("=================================")

    print("Calculadora de consumo")

    anterior = float(input("Ingresa la lectura anterior: "))
    actual = float(input("Ingresa la lectura actual: "))

    if anterior < 0 or actual < 0:
        print("Error: Las lecturas no pueden ser negativas.")

    elif actual < anterior:
        print("Error: La lectura actual no puede ser menor que la anterior.")

    else:
        consumo = calcular_consumo(anterior, actual)
        importe = calcular_importe(consumo)

        mostrar_recibo(anterior, actual, consumo, importe)
if __name__ == "__main__":
    ejecutar()