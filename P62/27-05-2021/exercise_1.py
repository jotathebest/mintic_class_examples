# Ud ha sido encargado de crear un sistema que sirva cómo insumo para recurso humano
# en aras de encontrar posibles problemas de salud dentro de los empleados,así cómo
# procesamiento de datos basado en fecha de ingreso en otro script en el cual no participas.
# Para esto, se le proporcionan las siguientes listas:

# 1. Una lista con la edad de los empleados
# 2. Una lista con los nombres del empleado
# 3. Una lista con la fecha de ingreso del empleado en formato mes/dia/año hora:minuto AM/PM
# 4. Una lista con el índice de masa corporal
# 5. Una lista que indica si la persona tiene o no comorbilidades

# El indice de masa corporal responde a lo siguiente
# Composición corporal 	    Índice de masa corporal (IMC)
# Peso inferior al normal 	    Menos de 18.5
# Normal                  	    18.5 – 24.9
# Peso superior al normal 	    25.0 – 29.9
# Obesidad 	                    Más de 30.0

# Problema:
# Tu script debe entregar una lista de diccionarios, con las siguientes llaves:
# 1. name que guardará el nombre completo de la persona
# 2. date que tendrá que guardar la fecha de entrada en formato
# año-mes(en letras, completo)-dia hora(formato militar):minuto
# 3. corporal_comp que guardará la composicion corporal del IMC
# 4. risk que guardara un booleano, en verdadero, si se cumple:
#     a. Que la composicion corporal no sea normal
#     b. Que tenga comorbilidades
#     c. Que su edad sea mayor a 45 años
# 5. age con la edad de la persona

result = [
    {
        "name": "jose garcia",
        "age": 30,
        "risk": False,
        "date": "2020-March-05 23:59",
        "corporal_comp": "Normal",
    }
]

# los scripts de abajo serviran para que tengas listas de prueba
import random
import time


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, "%m/%d/%Y %I:%M %p", prop)


age = [random.randint(18, 65) for i in range(1, 50)]
names = [
    random.choice(["jose", "wendy", "betsy", "carolina", "gonzalo"])
    + " "
    + random.choice(["garcia", "delgado", "martinez", "jaimes", "riveros"])
    for i in range(1, 50)
]
imc = [round(random.random() * 100, 2) for i in range(1, 50)]

begin_date = [
    random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())
    for i in range(1, 50)
]

comorbilities = [random.choice([True, False]) for i in range(1, 50)]

print(age, names, imc, begin_date, comorbilities, sep="\n")
