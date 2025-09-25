from homework import helper
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    data=helper.loadfile()
    lines=helper.mapper(data,map_line)
    lines=helper.shuffle_sort(lines,False, lambda x: x[0])
    lines=helper.reducer(lines)
    lines=expand(lines)
    return lines

def expand(x:list[tuple]):
    result=[]
    for k,v in x:
        v=list(v)
        result.append((k,v))
    return result


def preprocess_line(x:list[str]):
    x=x[:2]
    return [(int(x[1]),x[0])]

def map_line(x:list[str]):
    x=preprocess_line(x)
    return x
