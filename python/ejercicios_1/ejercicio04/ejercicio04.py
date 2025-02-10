def palabra_mayuscula(str: str):

    str = str[0].upper() + str[1:len(str)]

    return str


def palabras_mayuscula(str: str):

    str = str.split(" ")

    for cadena in str:
        str[str.index(cadena)] = palabra_mayuscula(cadena)
    
    str = " ".join(str)

    return str


print(palabras_mayuscula("AL pan pan y al vino vino"))
print(palabras_mayuscula("caballo grande ande o no ande"))
print(palabras_mayuscula("yo tengo un jaco que me lleva al trabajo"))
