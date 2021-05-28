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
import datetime


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, "%m/%d/%Y %I:%M %p", prop)


ages = [random.randint(18, 65) for i in range(1, 50)]
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

# print(age, names, imc, begin_date, comorbilities, sep="\n")


def rrhh_inform(ages, names, imc, begin_date, comorbilities):
    # algorithm
    return [
        {
            "name": "jose garcia",
            "age": 30,
            "risk": False,
            "date": "2020-March-05 23:59",
            "corporal_comp": "Normal",
        }
    ]


# funcion para hallar el composicion corporal
# args --> imc: float
# return --> Composición_corporal: str

# El indice de masa corporal responde a lo siguiente
# Composición corporal 	    Índice de masa corporal (IMC)
# Peso inferior al normal 	    Menos de 18.5
# Normal                  	    18.5 – 24.9
# Peso superior al normal 	    25.0 – 29.9
# Obesidad 	                    Más de 30.0


def get_corporal_composition(imc: float):
    """
    Esta funcion devuelve la composicion corporal dado un indice de masa corporal
    """
    imc = round(imc, 1)
    if imc < 18.5:
        return "Peso inferior al normal"
    if imc >= 18.5 and imc <= 24.9:
        return "Normal"
    if imc >= 25 and imc <= 29.9:
        return "Peso superior al normal"
    if imc >= 30:
        return "Obesidad"


# funcion para definir el riesgo
# args --> composicion_corporal:str, comorbilidades:bool, edad:int
# return --> risk:bool

# risk que guardara un booleano, en verdadero, si se todas se cumplen:
#     a. Que la composicion corporal no sea normal
#     b. Que tenga comorbilidades
#     c. Que su edad sea mayor a 45 años


def get_risk(corporal_comp: str, has_comorbilities: bool, age: int):
    return (
        True if corporal_comp != "Normal" and has_comorbilities and age > 45 else False
    )


# funcion para cambiar el formato de la fecha
# args --> fecha:str [formato mes/dia/año hora:minuto AM/PM]
# return --> fecha:str [formato año-mes(en letras, completo)-dia hora(formato militar):minuto]


def convert_date(date_str):
    date = datetime.datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")
    return date.strftime("%Y-%B-%d %H:%M")


# print(convert_date("06/28/2008 02:13 AM"))

# construir diccionario
# args --> composicion_corporal: str, risk: bool, name: str, age: int, fecha: str
# return --> result:dict
# dict:
#  {
#     "name": "jose garcia",
#     "age": 30,
#     "risk": False,
#     "date": "2020-March-05 23:59",
#     "corporal_comp": "Normal",
# }


def build_person_dict(corporal_comp: str, risk: bool, name: str, age: int, date: str):
    person_dict = {
        "name": name,
        "age": age,
        "risk": risk,
        "date": date,
        "corporal_comp": corporal_comp,
    }
    return person_dict


# emparejar cada item de cada lista en un diccionario
# args --> ages, names, imc, begin_date, comorbilities
# return --> result_total:list


def process_data(
    ages: list, names: list, imc: list, begin_date: list, comorbilities: list
):
    result = []
    # iterates the names list with enumerate --> index, name
    # saves in 4 variables the following information: age, imc, begin_date, comorbility
    # Create the corporal_comp variable --> get_corporal_comp(imc)
    # Creates the risk variable --> get_risk(corporal_comp, comorbility, age)
    # Creates the new_date variable --> convert_date(begin_date)
    # Creates the person_dict variable --> build_person_dict(risk, new_date, age, name, corporal_comp)
    # Adds the person_dict to result

    for index, name in enumerate(names):
        age_person = ages[index]
        imc_person = imc[index]
        date_person = begin_date[index]
        comorbility_person = comorbilities[index]

        corporal_comp = get_corporal_composition(imc_person)
        risk = get_risk(corporal_comp, comorbility_person, age_person)
        new_date_person = convert_date(date_person)

        personal_dict = build_person_dict(
            corporal_comp, risk, name, age_person, new_date_person
        )

        result.append(personal_dict)

    return result


print(process_data(ages, names, imc, begin_date, comorbilities))
