import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict

##creacion de una tupla con nombre para los avistamientos
Avistamiento = namedtuple('Avistamiento','fechahora, cuidad, estado, forma, duracion, comentarios, latitud, longitud')


def lee_avistamientos(fichero):
    res = []
    with open (fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for x in lector:
            fecha_hora= x[0]
            fechahora = datetime.strptime(fecha_hora, "23/04/22 13:34")
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int (x[4])
            comentarios = x[5]
            latitud = float (x[6])
            longitud = float (x[7])
            tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)
           
        return res
                        