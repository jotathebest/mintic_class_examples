# def clasificacion_huevos(mi_lista):
#     huevos_AAA = 0
#     huevos_AA = 0
#     huevos_A = 0
#     huevos_BC = 0
#     for huevo in mi_lista:
#         # extrae aca el tipo de huevo con base en el peso (puedes usar una funcion para esto)
#         # incrementa el contador de la categoria del huevo respectiva

#     # conociendo el numero de huevos por categoria, calcula las bandejas por categoria (puedes usar una funcion para esto)
#     bandejas_AAA = 0
#     bandejas_AA = 0
#     bandejas_A = 0
#     bandejas_BC = 0

#     # crea el diccionario de resultados con
#     result = [{'tipo_huevo': 'AAA', 'numero_huevos': huevos_AAA, 'numero_bandejas': bandejas_AAA}
#               {'tipo_huevo': 'AA', 'numero_huevos': huevos_AA, 'numero_bandejas': bandejas_AA}
#               {'tipo_huevo': 'A', 'numero_huevos': huevos_A, 'numero_bandejas': bandejas_A}
#               {'tipo_huevo': 'BC', 'numero_huevos': huevos_BC, 'numero_bandejas': bandejas_BC}
#     ]

#     return result


def tipo_huevos(peso_huevos):
    A = 0
    AA = 0
    AAA = 0
    BC = 0
    for peso in peso_huevos:
        if peso >= 53.0 and peso < 60.0:
            A += 1
        elif peso >= 60.0 and peso < 67.0:
            AA += 1
        elif peso >= 67.0:
            AAA += 1
        elif peso < 53.0:
            BC += 1
    return (A, AA, AAA, BC)


# def cantidad_huevos()


def calcular_badejas(lista):

    BANDEJA_A = lista[0] / 30
    BANDEJA_A = int(BANDEJA_A)

    BANDEJA_AA = lista[1] / 24
    BANDEJA_AA = int(BANDEJA_AA)

    BANDEJA_AAA = lista[2] / 12
    BANDEJA_AAA = int(BANDEJA_AAA)

    BANDEJA_BC = lista[3] / 30
    BANDEJA_BC = int(BANDEJA_BC)
    return (BANDEJA_A, BANDEJA_AA, BANDEJA_AAA, BANDEJA_BC)


# print(calcular_badejas(tipo_huevos(peso_huevos)))


# print(f" tipo_huevo: A numero_huevos: {clasificacion_huevos(peso_huevos)}, numero_bandejas: {calcular_badejas(clasificacion_huevos(peso_huevos))}")


def construir_dic(peso_huevos):
    huevos_dict = {
        "tipo_huevo": tipo_huevos,
        "numero_huevos": tipo_huevos,
        "numero_bandejas": tipo_huevos,
    }
    return huevos_dict


def clasificacion_huevos(peso_huevos):

    result = []

    for huevo in peso_huevos:
        import ipdb

        ipdb.set_trace()
        tipo_huevo = tipo_huevos(peso_huevos)
        numero_huevos = tipo_huevos(peso_huevos)
        numero_bandejas = calcular_badejas(peso_huevos)

        huevos_dict = construir_dic(peso_huevos)

        result.append(huevos_dict)

    return result


peso_huevos = [46.5, 60.8, 58.7, 70.0, 49.8]
print(clasificacion_huevos(peso_huevos))
