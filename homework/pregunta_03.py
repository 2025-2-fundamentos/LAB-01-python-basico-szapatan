import csv
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
    rta={}
    with open('files/input/data.csv',newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            row1=row[0].split('\t')[:2]
            if row1[0] in rta:
                rta[row1[0]]+=int(row1[1])
            else:
                rta[row1[0]]=int(row1[1])
    data=[]
    for k,y in rta.items():
        data.append((k,y))
    data.sort(key=lambda x: x[0])
    return data
