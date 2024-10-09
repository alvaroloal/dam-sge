import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict
import calendar

# Clase Avistamiento con sus respectivos atributos
class Avistamiento:
    def __init__(self, fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud):
        self.fechahora = fechahora
        self.ciudad = ciudad
        self.estado = estado
        self.forma = forma
        self.duracion = duracion
        self.comentarios = comentarios
        self.latitud = latitud
        self.longitud = longitud

#  para leer avistamientos desde un archivo CSV
def lee_avistamientos(fichero):
    avistamientos = []
    
    with open(fichero, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  
        
        for fila in lector_csv:
            print(fila)  
            if len(fila) < 8:  
                print(f"Fila incompleta: {fila}")
                continue
            
            try:
                # formato de fecha a 'mes/día/año'
                fechahora = datetime.strptime(fila[0], '%m/%d/%Y %H:%M')
                ciudad = fila[1]
                estado = fila[2]
                forma = fila[3]
                duracion = int(fila[4])
                comentarios = fila[5]
                latitud = float(fila[6])
                longitud = float(fila[7])
                
                # crear una instancia de Avistamiento
                avistamiento = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
                avistamientos.append(avistamiento)
            except ValueError as e:
                print(f"Error al procesar fila: {fila}, Error: {e}")
    
    # ordenar por fecha y hora
    avistamientos.sort(key=lambda x: x.fechahora)
    
    return avistamientos

# funcion que calcula la duración total de avistamientos en un estado dado
def duracion_total(registros, estado):
    duracion = 0
    for avistamiento in registros:
        if avistamiento.estado.lower() == estado.lower():
            duracion += avistamiento.duracion
    return duracion

# prueba de la función duracion_total
registros = [
    Avistamiento(datetime(2024, 1, 1, 0, 0), 'Nueva York', 'activo', 'ovni', 10, 'sin comentarios', 40.7128, -74.0060),
    Avistamiento(datetime(2024, 1, 2, 0, 0), 'Los Ángeles', 'inactivo', 'platillo', 5, 'sin comentarios', 34.0522, -118.2437)
]


# llamar a la funcion duracion_total
duracion_in = duracion_total(registros, 'activo')
print(f'Duración total de avistamientos "activo": {duracion_in}')


# funcion que encuentra el comentario más largo de un avistamiento en un año determinado que contenga una palabra específica
def comentario_mas_largo(registros, anyo, palabra):
    max_avistamiento = None
    max_longitud_comentario = 0
    
    for avistamiento in registros:
        # Filtrar por año
        if avistamiento.fechahora.year == anyo:
            # Filtrar si el comentario contiene la palabra (insensible a mayúsculas)
            if palabra.lower() in avistamiento.comentarios.lower():
                longitud_comentario = len(avistamiento.comentarios)
                
                # Verificar si es el comentario más largo
                if longitud_comentario > max_longitud_comentario:
                    max_longitud_comentario = longitud_comentario
                    max_avistamiento = avistamiento
    
    return max_avistamiento


# funcion que indexa las formas de avistamientos por mes
def indexa_formas_por_mes(registros):
    formas_por_mes = defaultdict(set)
    
    for registro in registros:
        mes_nombre = calendar.month_name[registro.fechahora.month]  # para obtener el nombre del mes
        formas_por_mes[mes_nombre].add(registro.forma)  # añadir la forma del avistamiento al mes correspondiente
    
    return dict(formas_por_mes)


# funcion que filtra avistamientos por un rango de fechas
def avistamientos_fechas(registros, fecha_inicial=None, fecha_final=None):
    if fecha_inicial is None and fecha_final is None:
        registros_filtrados = registros
    elif fecha_inicial is None:
        registros_filtrados = [r for r in registros if r.fechahora <= fecha_final]
    elif fecha_final is None:
        registros_filtrados = [r for r in registros if r.fechahora >= fecha_inicial]
    else:
        registros_filtrados = [r for r in registros if fecha_inicial <= r.fechahora <= fecha_final]
    
    # Ordenar por fecha de forma descendente
    registros_ordenados = sorted(registros_filtrados, key=lambda r: r.fechahora, reverse=True)
    
    return registros_ordenados


# funcion que encuentra la hora con más avistamientos
def hora_mas_avistamientos(registros):
    horas = [registro.fechahora.hour for registro in registros]
    contador_horas = Counter(horas)
    return contador_horas.most_common(1)[0][0]


# funcion que devuelve un diccionario con la longitud media de los comentarios por estado
def dicc_estado_longitud_media_comentario(registros):
    longitudes_por_estado = defaultdict(list)
    
    # longitd de los comentarios por estado
    for registro in registros:
        longitudes_por_estado[registro.estado].append(len(registro.comentarios))
    
    # media de longitud por estado
    longitud_media_por_estado = {estado: sum(longitudes)/len(longitudes) 
                                 for estado, longitudes in longitudes_por_estado.items()}
    
    return longitud_media_por_estado
