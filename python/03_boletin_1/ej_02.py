## importa palabras y las muestra en bloques y frecuencia
def carga_palabras():
    try:
        palabras_frecuencia = {}
        with open("C:/Users/lorente.alalv24_tria/Desktop/dam-sge/python/03_boletin_1/palabras.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                palabra = linea.strip()
                if palabra in palabras_frecuencia:
                    palabras_frecuencia[palabra] += 1
                else:
                    palabras_frecuencia[palabra] = 1
        return palabras_frecuencia
    except FileNotFoundError:
        print("El archivo palabras.txt no se encuentra en el directorio.")
        return {}

def mostrar_palabras(palabras_frecuencia):
    if not palabras_frecuencia:
        print("No hay palabras para mostrar.")
        return
    
    palabras_lista = list(palabras_frecuencia.items())
    for i in range(0, len(palabras_lista), 20):
        
        for palabra, frecuencia in palabras_lista[i:i+20]:
            print(f"{palabra}: {frecuencia}")
        
        if i + 20 < len(palabras_lista):
            input("Presiona Enter para ver más...")

def menu():
    palabras_frecuencia = {}
    
    while True:
        print("\nMenú de opciones ej2:")
        print("[1] – Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            palabras_frecuencia = carga_palabras()
            print(f"Se han importado {len(palabras_frecuencia)} palabras clave únicas.")
        
        elif opcion == "2":
            mostrar_palabras(palabras_frecuencia)
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

##ejecutar
if __name__ == "__main__":
    menu()
