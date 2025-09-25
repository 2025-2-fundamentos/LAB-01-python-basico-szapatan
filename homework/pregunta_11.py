from homework import helper
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data=helper.loadfile()
    lines=helper.mapper(data,map_line)
    lines=helper.shuffle_sort(lines,False, lambda x: x[0])
    lines=helper.reducer(lines)
    lines=dict(lines)
    return lines
    


def preprocess_line(x:list[str]):
    result=[]
    n=int(x[1])
    x=x[3]
    line=x.split(",")
    for i in line:
        result.append((i,n))
    return result

def map_line(x:list[str]):
    x=preprocess_line(x)
    return x