from funciones_harry import *

pruebas = leer_json("harry_potter.json")

opcion = int(input('''
1. Listar el nombre de los personajes y su apodo
2. Contar cuantos son estudiantes de Hogwarts
3. Mostrar los personajes y su apodo de la casa introducida por teclado
4. Introduce un hijo y te muestra quien es el padre/madre
5. Introduce el nombre de una casa y te muestra que personajes hay en cada casa y quien lo interpreta
6. Salir del programa

Elije una opcion: '''))

while opcion != 6:
    if opcion == 1:
        dato = nombresyapodos_personajes(pruebas)
        for a in dato:
            print(a)

    if opcion == 2:
        print("Hay",cuantos_estudiantes(pruebas),"estudiantes de Hogwarts")

    if opcion == 3:
        casa = input("Dime una casa (Gryffindor, Slytherin, Huffelpuff, Ravenclaw): ")
        print("\r")
        dato = nombresyapodo_casa(pruebas,casa)
        for a in dato:
            print(a)

    if opcion == 4:
        hijo = input("Dime un hijo: ")
        print("\r")
        print("Padres:")
        dato = nombre_padremadre(pruebas,hijo)
        for a in dato:
            print(a)

    if opcion == 5:
        casa = input("Dime una casa (Gryffindor, Slytherin, Huffelpuff, Ravenclaw): ")
        print("\r")
        dato = personaje_casa(pruebas,casa)
        for a in dato:
            print(a)

    opcion = int(input('''
1. Listar el nombre de los personajes y su apodo
2. Contar cuantos son estudiantes de Hogwarts
3. Mostrar los personajes y su apodo de la casa introducida por teclado
4. Introduce un hijo y te muestra quien es el padre/madre
5. Introduce el nombre de una casa y te muestra que personajes hay en cada casa y quien lo interpreta
6. Salir del programa

Elije una opcion: '''))
print("\r")
print("Ha salido del programa")