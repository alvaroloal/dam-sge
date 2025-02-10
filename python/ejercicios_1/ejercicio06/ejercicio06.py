def funcion_arrays(array1: list, array2: list, booleano: bool):
    
    array_devuelto = set()

    if(booleano):

        for elemento1 in array1:

            if(elemento1 in array2):
                array_devuelto.add(elemento1)
            
        for elemento2 in array2:

            if(elemento2 in array1):

                array_devuelto.add(elemento2)

    if(not booleano):

        for elemento1 in array1:

            if(elemento1 not in array2):
                array_devuelto.add(elemento1)
            
        for elemento2 in array2:

            if(elemento2 not in array1):
                array_devuelto.add(elemento2)
    
    array_devuelto = list(array_devuelto)
    
    return array_devuelto

array1 = ["a", 1, "c", "d", "e"]
array2 = ["2", 1, "a", "b", "9"]

print(funcion_arrays(array1, array2, False))
print(funcion_arrays(array1, array2, True))