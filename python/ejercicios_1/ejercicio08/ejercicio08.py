def resultado_batalla(ejercito1: list, ejercito2: list):

    razas_bondadosas = {

        "Peloso": 1,
        "Sureño bueno": 2,
        "Enano": 3,
        "Númenóreano": 4,
        "Elfo": 5
    }

    razas_malvadas = {

        "Sureño malo": 2,
        "Orco": 2,
        "Goblin": 2,
        "Huargo": 3,
        "Troll": 5
    }

    valor_ejercito1 = sum(list(map(lambda raza: razas_bondadosas[raza], ejercito1)))

    valor_ejercito2 = sum(list(map(lambda raza: razas_malvadas[raza], ejercito2)))

    if(valor_ejercito1 > valor_ejercito2):
        return "Ha ganado el ejercito de los buenos"
    
    if(valor_ejercito2 > valor_ejercito1):
        return "Ha ganado el ejercito de los malos"
    
    return "Empate"



ejercito_bondadoso_1, ejercito_malvado_1 = ["Elfo", "Enano", "Sureño bueno", "Peloso"], ["Orco", "Huargo", "Goblin", "Troll"]

ejercito_bondadoso_2, ejercito_malvado_2 = ["Peloso", "Sureño bueno", "Elfo"], ["Huargo", "Goblin"]

print(resultado_batalla(ejercito_bondadoso_1, ejercito_malvado_1))
print(resultado_batalla([], []))
print(resultado_batalla(ejercito_bondadoso_2, ejercito_malvado_2))


