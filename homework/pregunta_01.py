import csv
from homework import helper
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """

    data=helper.loadfile("files\\input\\\data.csv")
    line=helper.mapper(data,map_line)
    
    return sum(line)



def preprocess_line(x:list):
    x=x[1]
    return [int(x)]

def map_line(data:list):
    x=preprocess_line(data)
    return x

