#Encuentra todos los números del 1 al 1000 que sean divisibles por 7
print()
funcion_divisibles_por_7 = [num for num in range(1, 1001) if num % 7 == 0]
print(funcion_divisibles_por_7)
print()

#Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.
funcion_numeros_con_3 = [num for num in range(1, 1001) if '3' in str(num)]
print(funcion_numeros_con_3)
print()

#Contar el número de espacios en una cadena
cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
numero_espacios = cadena.count(' ')
print(f"Número de espacios en la cadena: {numero_espacios}")
print()

#Crea una lista de todas las consonantes de la cadena “A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos”
cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
vocales = "aeiouáéíóúü"
consonantes = [consonantes for consonantes in cadena.lower() if consonantes.isalpha() and consonantes not in vocales]
print(f"Consonantes de la cadena: {consonantes}") 
print()


#Obtén el índice y el valor como una tupla para los elementos de la lista “hi”, 4, 8.99, 'apple', ('t,b','n'). El resultado se vería así (índice, valor), (índice, valor)
elementos = ["hi", 4, 8.99, "apple", ("t,b", "n")]
resultado = list(enumerate(elementos))
print(f"Indice - valor: {resultado}")
print()

#Encuentra los números comunes en dos listas (sin usar una tupla o conjunto) lista_a = 1, 2, 3, 4, lista_b = 2, 3, 4, 5
lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]
numeros_comunes = [num for num in lista_a if num in lista_b]
print(f"Los números comunes de las dos listas son: {numeros_comunes}") 
print()

#Obtén solamente los números en una oración como 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'
oracion = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"
numeros = [int(s) for s in oracion.split() if s.isdigit()]
print(f"Los números de la oración son: {numeros}") 
print()

#Dado numbers = range(20), se genera una lista que contiene la palabra "par" si un número en los números es par, y la palabra "impar" si el número es impar. El resultado se vería así: "impar", "impar", "par".
numbers = range(20)
par_impar = ["par" if num % 2 == 0 else "impar" for num in numbers]
print(par_impar)
print()

#Generar una lista de tuplas que consten únicamente de los números coincidentes en estas listas list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. El resultado se vería así (4,4), (12,12)
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
coincide = [(num, num) for num in list_a if num in list_b]
print(coincide)
print()


#Encuentra todas las palabras en una cadena que tengan menos de 4 letras
txt = "La Giralda presume orgullosa de ver al Sevilla en el Sanchez Pizjuan"
palabras_cortas = [palabra for palabra in txt.split() if len(palabra) < 4]
print(palabras_cortas)
print()

#Utiliza una comprensión de lista anidada para encontrar todos los números del 1 al 1000 que sean divisibles por cualquier dígito excepto 1 (2-9)
numeros_divisibles = [num for num in range(1, 1001) if any(num % d == 0 for d in range(2, 10))]
print(numeros_divisibles)
print()