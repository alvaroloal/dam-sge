import csv

def leer_notas(fichero):
    alumnos = []
    with open(fichero, mode='r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        for row in reader:
            nombre = row['Nombre']
            apellidos = row['Apellidos']
            curso = row['Curso']
            notas = {asig: int(row[asig]) for asig in ["FH", "LM", "ISO", "FOL", "PAR", "SGBD"]}
            alumnos.append({"nombre": nombre, "apellidos": apellidos, "curso": curso, "notas": notas})
    return alumnos

def calcular_media(notas):
    return sum(notas.values()) / len(notas)

def mostrar_media_alumnos(alumnos):
    for alumno in alumnos:
        media = calcular_media(alumno["notas"])
        print(f"{alumno['nombre']} {alumno['apellidos']} - Media: {media:.2f}")

def mostrar_notas_asignatura(alumnos, curso, asignatura):
    for alumno in alumnos:
        if alumno["curso"] == curso:
            print(f"{alumno['nombre']} {alumno['apellidos']}: {alumno['notas'].get(asignatura, 'N/A')}")

def porcentaje_aprobados(alumnos, curso):
    asignaturas = set()
    aprobados = {}
    total_alumnos = 0
    
    for alumno in alumnos:
        if alumno["curso"] == curso:
            total_alumnos += 1
            for asig, nota in alumno["notas"].items():
                asignaturas.add(asig)
                if nota >= 5:
                    aprobados[asig] = aprobados.get(asig, 0) + 1
    
    if total_alumnos > 0:
        for asig in asignaturas:
            porcentaje = (aprobados.get(asig, 0) / total_alumnos) * 100
            print(f"{asig}: {porcentaje:.2f}% de aprobados")

def generar_fichero_curso(alumnos, curso):
    with open(f"{curso}.txt", "w", encoding="utf-8") as f:
        for alumno in alumnos:
            if alumno["curso"] == curso:
                media = calcular_media(alumno["notas"])
                f.write(f"{alumno['nombre']} {alumno['apellidos']} - Media: {media:.2f}\n")
    

def menu():
    alumnos = leer_notas("notas.csv")
    while True:
        print("\nMenú:")
        print("1. Mostrar listado de alumnos con nota media")
        print("2. Mostrar notas de una asignatura en un curso")
        print("3. Mostrar porcentaje de aprobados por asignatura en un curso")
        print("4. Generar fichero con notas medias de un curso")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_media_alumnos(alumnos)
        elif opcion == "2":
            curso = input("Introduce el curso: ")
            asignatura = input("Introduce la asignatura: ")
            mostrar_notas_asignatura(alumnos, curso, asignatura)
        elif opcion == "3":
            curso = input("Introduce el curso: ")
            porcentaje_aprobados(alumnos, curso)
        elif opcion == "4":
            curso = input("Introduce el curso: ")
            generar_fichero_curso(alumnos, curso)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, introduce una opción que sea válida.")

if __name__ == "__main__":
    menu()