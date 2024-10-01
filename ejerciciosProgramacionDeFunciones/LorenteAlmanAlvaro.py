import math

# ejercicio 1
def area_rectangulo(base, altura):
    return base * altura
print((area_rectangulo(15, 10)))

#ejercicio 2
from math import pi

def area_circulo(radio):
    return pi * radio**2

(area_circulo(5))

# ejercicio 3
def relacion(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0
print(f"Resultado: {relacion(5, 10), relacion(10, 5), relacion(5, 5)}")

## ejercicio 4
def intermedio(num1, num2):
    return (num1 + num2) / 2

print (intermedio(-12, 24))

## ejercicio 5
def recortar(num, minimo, maximo):
    return max(min(num, maximo), minimo)

print (recortar(-2, 0, 10))

## ejercicio 6
numeros = [-12, 84, 13, 20, -33, 101, 9]

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
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]





