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
# Normal                  	    Mayor o igual a 18.5 – menor a 25
# Peso superior al normal 	    Mayor o igual a 25.0 – menor a 30
# Obesidad 	                    Máyor o igual de 30.0

# Problema:
# Tu script debe entregar una lista de diccionarios, con las siguientes llaves:
# 1. name que guardará el nombre completo de la persona
# 2. date que tendrá que guardar la fecha de entrada en formato
# año-mes(en letras, completo)-dia hora(formato militar):minuto
# 3. corporal_comp que guardará la composicion corporal del IMC
# 4. risk que guardara un booleano, en verdadero, si se cumple todas las siguientes condiciones:
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
import datetime


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

print(age, names, imc, begin_date, comorbilities, sep="\n\n")

# --- funciones
# procesar el imc y que entregue la composición corporal
# args --> imc: float
# return --> corporal_comp: str

# El indice de masa corporal responde a lo siguiente
# Composición corporal 	    Índice de masa corporal (IMC)
# Peso inferior al normal 	    Menos de 18.5
# Normal                  	    Mayor o igual a 18.5 – menor a 25
# Peso superior al normal 	    Mayor o igual a 25.0 – menor a 30
# Obesidad 	                    Máyor o igual de 30.0
def get_corporal_comp(imc: float):
    """Retorna la composicion corporal dado un indice de masa

    Args:
        imc (float): Indice de masa corporal

    Returns:
        str: Composicion corporal
    """
    if imc < 18.5:
        return "Peso inferior al normal"
    if imc >= 18.5 and imc < 25:
        return "Normal"
    if imc >= 25 and imc < 30:
        return "Peso superior al normal"
    if imc >= 30:
        return "Obesidad"


# procesar el riesgo
# args --> corporal_comp:str, age:int, comorbility:bool
# return --> risk: bool

# risk que guardara un booleano, en verdadero, si se cumple todas las siguientes condiciones:
#     a. Que la composicion corporal no sea 'Normal'
#     b. Que tenga comorbilidades
#     c. Que su edad sea mayor a 45 años
def get_risk(corporal_comp: str, age: int, has_comorbilities: bool):
    return (
        True if corporal_comp != "Normal" and has_comorbilities and age > 45 else False
    )


# procesar la fecha
# args --> fecha: str [formato mes/dia/año hora:minuto AM/PM] 06/28/2008 02:13 AM
# return --> fecha:str [año-mes(en letras, completo)-dia hora(formato militar):minuto]
# strptime() ---> leer fechas
# strftime() --> imprimir con formato
def convert_date(date_str: str):
    date = datetime.datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")
    new_date = date.strftime("%Y-%B-%d %H:%M")
    return new_date


# funcion para ordenar los datos
# funcion que me retorne un diccionario para una persona con las llaves name, risk, date, age, corporal_comp
# args --> name:str, date:str, age:int, corporal_comp:str, risk: bool
# return --> person_dict: {}
#  {
#         "name": "jose garcia",
#         "age": 30,
#         "risk": False,
#         "date": "2020-March-05 23:59",
#         "corporal_comp": "Normal",
#     }


def build_personal_dict(name: str, date: str, age: int, corporal_comp: str, risk: bool):

    personal_dict = {
        "name": name,
        "date": date,
        "age": age,
        "corporal_comp": corporal_comp,
        "risk": risk,
    }

    return personal_dict


# funcion para iterar las listas
# reciba datos
# args --> ages: list, names: list, begin_date: list, comorbilities: list, imc: list
# return --> result_total: list

# crear un arreglo para guardar resultados
# recorrer las listas
# extraer la siguiente informacion: personal_age, personal_date, personal_name, personal_comor, personal_imc
# extraer personal_composition_corp --> get_corporal_comp(personal_imc)
# extraer risk --> get_risk()
# extraer new_date --> convert_date()
# create personal_dict --> build_personal_dict()
# agregar a los resultados el diccionario personal


# --- Ideas de iteración y ordenamiento ---
# un diccionario
# dato dentro de la funcion que nos arroje el indice dentro de las listas para agregar las llaves
# zip
# crear listas con riesgo y fecha para reemplazarlos dentro del diccionario
