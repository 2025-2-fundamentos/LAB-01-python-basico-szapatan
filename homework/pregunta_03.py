import csv
from homework import helper
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    data=helper.loadfile()
    lines=helper.mapper(data,map_line)
    lines=helper.shuffle_sort(lines,False, lambda x: x[0])
    lines=helper.reducer(lines)
    return lines
    

def preprocess_line(x:list[str]):
    x=x[:2]
    return [(x[0],int(x[1]))]

def map_line(x:list[str]):
    x=preprocess_line(x)
    return x