import json
import random
import os


def calificar_pelicula(lista):
    listaCalificada = []
    peliculasAlAzar = random.sample(lista, 10)

    for pelicula in peliculasAlAzar:
        os.system("cls")
        print("#"*90)
        print("#                                                                                        #")
        print("#                             Calificacion De Titulos                                    #")
        print("#                                                                                        #")
        print("#"*90)
        
        print(pelicula["titulo"])
        print()
        print(pelicula["sinopsis"])
        print()
        

        while True:
            try:
                calificacion = input("Ingrese su calificacion del 1 al 10 u oprima 0 (cero) para omitir calificacion: ")
                calificacion = int(calificacion)
                break
            except:
                print("Ingrese un numero entero")
                print()
        calificaciones = pelicula.get("calificacion", [])
        
        if calificacion >= 1 and calificacion <= 10:
            calificaciones.append(calificacion)
            listaCalificada.append({"titulo": pelicula["titulo"], "calificacion": calificacion})
            os.system("cls")
        elif calificacion == 0:
            print()  
        else:
            print()
            print("Ingrese un numero valido")
            while True: 
                print() 
                while True:
                    try:
                        calificacion = input("Ingrese su calificacion del 1 al 10 u oprima 0 (cero) para omitir: ")
                        calificacion = int(calificacion)
                        break
                    except:
                        print()
                        print("Ingrese un numero entero")
                        print()
                if calificacion >= 1 and calificacion <= 10:
                    calificaciones.append(calificacion)
                    listaCalificada.append({"titulo": pelicula["titulo"], "calificacion": calificacion})
                    break
                elif calificacion == 0:
                    break
                else: 
                    print()
                    print("Ingrese un numero valido")
                   
        archivo = open("peliculas.json","w")
        json.dump(lista, archivo, indent = 4)
        archivo.close()

    print("#"*90)
    print("#                                                                                        #")       
    print("#                             Titulos y sus Calificaciones                               #")
    print("#                                                                                        #")       
    print("#"*90)
    for pelicula in listaCalificada:
            print(pelicula["titulo"])
            print(pelicula["calificacion"])
            print("-"*90)
