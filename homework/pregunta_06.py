from homework import helper

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    data=helper.loadfile()
    lines=helper.mapper(data,map_line)
    lines=helper.shuffle_sort(lines,False, lambda x: x[0])
    lines=helper.reducer(lines,True)
    lines=invert(lines)
    return lines
    
def invert(x:list[tuple]):
    result=[]
    for k,n_max,n_min in x:
        result.append((k,n_min,n_max))
    return result

def preprocess_line(x:list[str]):
    result=[]
    x=x[4]
    line=x.split(",")
    for i in line:
        k=i.split(":")
        result.append((k[0],int(k[1])))
    return result

def map_line(x:list[str]):
    x=preprocess_line(x)
    return x
