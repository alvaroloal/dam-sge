import csv

def leer_fichero():
    cotizaciones = []
    with open("./ejercicios_2/cotizacion.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if all(key in row for key in ["Nombre", "Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]):
                cotizacion = {
                    "nombre": row["Nombre"],
                    "final": float(row["Final"].replace('.', '').replace(',', '.')),
                    "maximo": float(row["Máximo"].replace('.', '').replace(',', '.')),
                    "minimo": float(row["Mínimo"].replace('.', '').replace(',', '.')),
                    "volumen": float(row["Volumen"].replace('.', '').replace(',', '.')),
                    "efectivo": float(row["Efectivo"].replace('.', '').replace(',', '.'))
                }
                cotizaciones.append(cotizacion)
            else:
                print(f"Fila de la que faltan datos: {row}")
    print()
    print(f"Cotizaciones leídas: {cotizaciones}")  
    return cotizaciones

def cotizaciones_columnas(cotizaciones):
    columnas = {"final": [], "maximo": [], "minimo": [], "volumen": [], "efectivo": []}
    for cotizacion in cotizaciones:
        for key in columnas.keys():
            columnas[key].append(cotizacion[key])
    print()
    print(f"Datos por columnas: {columnas}")  
    return columnas

def crear_fichero_cotizaciones_columnas(columnas):
    with open("./ejercicios_2/cotizaciones_columnas.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        for key in columnas.keys():
            if columnas[key]:  
                writer.writerow([key, min(columnas[key]), max(columnas[key]), sum(columnas[key]) / len(columnas[key])])
            else:
                print(f"La columna {key} está vacía por lo que no se puede calcular el mínimo, el máximo y la media de las cotizaciones.") 

def menu():
    cotizaciones = leer_fichero()
    columnas = cotizaciones_columnas(cotizaciones)
    crear_fichero_cotizaciones_columnas(columnas)

menu()