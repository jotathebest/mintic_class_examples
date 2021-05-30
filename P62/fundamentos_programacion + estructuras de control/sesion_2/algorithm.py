import time

time.sleep(0.1)

number = input("Qué número? ")

if not number.lstrip("-").isdigit():
    print("Entrada no valida, no pusiste numero")
else:
    number = float(number)

    # if <condition>:
    #     <algorithm>
    if number == 0:
        print("Es cero")

    if number > 0:
        print("Es positivo")

    if number < 0:
        print("Es negativo")

    # if number > 0:
    #     print("Es positivo")
    # else:
    #     print("Es negativo")
