import os
import json
import menu4Busq

# Funcion Baja de Peliculas
def baja_peli():
    busqueda = menu4Busq.menu4Busq()
    print("Busqueda: ", busqueda)
    opcionBusq = busqueda[0]
    buscado = busqueda[1]
    busqueda_peli(opcionBusq, buscado)
    input("presiona tecla para continuar")

def cargar_peliculas():# Carga la BD Json de peliculas
    try: 
        with open("peliculas.json", "r") as archivo:
            return json.load(archivo) 
    except FileNotFoundError: 
        peliculas = []
        guardar_peliculas(peliculas)
        print("El archivo que desea abrir no existe!!")

def guardar_peliculas(peliculas): 
    with open("peliculas.json", "w") as archivo: 
        json.dump(peliculas, archivo)

def busqueda_peli(opcionBusq, buscado):
    peliculas = cargar_peliculas()
    peli_enc = {}
    for pelicula in peliculas: 
        if opcionBusq == "1" and buscado == pelicula['id']:
            peli_enc = pelicula
            indice_peli = peliculas.index(pelicula)
            break
        elif opcionBusq == "2" and buscado.lower() in pelicula['titulo'].lower():
            peli_enc = pelicula
            indice_peli = peliculas.index(pelicula)
            break
        elif (opcionBusq == "3"): # Busqueda secuencial
            pass
    if (peli_enc) != {}:
        print(f"Se ha encontrado la siguiente pelicula: {peli_enc['titulo']}")
        print(f"Y se encuentra en la siguiente posicion: {indice_peli}")
        modif = input("\nDesea eliminar esta pelicula? (s/n): ").lower()
        if(modif == "s"): modif_datos(peliculas, peli_enc, indice_peli)
    elif (opcionBusq == "1"):
        print(f"No se encontro una peliculas con el id: {buscado}")
    elif (opcionBusq == "2"):
        print(f"No se encontro una peliculas con el Titulo: {buscado}")
    input("Para continuar presione una tecla ...... ")
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#      [3] Baja de pelicula existente               #")
    print("#                                                   #")
    print("#####################################################")

def modif_datos(peliculas, peli_enc, indice_peli):
    peliculas.pop(indice_peli)
    guardar_peliculas(peliculas)
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#     La pelicula ha sido eliminada con éxito!!     #")
    print("#                                                   #")
    print("#####################################################")
    print()

def validar_Gen():
        lista_genero = ["1 - Acción", "2 - Animación", "3 - Comedia", 
                        "4 - Drama", "5 - Ciencia ficción", "6 - Terror",
                        "7 - Suspenso", "8 - Romántica"]
        condicion = True
        while(condicion == True):
            print("Opciones de genero: ", lista_genero)
            gen = int(input("Ingresa el genero de la pelicula (1 al 8): "))
            if(0 < gen < 9):
                condicion = False
            else:
                print("Ingrese una opcion valida!!")
        return lista_genero[gen -1][4::]

def validar_Clasif():
        lista_clasific = ["1 - ATP", "2 - PG", "3 - PG-14", "4 - R", "5 - NC-18"]
        condicion = True
        while(condicion == True):
            print("Opciones de clasificacion: ", lista_clasific)
            clasif = int(input("Ingresa la clasificacion de la pelicula (1 al 5): "))
            if(0 < clasif < 6):
                condicion = False
            else:
                print("Ingrese una opcion valida!!")
        return lista_clasific[clasif -1][4::]


