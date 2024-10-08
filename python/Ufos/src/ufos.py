import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict
import calendar

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

    def __repr__(self):
        return (f"Avistamiento(fechahora={self.fechahora}, ciudad='{self.ciudad}', "
                f"estado='{self.estado}', forma='{self.forma}', duracion={self.duracion}, "
                f"comentarios='{self.comentarios}', latitud={self.latitud}, longitud={self.longitud})")

def lee_avistamientos(fichero):
    avistamientos = []
    
    with open(fichero, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        
        # Saltar la cabecera si existe
        next(lector_csv)
        
        for fila in lector_csv:
            # Imprimir la fila para verificar su contenido
            print(fila)  # Debugging: esto te permitirá ver si la fila tiene todos los elementos esperados
            
            # Verificar que la fila tiene suficientes columnas
            if len(fila) < 8:
                print(f"Fila incompleta: {fila}")
                continue  # Saltar filas incompletas
            
            try:
                # Descomponemos la fila en las variables correspondientes
                fechahora = datetime.strptime(fila[0], '%d/%m/%Y %H:%M')  # Cambio en el formato de fecha
                ciudad = fila[1]
                estado = fila[2]
                forma = fila[3]
                duracion = int(fila[4])
                comentarios = fila[5]
                latitud = float(fila[6])
                longitud = float(fila[7])
                
                # Creamos una instancia de Avistamiento
                avistamiento = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
                avistamientos.append(avistamiento)
            except ValueError as e:
                print(f"Error al procesar fila: {fila}, Error: {e}")
    
    # Ordenamos la lista de avistamientos por fecha y hora
    avistamientos.sort(key=lambda x: x.fechahora)
    
    return avistamientos

# ejercicio 2
def duracion_total(registros, estado):
    total_duracion = 0
    
    # Recorremos todos los registros
    for avistamiento in registros:
        if avistamiento.estado.lower() == estado.lower():  # Comparación insensible a mayúsculas
            total_duracion += avistamiento.duracion
    
    return total_duracion

#ejercicio 3
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

## ejercicio 4
def indexa_formas_por_mes(registros):
    formas_por_mes = defaultdict(set)
    
    for registro in registros:
        # Obtener el nombre del mes
        mes_nombre = calendar.month_name[registro.fechahora.month]
        # Añadir la forma del avistamiento al conjunto correspondiente al mes
        formas_por_mes[mes_nombre].add(registro.forma)
    
    return dict(formas_por_mes)

##ejercicio 5
def avistamientos_fechas(registros, fecha_inicial=None, fecha_final=None):
    if fecha_inicial is None and fecha_final is None:
        registros_filtrados = registros
    elif fecha_inicial is None:
        registros_filtrados = [r for r in registros if r.fechahora <= fecha_final]
    elif fecha_final is None:
        registros_filtrados = [r for r in registros if r.fechahora >= fecha_inicial]
    else:
        registros_filtrados = [r for r in registros if fecha_inicial <= r.fechahora <= fecha_final]
    
    # Ordenar los registros por fecha de forma descendente
    registros_ordenados = sorted(registros_filtrados, key=lambda r: r.fechahora, reverse=True)
    
    return registros_ordenados


#ejercicio 6
def hora_mas_avistamientos(registros):
    horas = [registro.fechahora.hour for registro in registros]
    contador_horas = Counter(horas)
    return contador_horas.most_common(1)[0][0]

# ejercico 7
def dicc_estado_longitud_media_comentario(registros):
    longitudes_por_estado = defaultdict(list)
    
    # Recolectar las longitudes de los comentarios por estado
    for registro in registros:
        longitudes_por_estado[registro.estado].append(len(registro.comentarios))
    
    # Calcular la media de longitud por estado
    longitud_media_por_estado = {estado: sum(longitudes)/len(longitudes) 
                                 for estado, longitudes in longitudes_por_estado.items()}
    
    return longitud_media_por_estado
