import json
import os
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)

archivo = open("peliculas.json","r")
peliculas = json.load(archivo)
for pelicula in peliculas: # Aqui calcula el promedio de las calificaciones de la lista
        pelicula['calificacion'] = sum(pelicula['calificacion'])/len(pelicula)

def menu3ListEst():
    contLE = True
    while (contLE == True):
        print("\n\n############## Cinema+:                ##############")
        print("############# Reportes y estadisticas  ##############")
        print("#                                                   #")
        print("#      [1] Listado de Peliculas                     #")
        print("#      [2] Peliculas de mayor puntaje               #")
        print("#      [3] Peliculas disponibles en la plataforma   #")
        print("#      [0] Volver                                   #")
        print("#                                                   #")
        print("#####################################################")
        opcionLE = input("\nIngrese una opcion: ")
        
        if(opcionLE == '1'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [1] Listado de Peliculas                     #")
            print("#                                                   #")
            print("#####################################################")
            
            peliculas.sort(key=lambda x: x['titulo'])
            for pelicula in peliculas:
                print(f"{pelicula['titulo']} - {pelicula['genero']} - Calificacion: {pelicula['calificacion']}")
                print() # Espacio vacio
            input("Presione cualquier tecla para continuar ....")
        
        elif(opcionLE == '2'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [2] Peliculas de mayor puntaje               #")
            print("#                                                   #")
            print("#####################################################")
            
            peliculas.sort(key=lambda x: x['calificacion'], reverse=True)
            for pelicula in peliculas[0:15]: # Imprimimos las primeras 15 peliculas
                print(f"Titulo: {pelicula.get('titulo', 'N/A')}, Genero: {pelicula.get('genero', 'N/A')}, Calificación: {pelicula.get('calificacion', 'N/A')}")
                print() # Espacio vacio
            input("Presione cualquier tecla para continuar ....")
                
        elif(opcionLE == '3'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [3] Peliculas disponibles en la plataforma   #")
            print("#                                                   #")
            print("#####################################################")
            
            for pelicula in peliculas:
                try:
                    if pelicula['disponible'] == True :
                        print(f"Titulo: {pelicula['titulo']} - Disponible")
                except: 
                    print("\n")
                print() # Espacio vacio
            input("Presione cualquier tecla para continuar ....")
                
        elif(opcionLE == '0'):
            os.system("cls")
            print("\n\n#####################################################")
            print("#                                                   #")
            print("#      [0] Volver                                   #")
            print("#                                                   #")
            print("#####################################################")
            
            def volver():
                print("Aqui volver al MP")
            contLE = False
                
archivo.close()
