import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict

##creacion de una tupla con nombre para los avistamientos
# Avistamiento = namedtuple('Avistamiento','fechahora, cuidad, estado, forma, duracion, comentarios, latitud, longitud')


# def lee_avistamientos(fichero):
#     res = []
#     with open (fichero, encoding='utf-8') as f:
#         lector = csv.reader(f)
#         next(lector)
#         for x in lector:
#             fecha_hora= x[0]
#             fechahora = datetime.strptime(fecha_hora, "23/04/22 13:34")
#             ciudad = x[1]
#             estado = x[2]
#             forma = x[3]
#             duracion = int (x[4])
#             comentarios = x[5]
#             latitud = float (x[6])
#             longitud = float (x[7])
#             tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
#             res.append(tupla)
#         return res
    
# ejercicio 1
def lee_avistamientos(fichero):
    avistamientos = []
    
    with open(fichero, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # combina fecha y hora y convertir a objeto datetime
            fecha_hora = datetime.strptime(row['fecha'] + ' ' + row['hora'], '%Y-%m-%d %H:%M')
            avistamientos.append((
                fecha_hora,
                row['ciudad'],
                row['estado'],
                row['forma'],
                int(row['duracion']),  
                row['descripcion'],
                float(row['latitud']),  # convertir latitud a float
                float(row['longitud'])   
            ))

    # ordenar la lista de tuplas por fecha y hora
    avistamientos.sort(key=lambda x: x[0])
    
    return avistamientos

# ejercicio 2
def duracion_total(registros, estado):
    total_duracion = 0
    
    for registro in registros:
        # comprobar si el estado del registro coincide con el estado proporcionado
        if registro[2].upper() == estado.upper():  # comparar sin importar mayus
            total_duracion += registro[4]  # sumar la duracion (índice 4 en la tupla registro)
    
    return total_duracion

# ejercicio 3
def comentario_mas_largo(registros, anyo, palabra):
    comentario_largo = ""
    avistamiento_mas_largo = None

    for registro in registros:
        fecha_hora = registro[0]
        comentario = registro[5]

        # Filtrar por año y verificar si la palabra está en el comentario
        if fecha_hora.year == anyo and palabra.lower() in comentario.lower():
            # Comprobar si el comentario actual es más largo que el anterior
            if len(comentario) > len(comentario_largo):
                comentario_largo = comentario
                avistamiento_mas_largo = registro

    return avistamiento_mas_largo



                        