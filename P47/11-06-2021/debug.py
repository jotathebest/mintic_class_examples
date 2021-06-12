import pdb

def sumar(a, b):
    pdb.set_trace()
    print("voy a sumarrr")
    result = a + b
    restar(a, b)
    return result


def restar(a, b):
    print("voy a restarrr")
    return a - b

sumar(3, 4)
