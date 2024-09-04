renta = int(input("cual es su renta anual"))
if renta < 1000000:
    print("el valor del pago de su impositivo es del 5%")
elif renta >= 1000000 and renta < 2000000:
    print("el valor del pago del impositivo es del 15%")
elif renta >= 2000000 and renta < 3500000:
    print("el valor del pago del impositovo es del 20%")
elif renta >=3500000 and renta < 6000000:
    print("el valor del pago del impositivo es del 30%")
elif renta >= 6000000:
    print("el valor del pago del impositivo es del 45%")
