import os
import json
import funcComABM

# Funcion Alta de Peliculas
def alta_peli():
    peliculas = funcComABM.cargar_peliculas()
    id = peliculas[len(peliculas)-1]["id"] + 1
    titulo = input("\nIngresa el titulo de la pelicula: ").title()
    duracion = int(input("\nIngrese la duracion en minutos: "))
    sinopsis = input("\nIngrese una breve sinopsis de la pelicula: ").capitalize()
    pais_de_origen = input("\nIngrese el pais de origen: ").title()
    idioma = input("\nIngrese el idioma: ").capitalize()
    genero = funcComABM.validar_Gen()
    clasificacion = funcComABM.validar_Clasif()
    calificacion = []
    disponible = input("\nIngrese disponinilidad (s/n): ").lower()
    if(disponible == "s"): disponible = True
    else: disponible = False
    
    pelicula = { # Crea la pelicula en formato json para ser agregada a la BD
        "id": id,
        "titulo": titulo,
        "genero": genero,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "pais de origen": pais_de_origen,
        "idioma": idioma,
        "clasificacion": clasificacion,
        "calificacion": calificacion,
        "disponible": disponible
    }
        
    peliculas.append(pelicula)
    funcComABM.guardar_peliculas(peliculas)
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#     La pelicula ha sido agregada con éxito!!      #")
    print("#                                                   #")
    print("#####################################################")
    print() 
