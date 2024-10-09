def carga_palabras():
    """Carga palabras clave desde un archivo y devuelve una lista de ellas."""
    palabras = []
    try:
        with open('C:/Users/alvaro/proyectos/dam-sge/python/03_boletin_1/palabras.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras.append(linea.strip())
    except FileNotFoundError:
        print("El archivo 'palabras.txt' no se encontró.")
    return palabras

def mostrar_palabras(palabras):
    """Muestra las palabras clave de 20 en 20."""
    for i in range(0, len(palabras), 20):
        # Muestra un grupo de 20 palabras
        for palabra in palabras[i:i + 20]:
            print(palabra)
        # Espera a que el usuario presione enter para continuar
        input("Presiona Enter para ver más palabras...")

def main():
    palabras = []
    
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
