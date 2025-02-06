acciones = ["jump", "run", "run", "run", "jump","run","jump"]
pista = "__|_|"

def funcion_evaluar(acciones: list, pista: str):

    superada = True
    pista_lista = list(pista)

    for parte in pista_lista:

        if(acciones[pista_lista.index(parte)] == "run" and parte == "|"):
            superada = False
            pista_lista[pista_lista.index(parte)] = "/"

        if(acciones[pista_lista.index(parte)] == "jump" and parte == "_"):
            superada = False
            pista_lista[pista_lista.index(parte)] = "x"
    
    pista = "".join(pista_lista)
    print(pista)

    return superada


print(funcion_evaluar(acciones, pista))
