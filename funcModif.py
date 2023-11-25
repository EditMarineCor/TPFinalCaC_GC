import os
import json
import menu4Busq
import funcComABM

# Funcion Modificacion de Peliculas
def modif_peli():
    busqueda = menu4Busq.menu4Busq()
    print("Busqueda: ", busqueda)
    opcionBusq = busqueda[0]
    buscado = busqueda[1]
    if opcionBusq == "0":
        return
    busqueda_peli(opcionBusq, buscado)
    input("presiona tecla para continuar ...... ")
    
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
        modif = input("\nDesea modificar esta pelicula? (s/n): ").lower()
        if(modif == "s"): modif_datos(peliculas, peli_enc, indice_peli)
    elif (opcionBusq == "1"):
        print(f"No se encontro una peliculas con el id: {buscado}")
    elif (opcionBusq == "2"):
        print(f"No se encontro una peliculas con el Titulo: {buscado}")
    input("Para continuar presione una tecla ...... ")
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#      [2] Modificacion de pelicula existente       #")
    print("#                                                   #")
    print("#####################################################")

def modif_datos(peliculas, peli_enc, indice_peli):
    id = peli_enc['id'] # Conserva el mismo id
    consulta = input(f"\nTitulo: {peli_enc['titulo']}, Desea modificarlo? (s/n): ").lower()
    if(consulta == "s"): titulo = input("Reingrese el titulo: ")
    else: titulo = peli_enc['titulo']
    consulta = input(f"\nGenero: {peli_enc['genero']}, Desea modificarlo? (s/n): ").lower()
    if(consulta == "s"): genero = funcComABM.validar_Gen()
    else: genero = peli_enc['genero']
    consulta = input(f"\nDuracion: {peli_enc['duracion']}, Desea modificarla? (s/n): ").lower()
    if(consulta == "s"): duracion = int(input("Reingrese la duracion: "))
    else: duracion = peli_enc['duracion']
    consulta = input(f"\nSinopsis: {peli_enc['sinopsis']}, Desea modificarla? (s/n): ").lower()
    if(consulta == "s"): sinopsis = input("Reingrese la sinopsis: ")
    else: sinopsis = peli_enc['sinopsis']
    consulta = input(f"\nPais de origen: {peli_enc['pais de origen']}, Desea modificarlo? (s/n): ").lower()
    if(consulta == "s"): pais_de_origen = input("Reingrese el pais de origen: ")
    else: pais_de_origen = peli_enc['pais de origen']
    consulta = input(f"\nIdioma: {peli_enc['idioma']}, Desea modificarlo? (s/n): ").lower()
    if(consulta == "s"): idioma = input("Reingrese el idioma: ")
    else: idioma = peli_enc['idioma']
    consulta = input(f"\nClasificacion: {peli_enc['clasificacion']}, Desea modificarla? (s/n): ").lower()
    if(consulta == "s"): clasificacion = funcComABM.validar_Clasif()
    else: clasificacion = peli_enc['clasificacion']
    calificacion = peli_enc['calificacion']
    consulta = input(f"\nDisponible: {peli_enc['disponible']}, Desea modificarlo? (s/n): ").lower()
    if(consulta == "s"): 
        disp = input("Reingrese la disponibilidad (s/n): ").lower()
        if(disp == "s"): disponible = True
        else: disponible = False
    else: disponible = peli_enc['disponible']
    
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
    peliculas.pop(indice_peli)
    peliculas.insert(indice_peli, pelicula)
    funcComABM.guardar_peliculas(peliculas)
    os.system("cls")
    print("\n\n#####################################################")
    print("#                                                   #")
    print("#     La pelicula ha sido modificada con éxito!!    #")
    print("#                                                   #")
    print("#####################################################")
    print()
