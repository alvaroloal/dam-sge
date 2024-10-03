from ufos import *

# Test de la función lee_avistamientos
avistamientos  = lee_avistamientos('C:\\Users\\alvaro\\proyectos\\dam-sge\\python\\Ufos\\data\\ovnis.csv')

#Test de la función duracion_total
total_duracion_estado = duracion_total(avistamientos, 'CA')  # ej:California
print(f'Duración total de avistamientos en CA: {total_duracion_estado} segundos')

    
# Test de la función comentario_mas_largo
avistamiento_largo = comentario_mas_largo(avistamientos, 2015, 'ufo')
if avistamiento_largo:
    print(f'El avistamiento con el comentario más largo de 2015 incluyendo la palabra "ufo" es:\n{avistamiento_largo}')
else:
    print('No se encontraron avistamientos que cumplan con los criterios.')



# Test de la función avistamientos_fechas



# Test de la función hora_mas_avistamientos










# # Test de la función formas_estados
#  conjunto_estados = {'in', 'nm', 'pa', 'wa'}
#  print("Número de formas distintas observadas en los estados {}: {}"
#       .format(', '.join(conjunto_estados), formas_estados(avistamientos, conjunto_estados)))
#  print()
 
# # Test de la función avistamiento_mayor_duracion
# forma = 'circle'
# print("Avistamiento de forma \'{}\' de mayor duración: {}"
#       .format(forma, avistamiento_mayor_duracion(avistamientos, forma)))
# print()
# 
# 
# #Test de la función avistamiento_cercano_mayor_duracion
# coordenadas = (40.2, -85.4)
# radio = 0.5
# duracion, comentario = avistamiento_cercano_mayor_duracion(avistamientos, coordenadas)
# print("Duración del avistamiento más largo en un entorno de radio {} sobre las coordenadas {}: {} segundos"
#       .format(radio, coordenadas, duracion))
# print("Comentario:", comentario)
# print()
# 
# # Test de la función porc_avistamientos_por_forma
# porcentajes = porc_avistamientos_por_forma(avistamientos)
# print("Porcentajes de avistamientos de las distintas formas (sólo se muestran las formas 'changing', 'chevron', 'cigar' y 'circle'):")
# for forma in ['changing', 'chevron', 'cigar', 'circle']:
#     print("\t{}: {:.2f}%".format(forma, porcentajes[forma]))
# print ()
# 
# 
# # Test de la función coordenadas_mas_avistamientos
# print("Coordenadas enteras de la región en la que se observaron más avistamientos:", 
#       coordenadas_mas_avistamientos(avistamientos))    
# print ()
# 
# 
# 
# 
# 
# # Test de la función formas_por_mes
# indice = formas_por_mes(avistamientos)
# print("Índice de formas por mes (se muestran las formas para enero, julio y noviembre:")
# for mes in ["Enero", "Julio", "Noviembre"]:
#     print("\t{} ({} formas distintas): {}"
#           .format(mes, len(indice[mes]), ', '.join(sorted(indice[mes]))))   
# print()    
#     
# 
# # Test de la función avistamientos_mayor_duracion_por_estado
# indice = avistamientos_mayor_duracion_por_estado(avistamientos)
# print("Mostrando los 3 avistamientos de mayor duración de los estados 'in' y 'nm':")
# for estado in ['in', 'nm']:
#     print("\t", estado)
#     for a in indice[estado]:
#         print("\t\t", a) 
# =============================================================================
        

# =============================================================================
# # Test de la función numero_avistamientos_por_año
# indice = numero_avistamientos_por_año(avistamientos)
# print("Número de avistamientos por año:")
# for a in indice.keys():
#     print("\t{}: {}".format(a, indice[a]))    
# print()    
#    
# 
# # Test de la función longitud_media_comentarios_por_estado
# indice = longitud_media_comentarios_por_estado(avistamientos)
# print("Mostrando la media del tamaño de los comentarios de los avistamientos de los estados 'in','nm', 'pa' y 'wa':")
# for estado in ['in', 'nm', 'pa', 'wa']:
#      print("\t{}: {}".format(estado, indice[estado]))
# print()
# 
# # Test de la función avistamientos_cercanos_ubicacion
# coordenadas = (38.26, -77.18)
# radio = 0.1
# conjunto_av_cercanos = avistamientos_cercanos_ubicacion(avistamientos, coordenadas, radio)
# print("Avistamientos cercanos a {}: {}".format(coordenadas, conjunto_av_cercanos))    
# print()
# 
# =============================================================================

# =============================================================================
# # Test de la función avistamientos_por_fecha
# indice = avistamientos_por_fecha(avistamientos)
# print("Avistamientos por fecha (se muestran solo dos fechas):", )
# for f in [datetime(1986, 9, 18).date(), datetime(1986, 7, 20).date()]:
#     print("\t{}: {}".format(f, indice[f])) 
# print()
# =============================================================================
    

 
    
# =============================================================================
# # Test de la función num_avistamientos_por_mes
# indice = num_avistamientos_por_mes(avistamientos)
# print("Número de avistamientos por mes (sólo se muestran enero, febrero y marzo):")
# for mes in ["Enero", "Febrero", "Marzo"]:
#     print("\t{}: {}".format(mes, indice[mes]))
# print()
#     
# =============================================================================
    


# =============================================================================
# # Test de la función numero_avistamientos_fecha
# fecha = datetime(2005, 5, 1).date()
# numero_avistamientos = numero_avistamientos_fecha(avistamientos, fecha)
# print("El día {} se produjeron {} avistamientos"
#       .format(datetime.strftime(fecha, '%d/%m/%Y'), numero_avistamientos))
# =============================================================================



 

 

 





