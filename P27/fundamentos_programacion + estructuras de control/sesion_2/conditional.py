# numero = input("Escribe un numero")

# if 5 < 0:
#     print("procesando ...")
#     print("5 es un numero positivo")
#     print("finalizado")

# if 5 > 0:
#     print("5 no es un numero positivo")

numero = input("Write a number: ")

#  numero = "7"
#  not True
if not numero.isdigit():
    print("Ud ingreso algo no valido")

else:
    numero = float(numero)

    if numero == 0:
        print("procesando...")
        print("Es igual a 0")
        print("finalizado")

    if numero > 0:
        print("procesando...")
        print("El número es positivo")
        print("finalizado")

    if numero < 0:
        print("procesando...")
        print("El número es negativo")
        print("finalizado")
