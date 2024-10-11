## libreria para palabras aleatorias (de las que yo he insertado en la coleccion)
import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "desarrollo", "juego", "ahorcado", 'angular','spring']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    estado = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return estado

def jugar():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos = 6

    print("Bienvenido al juego del ahorcado")
    
    while intentos > 0:
        print(f"\nPalabra: {mostrar_estado(palabra, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")
        
        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(letra)

        if letra not in palabra:
            intentos -= 1
            print("Letra incorrecta")
        else:
            print("Bien hecho")

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\nFelicidades! Has adivinado la palabra: {palabra}")
            break
    else:
        print(f"\nGame over. La palabra era: {palabra}")

def main():
    while True:
        jugar()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
