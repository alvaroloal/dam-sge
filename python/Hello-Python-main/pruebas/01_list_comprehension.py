# lista original
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)
# salida: [0, 1, 2, 3, 4, 5, 6, 7]

# rango convertido a lista
my_range = range(8)
print(list(my_range))
# salida: [0, 1, 2, 3, 4, 5, 6, 7]

# crear una lista con elementos incrementados en 1
my_list = [i + 1 for i in range(20)]
print(my_list)
# salida: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#  crear una lista con elementos multiplicados por 2
my_list = [i * 2 for i in range(8)]
print(my_list)
# salida: [0, 2, 4, 6, 8, 10, 12, 14]

# crear una lista con elementos elevados al cuadrado
my_list = [i * i for i in range(8)]
print(my_list)
# salida: [0, 1, 4, 9, 16, 25, 36, 49]



# función que suma 5 a un número
def sum_five(number):
    return number + 5
#  aplicar la función sum_five a cada elemento del rango
my_list = [sum_five(i) for i in range(8)]
print(my_list)
# salida: [5, 6, 7, 8, 9, 10, 11, 12]
