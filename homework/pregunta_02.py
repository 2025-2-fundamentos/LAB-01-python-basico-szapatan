import csv
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    rta={}
    with open('files/input/data.csv',newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            row1=row[0].split('\t')[:2]
            if row1[0] in rta:
                rta[row1[0]]+=1
            else:
                rta[row1[0]]=1
    data=[]
    for k,y in rta.items():
        data.append((k,y))
    data.sort(key=lambda x: x[0])
    return data
