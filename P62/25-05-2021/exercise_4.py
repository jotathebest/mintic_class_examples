# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(long_str, short_str):
    counter = 0
    for l in range(0, len(long_str)):
        if short_str ==  long_str[l:l + len(short_str)]:
            counter += 1

    return counter

# Miguel

def busqueda(a,b):
    long_1 = len(a)
    long_2 = len(b)
    resta = long_1 - long_2 + 1
    contador = 0
    for j in range(0, resta):
        comparacion = ""
        for i in range(j, long_2 + j):
            comparacion += a[i]
        if comparacion == b:
            contador += 1

    print(f"Se encuentra la ´frase 2´ en la ´frase 1´ {contador} veces.")

frase1 = input("Inserte la cadena de texto base: ")
frase2 = input("Inserte la cadena de texto a buscar: ")
busqueda(frase1, frase2)

# Eduardo

def comparar_cadena(CadenaLarga,CadenaCorta):
    while len(CadenaLarga)>200 or len(CadenaCorta)>len(CadenaLarga):
        CadenaLarga=input('ingrese cadena de texto para anlizar:\n')
        CadenaCorta=input('ingrese Cadena corta de texto: \n')
    letras1=len(CadenaLarga)
    letras2=len(CadenaCorta)
    letras3=len(CadenaLarga.replace(CadenaCorta,''))
    numero_repeticiones=int((letras1-letras3)/letras2)
    print(f'La cadena de texto "{CadenaCorta}" se repite {numero_repeticiones} veces en "{CadenaLarga}"') 
        
Cadena1=input('ingrese cadena de texto para anlizar:\n')
Cadena2=input('ingrese Cadena corta de texto: \n')
comparar_cadena(Cadena1,Cadena2) 
