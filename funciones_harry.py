import json
import sys
def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos = json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

def nombresyapodos_personajes(datos):
    lista = []
    for n in datos.get("personajes"):
        print("Personaje:",n.get("personaje"))
        print("Apodo:",n.get("apodo"))
        print("\r")
    return lista

def cuantos_estudiantes (datos):
    cont=0
    for n in datos.get("personajes"):
        if n.get("estudianteDeHogwarts") == True:
            cont+=1
    return cont

def nombresyapodo_casa (datos,casa):
    lista = []
    for n in datos.get("personajes"):
        if n.get("casaDeHogwarts")==casa:
            print("Personaje:",n.get("personaje"))
            print("Apodo:",n.get("apodo"))
            print("\r")
    return lista

def nombre_padremadre (datos,hijo):
    lista = []
    for n in datos.get("personajes"):
        for a in n.get("hijos"):
            if a == hijo:
                print("Personaje:",n.get("personaje"))
                print("Apodo:",n.get("apodo"))
    return lista

def personaje_casa (datos,casa):
    lista = []
    for n in datos.get("personajes"):
        if n.get("casaDeHogwarts")==casa:
            print("Personaje:",n.get("personaje"))
            print("Lo intrerpreta:",n.get("interpretado_por"))
            print("\r")
    return lista