
##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##

cadena = input("Ingrese una letra y dos números separados por comas: ")
cadena.split(",")
lista= cadena.split(",")
if (lista[1])>(lista[2]):
    print (f" Max: {lista[1]}, Min: {lista[2]}")
if (lista[2])>(lista[1]):
    print (f" Max: {lista[2]}, Min: {lista[1]}")
else:
    print ("Los dos números ingresados son iguales")

##
## Por cada fila , obtenga el valor numérico mas pequeño y el valor mas grande.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
