##importa palabras y las muestra
def carga_palabras():
    try:
        with open("palabras.txt", "r", encoding="utf-8") as archivo:
            # quitar espacios en blanco
            palabras = [linea.strip() for linea in archivo.readlines()]
        return palabras
    except FileNotFoundError:
        print("El archivo palabras.txt no se encuentra en el directorio.")
        return []

def mostrar_palabras(palabras):
    if not palabras:
        print("No hay palabras para mostrar.")
        return
    
    for i in range(0, len(palabras), 20):
        print("\n".join(palabras[i:i+20]))  # 20 palabras
        if i + 20 < len(palabras):
            input("Presiona Enter para ver más...")

def menu():
    palabras = []
    
    while True:
        print("\nMenú de opciones:")
        print("[1] – Importar palabras clave")
        print("[2] – Mostrar palabras clave")
        print("[0] – Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            palabras = carga_palabras()
            print(f"Se han importado {len(palabras)} palabras clave.")
        
        elif opcion == "2":
            mostrar_palabras(palabras)
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
