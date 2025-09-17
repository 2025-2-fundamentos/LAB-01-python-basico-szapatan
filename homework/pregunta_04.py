import csv
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    rta={}
    with open('files/input/data.csv',newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:

            row1=row[0].split('\t')[2].split('-')
            print(row1)
            if row1[1] in rta:
                rta[row1[1]]+=1
            else:
                rta[row1[1]]=1
    data=[]
    for k,y in rta.items():
        data.append((k,y))
    data.sort(key=lambda x: x[0])
    return data