print("Hola mundo")

print(2+3)
print(2-3)
# Módulo
print(3 % 2)

res= None
res = "Hola"##sobrescribir
print(res)


cadena = "Hola 'me llamo Alvaro'"
print(cadena)

cadena_salto_linea = "Hola\mundo"
print("Un texto\tuna tabulación")
print("Un texto\nuna nueva línea")



print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)

diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")

palabra = "Python"
palabra[0] # carácter en la posición 0
print(palabra[3])

palabra2 = "Spring"
print (palabra2[0:2])

print (palabra2[:2])

##inmutabilidad
palabra = "N" + palabra[1:]
palabra


#funciones
def nombre_funcion(parametro1):

    return parametro1



palabra = "Python"
len(palabra)

##listas
numeros = [1,2,3,4]
print (numeros)

##listas anidadas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)
##para acceder a la posicio del numero 3
print(r[0][2])##accedo al elemento grande y luego al pequeño

print(r[0][1:3])##accedo a las posiciones segunda y tercera

print(r[0])       # Primera sublista
print(r[-1])      # Última sublista

print(r[0][0])    # Primera sublista, y de ella, primer ítem
print(r[1][1])    # Segunda sublista, y de ella, segundo ítem
print(r[2][2])    # Tercera sublista, y de ella, tercer ítem
print(r[-1][-1])  # Última sublista, y de ella, último ítem



# valor = input("Introduce un valor: ")  # Podemos mostrar un mensaje
# valor

# valor = int(input("Introduce un número entero: "))
# valor * 2

##Condicionales
nota = float(input("Introduce una nota: "))

if nota >= 9:
    print("Sobresaliente")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota < 5:
    print("Insuficiente")


##Sirve para como instrucción de paso para utilizar en un bloque de código vacío, no finaliza el código. No tiene ningún efecto pero sirve para crear estructuras pendientes de ser programadas
if True:
    pass


##while
c = 0
while c <= 5:
    c+=1
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)


##break
c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)
    
#     ##Ejemplo menú interactivo
#     print("Bienvenido al menú interactivo")
# while(True):
#     print("""¿Qué quieres hacer? Escribe una opción
#     1) Saludar
#     2) Sumar dos números
#     3) Salir""")
#     opcion = input()
#     if opcion == '1':
#         print("Hola, espero que te lo estés pasando bien")
#     elif opcion == '2':
#         n1 = float(input("Introduce el primer número: "))
#         n2 = float(input("Introduce el segundo número: "))
#         print("El resultado de la suma es: ",n1+n2)
#     elif opcion =='3':
#         print("¡Hasta luego! Ha sido un placer ayudarte")
#         break
#     else:
#         print("Comando desconocido, vuelve a intentarlo")

##for con listas
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1

for numero in numeros:  # Para [variable] en [lista]
    print(numero)


##for con cadenas
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)



##Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:
for numero in numeros:
    numero *= 10   
numeros


##enumerate 
##Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print (numeros)

##for con cadenas
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)


##Funcion range
for i in range(10):
    print(i) 

list(range(10))


##Tuplas
tupla = (100,"Hola",[1,2,3],-50)
print (tupla)

print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])


##longuitud de la tupla
len(tupla)


##para buscar un elemento y saber su posición en la tupla:
tupla.index(100)
tupla.index('Hola')

## para contar cuantas veces aparece un elemento en una tupla:
tupla.count(100)

tupla = (100,100,100,50,10)
tupla.count(100)

##las tuplas no disponen de métodos para modificar su contenido:
tupla.append(10)
##da error


##Conjuntos


##Para definir un conjunto vacío hay que llamar a su clase set (conjunto en inglés):
conjunto = set()
conjunto

##si lo creamos con algunos datos se definen entre llaves:
conjunto = {1,2,3}
conjunto

##add
##Sirve para añadir elementos al conjunto, pero si un elemento ya se encuentra no se añadirá de nuevo:
conjunto.add(4)
conjunto

##gestionan automáticamente la posición de sus elementos, en lugar de conservarlos en la posición que nosotros los añadimos:
conjunto.add('H')
conjunto.add('A')
conjunto.add('Z')
conjunto

##Pertenencia a grupos
grupo = {'Hector','Juan','Mario'}

##Es fácil saber si un elemento se encuentra en un conjunto utilizando la sintaxis in. Se utiliza mucho para trabajar con grupos:
'Hector' in grupo
'Hector' not in grupo

##Diccionarios
## se definen igual que los conjuntos, utilizando llaves, pero también se pueden crear vacíos con ellas:
vacio = {}
vacio

##Si consultamos el tipo de la variable que contiene un diccionario con la función type() encontraremos la palabra dict, esa es la clase que define los diccionarios:
type(vacio)


##Definicion diccionario
##Para cada elemento se define la estructura clave:valor:
colores = {'amarillo':'yellow','azul':'blue'}
colores

##Para consultar el valor de una clave utilizaremos la clave a modo de índice:
colores['amarillo']

##Mutabilidad
colores['verde'] = 'green'
colores
##se puede sobrescribir valor
colores['amarillo'] = 'white'
colores

##Función del()
del(colores['amarillo'])
colores

numeros = {10:'diez',20:'veinte'}
numeros[10]

edades = {'Hector':27,'Juan':45,'Maria':34}
edades['Hector']+=1
edades

edades['Juan'] + edades['Maria']


##letra secuencial
edades = {'Hector':27,'Juan':45,'Maria':34}

for edad in edades:
    print(edad)
    
for clave in edades:
    print(edades[clave])
    
for clave in edades:
    print(clave,edades[clave])
    
for clave, valor in edades.items():
    print(clave, valor)
    
##lista de diccionarios
personajes = []

gandalf = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
legolas = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
gimli = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}

personajes.append(gandalf)
personajes.append(legolas)
personajes.append(gimli)

print(personajes)

for pesonaje in personajes:
    print(pesonaje['Nombre'], pesonaje['Clase'], pesonaje['Raza'])


##Pilas
pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)
##sacar elementos
print(pila.pop())
print(pila)

numero = pila.pop()
print(numero)

##Colas
##Debemos importar la colección deque manualmente para crear una cola:
from collections import deque
cola = deque()
print(cola)

cola = deque(['Hector','Juan','Miguel'])
print(cola)

cola.append('Maria')
cola.append('Arnaldo')
print(cola)

print(cola.popleft())
print(cola)

persona = cola.popleft()
print(persona)
print(cola)
