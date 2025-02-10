def comprobar_expresion(expresion: str):

    correcta = True
    expresion_no_correcta = expresion[::-1]

    if(expresion[0] + expresion[-1] != "{}"):
        return False
    
    if(expresion.__contains__("[") and expresion.find("]") == -1
       and correcta == True):

        correcta = False
    
    if (expresion.__contains__("(") and expresion.find(")") == -1
        and correcta == True):

        correcta = False

    if (expresion_no_correcta.__contains__("]") and expresion.find("[") == -1
       and correcta == True):
        correcta = False
    
    if (expresion_no_correcta.__contains__(")") and expresion.find("(") == -1
       and correcta == True):
        correcta = False
    
    return correcta

print(comprobar_expresion("{[a * (c + d)] - 5}"))
print(comprobar_expresion("[(a + b) * {c / 2}]"))
print(comprobar_expresion("{[a + b] * (c - 7})"))

