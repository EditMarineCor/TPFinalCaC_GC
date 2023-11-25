import os
import json
import menu4Busq
import funcComABM

# Funcion Baja de Peliculas
def baja_peli():
    busqueda = menu4Busq.menu4Busq()
    opcionBusq = busqueda[0]
    buscado = busqueda[1]
    busqueda_peli(opcionBusq, buscado)
    input("Para continuar presione una tecla ...... ")

def busqueda_peli(opcionBusq, buscado):
    peliculas = funcComABM.cargar_peliculas()
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
        print(f"Y su id es: {peli_enc['id']}")
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
    funcComABM.guardar_peliculas(peliculas)
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#     La pelicula ha sido eliminada con éxito!!     #")
    print("#                                                   #")
    print("#####################################################")
    print()
