
def get_max_average_price(prices_list: list):
    """Retorna el valor máximo dado una lista de precios

    Args:
        prices_list (list): Lista de precios

    Returns:
        float: valor máximo
    """

    # Algoritmo para obtener el máximo acá

    return maximo


def get_min_average_price(prices_list: list):
    """Retorna el valor mínimo dado una lista de precios

    Args:
        prices_list (list): Lista de precios

    Returns:
        float: valor mínimo
    """
    # Algoritmo para obtener el mínimo acá

    return minimo


def get_max_average_volume(volume_list: list):
    """Retorna el volumen máximo dado una lista de volumenes de venta

    Args:
        volume_list (list): Lista de volúmenes

    Returns:
        float: valor máximo
    """
    # Algoritmo para obtener el volumen máximo acá

    return volumen_maximo


def get_max_sale_date(dates_list: list, prices_list: list):
    """Retorna la fecha dónde se dió el máximo precio

    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios

    Returns:
        str: Fecha con histórico
    """
    max_price = get_max_average_price(prices_list)

    # Algoritmo para obtener el índice del máximo de la lista de precios acá

    return dates_list[max_index]


def get_min_sale_date(dates_list: list, prices_list: list):
    """Retorna la fecha dónde se dió el mínimo precio

    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios

    Returns:
        str: Fecha con histórico
    """
    min_price = get_min_average_price(prices_list)

    # Algoritmo para obtener el índice del mínimo de la lista de precios acá

    return dates_list[min_index]


def get_max_price_type(types_list: list, prices_list: list):
    """Retorna el tipo de aguacate con el máximo precio

    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios

    Returns:
        str: Fecha con histórico
    """
    max_price = get_min_average_price(prices_list)

    # Algoritmo para obtener el índice del máximo de la lista de precios acá

    return types_list[max_index]


def build_dict(prices_list, dates_list, types_list, volumes_list):
    """Función para construir el diccionario de salida

    Args:
        prices_list (list): [description]
        dates_list (list): [description]
        types_list (list): [description]
        volumes_list (list): [description]

    Returns:
        dict: Diccionario con las llaves solicitadas
    """
    max_price = get_max_average_price(prices_list)
    min_price = get_min_average_price(prices_list)
    max_volume = get_max_average_volume(volumes_list)
    max_date = get_max_sale_date(dates_list, prices_list)
    min_date = get_min_sale_date(dates_list, prices_list)
    max_type = get_max_price_type(types_list, prices_list)

    result = {
        "precio promedio maximo": max_price,
        "precio promedio minimo": min_price,
        "volumen maximo": max_volume,
        "fecha maximo promedio": max_date,
        "fecha minimo promedio": min_date,
        "tipo con maximo precio": max_type,
    }

    return result


def get_region_data(data: dict, region: str):
    """Extrae como listas, los datos de interes que son el tipo de aguacate,
       el precio promedio, las fechas y el volumen de venta

    Args:
        data (list): Diccionario con todas las llaves de datos
        region (str): region de interés para extraer

    Returns:
        (prices_list, dates_list, types_list, volumes_list) (tuple): Resultado con las listas de datos
    """
    # Listas para almacenar resultados
    types_list = []
    prices_list = []
    dates_list = []
    volumes_list = []

    # Extrae acá la información de interés, sigue el ejemplo dado
    region_data = data["region"]
    types_data = 
    prices_data = 
    dates_data = 
    volumes_data = 

    # itera los items del diccionario de region_data, extrayendo dos variables:
    # index, value. Dado que region_data es un diccionario, tendrás que usar items()

    # coloca el iterador acá

        # si el valor es igual a la region, añade a las listas los datos de interés, sigue el
        # ejemplo
            #types_list.append(types_data[index])
            

    return (prices_list, dates_list, types_list, volumes_list)


def get_general_statics(data: dict, region: str):
    # Escribe acá la instrucción para que
    # si la region NO existe dentro de las regiones de la llave "region" de data, retorne None

    prices_list, dates_list, types_list, volumes_list = get_region_data(data, region)

    result = build_dict(prices_list, dates_list, types_list, volumes_list)
    return result
