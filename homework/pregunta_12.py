from homework import helper
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data=helper.loadfile()
    lines=helper.mapper(data,map_line)
    lines=helper.shuffle_sort(lines,False, lambda x: x[0])
    lines=helper.reducer(lines)
    lines=dict(lines)
    return lines
    


def preprocess_line(x:list[str]):

    n=x[0]
    x=x[4]
    line=x.split(",")
    s=0
    for i in line:
        k=i.split(":")
        s+=int(k[1])

    return [(n,s)]

def map_line(x:list[str]):
    x=preprocess_line(x)
    return x