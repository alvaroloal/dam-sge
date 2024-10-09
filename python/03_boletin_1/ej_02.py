import os

def carga_palabras():
    """Carga palabras clave desde un archivo y devuelve un diccionario con la palabra y su frecuencia."""
    palabras = {}
    archivo_nombre = 'palabras.txt'
    ##C:\Users\alvaro\proyectos\dam-sge\python\03_boletin_1\palabras.txt
    
    # Mostrar el directorio actual y la ruta absoluta del archivo
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Intentando abrir el archivo '{archivo_nombre}' en {os.path.abspath(archivo_nombre)}...")
    
    try:
        with open(archivo_nombre, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabra = linea.strip()  # Eliminar espacios y saltos de línea
                if palabra:  # Comprobar que la línea no esté vacía
                    if palabra in palabras:
                        palabras[palabra] += 1  # Incrementar la frecuencia si la palabra ya existe
                    else:
                        palabras[palabra] = 1  # Añadir la palabra con frecuencia 1
        print(f"Se han cargado {len(palabras)} palabras clave (contando repeticiones).")
    except FileNotFoundError:
        print(f"El archivo '{archivo_nombre}' no se encontró. Asegúrate de que exista en {os.path.abspath(archivo_nombre)}.")
    
    return palabras

def mostrar_palabras(palabras):
    """Muestra las palabras clave y su frecuencia de 20 en 20."""
    palabras_lista = list(palabras.items())  # Convertir el diccionario a una lista de tuplas (palabra, frecuencia)
    
    for i in range(0, len(palabras_lista), 20):
        # Mostrar un grupo de 20 palabras junto con su frecuencia
        for palabra, frecuencia in palabras_lista[i:i + 20]:
            print(f"{palabra}: {frecuencia} veces")
        input("Presiona Enter para ver más palabras...")

def main():
    palabras = {}
    
    while True:
        print("\nMenú de opciones:")
        print("[1] – Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            palabras = carga_palabras()
            if palabras:
                print(f"{len(palabras)} palabras clave cargadas.")
        elif opcion == '2':
            if palabras:
                mostrar_palabras(palabras)
            else:
                print("No hay palabras clave cargadas. Por favor, importa primero.")
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona otra.")

if __name__ == "__main__":
    main()
