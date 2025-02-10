def funcion_ganador_rps(lista_pares: list):

    victoria1 = 0
    vitoria2 = 0

    for par in lista_pares:

        match(par):
            case ("R", "S"):
                victoria1+=1
            case ("S", "R"):
                vitoria2+=1
            case ("S", "P"):
                victoria1+=1
            case ("P", "S"):
                vitoria2+=1
            case ("P", "R"):
                victoria1+=1
            case ("R", "P"):
                vitoria2+=1
    
    if(victoria1 > vitoria2):

        return "Player 1"
    
    if(vitoria2 > victoria1):

        return "Player 2"
    
    return "Tie"

lista_pares1 = [("P", "R"), ("R", "P"), ("S", "P")]

lista_pares_2 = [("R", "R"), ("P", "P"), ("R", "P")]

lista_pares_3 = [("P", "S"), ("S", "R"), ("R", "P")]

print(funcion_ganador_rps(lista_pares1))
print(funcion_ganador_rps(lista_pares_2))
print(funcion_ganador_rps(lista_pares_3))