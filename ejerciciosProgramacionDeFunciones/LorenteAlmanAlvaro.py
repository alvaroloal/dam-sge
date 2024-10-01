import math

# ejercicio 1
def area_rectangulo(base, altura):
    return base * altura
print(f"Ejercicio 1. Area rectángulo: {(area_rectangulo(15, 10))}")

#ejercicio 2
from math import pi
def area_circulo(radio):
    return pi * radio**2
##print(f"\nEjercicio 2. Area círculo: {(area_circulo(5))}")
print(f"\nEjercicio 2. Área círculo: {round(area_circulo(5), 2)}") ## redondear a dos decimales


# ejercicio 3
def relacion(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0
print(f"\nEjercicio 3. Resultado: {relacion(5, 10), relacion(10, 5), relacion(5, 5)}")

## ejercicio 4
def intermedio(num1, num2):
    return (num1 + num2) / 2
print(f"\nEjercicio 4. Punto intermedio: {intermedio(-12, 24)}")


## ejercicio 5
def recortar(num, minimo, maximo):
    return max(min(num, maximo), minimo)
print(f"\nEjercicio 5. {recortar(15, 0, 10)}")



## ejercicio 6
numeros = [6, 5, 2, 1, 7]
def separar(*args):
    lista = sorted(args)
    pares = []
    impares = []
    for arg in lista:
        if arg % 2 == 0:
            pares.append(arg)
        else:
            impares.append(arg)
        
    return pares, impares

pares, impares = separar(*numeros)
print(f"\nEjercicio 6. Número pares de la cadena: {(pares)}")
print(f"\t\tNúmeros impares de la cadena: {(impares)}")