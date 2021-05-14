
##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,5,7
## E,9,1
##

# Solution 1
my_str = "A,9,1"

# my_list --> ["A", "9", "1"]
my_list = my_str.split(",")

max = my_list[1] if int(my_list[1]) > int(my_list[2]) else my_list[2]
min = my_list[1] if int(my_list[1]) < int(my_list[2]) else my_list[1]

print(f"max is {max} , min is {min}")

# Solution 2

my_str = "A,9,1"

# my_list --> ["A", "9", "1"]
my_list = my_str.split(",")

if my_list[1] >= my_list[2]:
    print("max is {my_list[1]}, min is {my_list[2]}")
else:
    print("max is {my_list[2]}, min is {my_list[1]}")

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
